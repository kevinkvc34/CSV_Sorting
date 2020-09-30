import pandas as pd
from pandas import DataFrame, read_csv
import os
import math

shortdf = pd.read_csv(os.path.expanduser("exported_numbers_pandas2.csv"), encoding="utf-8-sig", quotechar='"',skipinitialspace=True)
fulldf = pd.read_csv(os.path.expanduser("Alan Export For Nexis.csv"), skipinitialspace=True)
newdf = pd.read_csv("NewFinalCsv.csv")

print(shortdf)



for i in range(len(shortdf["Column2"])):
    # print("in first loop")
    print(i)
    for x in range(len(fulldf["ID"])):
        print(x)
        # print("second loop")
        # try:
        #     print(shortdf["Column1"][0])
        # except:
        #     print("didnt work")
        if fulldf["ID"][x] == shortdf["Column1"][i]:
            # print("if statement")
            # print(fulldf["ID"][x])
            newRecord = {'ID': shortdf["Column1"][i], 'Name': shortdf["Column2"][i], 'Home Address': '{}, {}, {} {}'.format(fulldf["Home Address Street Address"][x], fulldf["Home Address City"][x], fulldf["Home Address State"][x], fulldf["Home Address Zip"][x]), 'Phone Number': '', 'Birthday': fulldf["Date Of Birth"][x], 'SSN': fulldf["Tax ID"][x]}
            newdf = newdf.append(newRecord, ignore_index=True)
            print(newdf)
            break

newdf.to_csv("newdf_export.csv")

