# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# dbLoad.py:  This file contains the functions that read in the log files and load the cleaned  #
#             and filtered data into a database to perform aggregated recalculations.           #        
#                                                                                               #
# Author(s):  Sarah Torrence                                                                    #
#                                                                                               #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import pandas as pd
import os
from timer import timedFunction
from config import Config
import recalculate
import sqlite3

@timedFunction
def loadData():
    """
    Description: This function iterates through all the log files, reading them in, performing all
                 cleaning, filtering and calculation functions and loading the data into a database

    Return:         VOID 
    """
    con = sqlite3.connect(Config.DB_DIRECTORY + "/" + Config.DB_NAME)
    cur = con.cursor()
    counter = 0
    print("Loading in ")
    if os.path.exists(Config.INPUT_DIRECTORY + "/" + Config.DATA_FILE):
        os.remove(Config.INPUT_DIRECTORY + "/" + Config.DATA_FILE)
    for i in os.listdir(Config.INPUT_DIRECTORY):
        for folder in os.listdir(Config.INPUT_DIRECTORY + "/" + i):
            for file in os.listdir(Config.INPUT_DIRECTORY + "/" + i + "/" + folder):
                if os.path.isfile(os.path.join(Config.INPUT_DIRECTORY + "/" + i + "/" + folder, file)):
                    if os.path.splitext(file)[1].lower() == ".csv":
                        counter += 1
                        Data = pd.read_csv(Config.INPUT_DIRECTORY + "/" + i + "/" + folder + "/" + file,sep='\t',names = Config.Headers,engine='python')
                        Data['Exclusion'] = i
                        Data = manipulateFrame(Data)
                        Data = FilterFiles(Data,Config.NumSelections,cur,con)
                        print("Appended ", file, " to data set as file ",counter) 
    con.commit()
    con.close()
   
    
@timedFunction    
def manipulateFrame(x):
    """
    Description: This function runs the filtering and cleaning functions from recalculate    

    Return:         x - dataframe with session data 
    """

    x = recalculate.TimeZone_normalize(x)
    x = recalculate.Geo_locate(x)
    x = recalculate.Determine_Age(x)
    return x

@timedFunction
def FilterFiles(x,NumSelections,cur,con):
    """
    Description: This function runs the selection filter for each sample selection and appends them each
                 into a table in a sqlite database

    Return:         x - dataframe
    """
    for selection in range(NumSelections):
        #create a dataframe with filtered data
        DF = pd.DataFrame()
        DF = recalculate.SelectionFilter(x,Config.Market[selection],Config.Start[selection],Config.End[selection],Config.AgeStart[selection],Config.AgeEnd[selection])
        #DF = Recalculate(DF,Config.Start[selection],Config.End[selection])
        #appends the dataframe to a table in a sqlite database
        DF.to_sql(Config.tableName + str(selection+1), con, if_exists='append', index=False)
    return x

@timedFunction
def loadReports():
    """
    Description: Load the provided reports in the sqlite database for tie outs

    Return:         VOID
    """
    con = sqlite3.connect(Config.DB_DIRECTORY + "/" + Config.DB_NAME)
    counter = 1
    for i in os.listdir(Config.REPORTS_DIRECTORY):
        table = pd.read_csv(Config.REPORTS_DIRECTORY + "/" + i)
        table.to_sql(Config.CLIENT_NAME + str(counter), con, if_exists='replace', index=False)
        counter += 1
    Config.file.to_sql('file_name', con, if_exists='replace', index=False)
    con.commit()
    con.close()
    

