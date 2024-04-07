import pandas as pd 

def remove_missing_values(df, axis=0):
    """Remove rows or columns with missing values (NaNs)."""
    return df.dropna(axis=axis)

def remove_duplicates(df):
    """Remove duplicate rows from DataFrame."""
    return df.drop_duplicates(keep='first')

def compare_data(raw_data, processed_data):
    """Compare DataFrame function"""

    # Compare number of missing values
    raw_missing_values = raw_data.isnull().sum()
    processed_missing_values = processed_data.isnull().sum()
    missing_values_diff = processed_missing_values - raw_missing_values
    
    # Compare number of unique values
    raw_unique_values = raw_data.nunique()
    processed_unique_values = processed_data.nunique()
    unique_values_diff = processed_unique_values - raw_unique_values
    
    # Combine results into a dictionary
    comparison_results = {
        'missing_values': missing_values_diff,
        'unique_values': unique_values_diff

    }
    
    return comparison_results