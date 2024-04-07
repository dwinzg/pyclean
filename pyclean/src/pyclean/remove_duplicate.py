import pandas as pd

def remove_duplicates(df):
    """
    Remove duplicate rows from DataFrame.

    Parameters:
    - df: DataFrame
        Input DataFrame.
    Returns:
    - DataFrame
        DataFrame with duplicate rows removed.
    """
    return df.drop_duplicates(keep='first')