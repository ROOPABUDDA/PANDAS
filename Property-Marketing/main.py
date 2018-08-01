# version 0.0.0
# python 3.5
# author ROOPA BT 31/07/2018


import numpy as np
import pandas as pd
# from . import Dataset
pd.options.display.max_rows
pd.options.display.max_columns = 24
df = pd.read_csv("Dataset/Property/Properties.csv")
print(df)

def class_to_numeric(series):
    """[summary]:
    To convert characters to numeric

    [description]
    this function is used to convert the class values from characters to numeric values.

    Arguments:
        series {[type]} -- [description]
        a series of dataframe column 'class'

    Returns:
        number -- [description]
    """
    if series['class'] == 'Class A':
        return 0
    elif series['class'] =='Class B':
        return 1
    else:
        return 2


df['class'] = df.apply(class_to_numeric, axis='columns')
print(df['class'])
