import pandas as pd 

def remove_missing_values(df, axis=0):
    """
    Remove rows or columns with missing values (NaNs).

    Parameters:
    - df: DataFrame
        Input DataFrame.
    - axis: {0 or 'index', 1 or 'columns'}, default 0
        Axis along which to drop rows or columns.

    Returns:
    - DataFrame
        DataFrame with missing values removed.
    """
    return df.dropna(axis=axis)