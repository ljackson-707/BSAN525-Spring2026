# You can load an entire CSV file into 
# a pandas dataframe as follows
import pandas as pd

frame = pd.read_csv("breadprices.csv")
print(frame)

# There are a couple ways to clean a data set
# with null (NaN) values

# 1. Delete the row containing them
# frame.dropna(inplace = True)    # inplace - change original DataFrame
# print(frame)

# 2. Replace each null value with a single filler value
# e.g., the mean of existing values in its row
frame.drop(columns = "Year", inplace = True) 
# Drop the year column so it doesn't go into calculating mean
newValue = frame.loc[10].mean()
# Grabs row 11, because it is zero-based, gets the mean of the values in the row
frame.fillna(newValue, inplace = True)
print(frame)


