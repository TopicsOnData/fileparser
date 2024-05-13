# Command line arguments
import sys

# Data structures
import pandas as pd
from pandas import Series, DataFrame

# Catching the file name
csvfile = sys.argv[0]

# Reading the file
obj = pd.read_csv('csvfile')

# Removing unnecessary columns
obj = obj.drop(columns='Unnamed: 0')

# Breaking up names column into first and rest of the name
names_delimited = obj['Name'].str.split(n=1, expand=True)

# Inserting a new column for Last Names
obj.insert(1, column='Last Name', value='')

# Overwriting the columns with new information
obj['Name'] = names_delimited[0]
obj['Last Name'] = names_delimited[1]

# Add '+1' to every entry in Phone Number
obj['Phone Number'] = '+1' + obj['Phone Number']

# Export to .csv
obj.to_csv('sys.argv[1]')
