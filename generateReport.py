# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# generateReport.py:  This file generates an excel report with a tab for each sample selection. #                                           
#                                                                                               # 
# Author(s):  Sarah Torrence                                                                    #
#                                                                                               #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import sqlite3
import os
import pandas as pd
from config import Config
from timer import timedFunction

        
@timedFunction
def generateReport():
    """
    Description:    This function executes a sqlite script for each sample selection and outputs a comparison
                    between the provided weekly reports and the aggregated recalculated values 

    Return:         VOID
    """
    excelFilepath = Config.EXCEL_DIRECTORY + "/" + Config.CLIENT_NAME + "_" + Config.EXCEL_NAME
    
    # Delete Existing Report if Exists
    try:
        os.remove(excelFilepath)
    except OSError:
        pass
    
    #connect to the database and excel file        
    con = sqlite3.connect(Config.DB_DIRECTORY + "/" + Config.DB_NAME)
    cur = con.cursor()
    counter = 1
    writer = pd.ExcelWriter(excelFilepath)
    
    #run the query for each selection and output each one and each query in separate tabs in excel
    for i in os.listdir(Config.QUERY_DIRECTORY):
        with open(Config.QUERY_DIRECTORY + "/Selection" + str(counter) + ".sql", "r") as queryFile:
            query = "".join(queryFile.readlines())
            query_df = pd.DataFrame({'Query': [query]})
            cur.executescript(query)
        try:
            df = pd.read_sql_query("select * from OUTPUT" + str(counter), con)
            df.to_excel(writer, sheet_name='Selection' + str(counter) + " Recalculated Values", index=False)
            query_df.to_excel(writer, sheet_name= 'Selection' + str(counter) + " Query", index=False)
            print("Sucessfully created sheet for Selection " + str(counter) + " in " + excelFilepath)
            counter += 1
        except PermissionError:
            print("Failed to generate Excel report because file is already open.") 
    writer.save()
    con.commit()
    con.close()     
    


