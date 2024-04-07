import pandas as pd 

def remove_missing_values(df, axis=0):
    """Remove rows or columns with missing values (NaNs).

    Parameters
    ----------
    df : Input DataFrame.
    axis : Axis along which to drop rows or columns. Default is 0 for rows.

    Returns:
    df : DataFrame with missing values removed.
    """
    return df.dropna(axis=axis)

def remove_duplicates(df):
    """Remove duplicate rows from DataFrame.
    
    Parameters
    ----------
    df : Input DataFrame.

    Returns:
    --------
    df : DataFrame with duplicate rows removed.
    """
    return df.drop_duplicates(keep='first')