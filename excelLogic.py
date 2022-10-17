import pandas as pd

pathToExcel = "pandas_to_excel.xlsx"

def readFromExcel():
    userSheet = pd.read_excel(f"{pathToExcel}", sheet_name="user1")
    userSheetList = userSheet["main-links"].to_list()
    return userSheetList