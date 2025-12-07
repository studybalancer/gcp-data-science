"""
Pandas :

This is the library -- provides flexible data structure and data analysis.
pandas,numpy,seaborn,matplotlib.
1d - Series - 1d dimensional array
2d - 2 dimensional labeled data
https://pypi.org/project/pandas/
pip install pandas -- To install pandas librrary
1 2
3 4
5 6

 wed,thu,friday --- >




 pandas is like an excel for python

 it helps you

 1. Read data
 2. cleand data
 3. Fix mistakes in data
 4. Calculate things
 5. Summarize information
 6.make your data organized

 But instead of clicking with a mouse , you use code .


two main building blocks of pandas

1. Series = one column


think of series
1. one column from excel
2. A list of numbers,names or anything
3. Each value has a label row number

DataFrame  = whole Table
1. A complete exce sheet
2. made of many columns (many series.)
3. With rows and columns.


what pandas can do ?

1. Read files -- csv,text,csv in to python
 pd.read_csv("data.csv")


2. Clean messy data
    . Remove empty rows
    . Fix Wrong values
    . Fill missing data.

3. Change data
 . Rename columns
 . Add new column
 . Remove column

4. Analyze data.
    . count things
    . FInd averages
    . Group
    .Filter data

Writes back to csv


Pandas helps yous:
clean
fix
understand
use it for decison making or machine learning.


seaborn -- data visualization -- built on top of matplotlib.



"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("city.csv",index_col=False)

print(df)


total_customers = len(df)
print(total_customers)

average_age = df["age"].mean()
print(average_age)

print(df['purchaseamount'].sum())

print(df.groupby('gender')['purchaseamount'].sum())

print(df['city'].value_counts())

print(df[df['purchaseamount'] > 300])

print(df[df['gender'] == "female"])


print(df[df['age'] < 30])


print("---------------------")

df['Discount'] = df['purchaseamount'] * 0.1

print(df)

df["netAmount"] = df['purchaseamount'] - df ['Discount']

df.to_csv("city_new.csv", index=False)

print(df)


df = sns.load_dataset("titanic")

print(df)

df.to_csv("titanic_data.csv", index=False)








