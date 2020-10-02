import pandas as pd
from pandas import DataFrame, read_csv
import os
import math
import numpy as np

pd.options.mode.chained_assignment = None

master_list = pd.read_csv("MASTER LIST.csv", skipinitialspace=True, dtype=str)
df2 = pd.DataFrame({"Mailing Address Street Address": ["hello test", np.nan, np.nan, "another test"], 'Home Address Street Address': ['test', 'test2', 'test3', 'test4']})

master_home = list(master_list['Home Address Street Address'])
def address_fill(df):

    df["Mailing Address Street Address"] = df["Mailing Address Street Address"].fillna(df["Home Address Street Address"])
    df["Mailing Address City"] = df["Mailing Address City"].fillna(df["Home Address City"])
    df["Mailing Address State"] = df["Mailing Address State"].fillna(df["Home Address State"])
    df["Mailing Address Zip"] = df["Mailing Address Zip"].fillna(df["Home Address Zip"])

    del df['Home Address Street Address']
    del df['Home Address Secondary Address']
    del df['Home Address City']
    del df['Home Address State']
    del df['Home Address Zip']
    del df['Mailing Address Secondary Address']

    return df
master_list = address_fill(master_list)

master_list.to_csv('lexisFormat_export.csv')

with open('old_addresses.txt', 'w') as filehandle:
    for l in master_home:
        filehandle.writelines("%s\n" % l)



    


        
