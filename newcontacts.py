import pandas as pd
from pandas import DataFrame, read_csv
import os
import math

full = pd.read_csv("new full walter list.csv", nrows=100, skipinitialspace=True)
df2 = pd.read_csv("Alan Export For Nexis(1) (1).csv", skipinitialspace=True)
completedf = pd.read_csv("newdf_export.csv", skipinitialspace=True)

fulllist = list(full["ID"])
new = list(df2["ID"])
i = 1

def findContact(df):
    for x in range(len(new)):
        if new[x] in fulllist:
            i = fulllist.index(new[x])
            new_record = {'ID': new[x], 'Name': 'N/A', 'Home Address': '{}, {}, {} {}'.format(full["Home Address Street Address"][i], full["Home Address City"][i], full["Home Address State"][i], full["Home Address Zip"][i]), 'Phone Number': '', 'Birthday': full["Date Of Birth"][i], 'SSN': full["Tax ID"][i]}
            df = df.append(new_record, ignore_index=True)
            print(new_record)

    return df
completedf = findContact(completedf)
completedf.to_csv('final_csv.csv')