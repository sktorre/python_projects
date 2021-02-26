# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# config.py:  This class is used to store many of the variables required by the program. This   #
#             class is used in lieu of an actual config/settings file for ease-of-use.          #
#                                                                                               #
# Author(s):  Sarah Torrence                                                                    #
#                                                                                               #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import pandas as pd
import datetime

class Config:
    """
    Description:    This class serves as a CONFIG file. Change strings as necessary to adjust output.

    Attributes:     Broken into sections based on comment headers.
    """

    # Client Name and current year
    CLIENT_NAME = ""
    CURRENT_YEAR = 2020

    #Directories    
#    INPUT_DIRECTORY = "../Data"
    INPUT_DIRECTORY = ""
    DB_DIRECTORY = "../Database"
    LOCATION_DIRECTORY = "../Location"
    QUERY_DIRECTORY = "../Queries"
    EXCEL_DIRECTORY = ".."
    REPORTS_DIRECTORY = "../Reports"

    #Headers        
    Headers = [""]
    Merg_Headers = [""]
    Drop_Headers_MSA = ["PostalCode","PostalCode_y","code"]

    #Location Files   
    TimeZone = pd.read_csv(LOCATION_DIRECTORY + "/" + "" ,sep='\t',names = ['Time Zone'])
    ZipCode = pd.read_csv(LOCATION_DIRECTORY + "/" + "" ,sep='\t')
    MSA = pd.read_csv(LOCATION_DIRECTORY + "/" + "" ,sep='\t', names = ['MSA'])
    MSA_LookUp = pd.read_csv(LOCATION_DIRECTORY + "/" + "")
    PublicMSA = pd.read_csv(LOCATION_DIRECTORY + "/" + "PublicMSA.csv")
    
    #Dictionary with time zone adjustments
    TZ_dict = {'America/Los_Angeles': datetime.timedelta(hours=7), 'America/New_York': datetime.timedelta(hours=4), 'America/Chicago': datetime.timedelta(hours=5),
     'America/Phoenix': datetime.timedelta(hours=6), 'America/Denver': datetime.timedelta(hours=6), 'Pacific/Honolulu': datetime.timedelta(hours=10),
     'America/Puerto_Rico': datetime.timedelta(hours=4), 'America/Anchorage': datetime.timedelta(hours=8)}
    
    #Report/Database/Table names
    tableName = "Data"
    DB_NAME = "WCML.sqlite"
    CAMPAIGNID_COLUMN_HEADER = "Market"
    EXCEL_NAME = "FinalReport.xlsx"
    EXCEL_RESULT_SHEET = "Recalculated Values"
    EXCEL_QUERY_SHEET = "Queries"
    DATA_FILE = "Data.csv"
    
    #Sample Selection information
    NumSelections = 10
    
    Market = [""]

    
   





