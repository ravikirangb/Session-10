# -*- coding: utf-8 -*-
"""
@author: Ravikiran
"""

import pandas as pd

USBabyNames_df = pd.read_csv('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv')
print (USBabyNames_df.columns.values)


#1. Delete unnamed columns
USBabyNames_df.drop(USBabyNames_df.loc[:, USBabyNames_df.columns.str.contains('^Unnamed')], axis=1, inplace=True)
print (USBabyNames_df.columns.values)

#2. Show the distribution of male and female
print ("Male Female Distribution:: \n", USBabyNames_df.Gender.value_counts())

# Show the top 5 most preferred names

print ("top 5 most preferred names::\n", USBabyNames_df.groupby(['Name'])['Count'].sum().nlargest(5))


#4. What is the median name occurence in the dataset

print ("median name occurence in the dataset::- \n",USBabyNames_df[USBabyNames_df.Id == USBabyNames_df.median().Id]['Name'])


# 5. Distribution of male and female born count by states

print ("Distribution of male and female born count by states :: \n", USBabyNames_df.groupby(['State','Gender'])['Count'].sum())
