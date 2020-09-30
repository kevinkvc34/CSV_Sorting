import pandas as pd
from pandas import DataFrame, read_csv
import os
import math

df = read_csv("final_csv copy.csv", skipinitialspace=True)

for x in range(len(df["ID"])):
    print("{} {}".format(df["SSN"][x], df["Name"][x]))