import pandas as pd

pathToExcel = "pandas_to_excel.xlsx"

def readFromExcel():
    userSheet = pd.read_excel(f"{pathToExcel}", sheet_name="pryce14")
    userSheetList = userSheet["outer-links"].to_list()
    return userSheetList

def writeToExcel(arr, colName: str, user: str):
    df = pd.DataFrame(arr, columns=[f"{colName}"])
    print(df)
    df.to_excel(pathToExcel, sheet_name=f"{user}")