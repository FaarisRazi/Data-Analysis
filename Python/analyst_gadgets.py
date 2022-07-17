# Handy analytical functions to be added for re-usbility in projects
import pandas as pd


# Setting the header (column-names) by a specific row
def row_header(df, row=0, start=0):
  # row = int   -> number/index of the row to be made a header
  # start = int -> number/index of row from when the dataframe should "start"
  
  df.columns = df.iloc[row]
  
  if not start:
    start += 1
    
  df = df[start:]
  df.drop([0], inplace = True)
  df.reset_index(inplace = True)
  
  return df
