# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# launcher.py:  Main launcher for Recalculation. This file contains a "main" function           # 
#               that calls all other required modules. The main function accepts user input to  #
#               determine whether Database Load or Report Generation is required.               #
#                                                                                               #
# Author(s):  Sarah Torrence                                                                    #
#                                                                                               #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import dbLoad
from timer import timedFunction
import generateReport

@timedFunction
def main():
    """
    Description:    Launch point for the program. Calls all other modules.

    Return:         VOID
    """

    executionFlag = input("Enter \"d\" for DB Load or \"g\" to Generate Report: ").lower()


    if(executionFlag == "d"):
        # Load File Data into Dataframe
        dbLoad.loadData()
        dbLoad.loadReports()

    elif(executionFlag == "g"):
        # Generate Validation Report
        generateReport.generateReport()

    else:
        dbLoad.loadData()
        generateReport.generateReport()

    print("Program run complete!")
    
if __name__ == "__main__":
    main()

