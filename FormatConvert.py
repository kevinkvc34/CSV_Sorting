import pandas as pd
from pandas import DataFrame, read_csv
import os
import math

pd.options.mode.chained_assignment = None
newFormat = pd.read_csv("lexisupload.csv", skipinitialspace=True)
oldFormat = pd.read_csv("final_csv.csv", skipinitialspace=True)
newFormat.sort_values(by="ID", ascending=True)
oldFormat.sort_values(by="ID", ascending=True)

print(newFormat)
print(oldFormat)

newList = list(newFormat["ID"])
oldList = list(oldFormat["ID"])

def ridValid(inputDf, old, new):
    for x in range(len(new)): #length of new formatted list
        print("{}".format(new[x]))
        if not new[x] in old:
            inputDf = inputDf.drop([x])
            # print(inputDf["ID"][x]) 
    return inputDf

newDF = ridValid(newFormat, oldList, newList)
newDF.sort_values(by="Last Name", ascending=True)

# get all addresses:
for y in range(len(newDF["ID"])):
    mailingaddress = newDF.columns.get_loc("Mailing Address Street Address")
    if pd.isna(newDF.iloc[y, mailingaddress]):
        newDF.iloc[y, mailingaddress] = newDF.iloc[y, newDF.columns.get_loc("Primary Street Address")]
        newDF.iloc[y, newDF.columns.get_loc("Mailing Address City")] = newDF.iloc[y, newDF.columns.get_loc("Primary City")]
        newDF.iloc[y, newDF.columns.get_loc("Mailing Address State")] = newDF.iloc[y, newDF.columns.get_loc("Primary State")]
        newDF.iloc[y, newDF.columns.get_loc("Mailing Address Zip")] = newDF.iloc[y, newDF.columns.get_loc("Primary Zip")]
        newDF.drop(columns=["Primary Street Address", "Primary Secondary Address", "Primary State", "Primary City", "Primary Zip"])
newDF.to_csv("export.csv")
print("Done")