import pandas as pd 

def remove_missing_values(df, axis=0):
    """Remove rows or columns with missing values (NaNs)."""
    return df.dropna(axis=axis)

def remove_duplicates(df):
    """Remove duplicate rows from DataFrame."""
    return df.drop_duplicates(keep='first')
