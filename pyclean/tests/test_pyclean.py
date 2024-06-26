import pandas as pd
import numpy as np
import pytest
import sys
sys.path.append('src/pyclean')
from pyclean import pyclean
from pyclean import compare

# Test remove_missing_values function
def test_remove_missing_values():
    # Create a DataFrame with missing values
    df = pd.DataFrame({
        'A': [1, 2, None, 4],
        'B': [5, None, 7, 8]
    })

    # Remove missing values
    cleaned_df = pyclean.remove_missing_values(df)

    # Check if missing values are removed
    assert cleaned_df.isnull().sum().sum() == 0

# Test remove_duplicates function
def test_remove_duplicates():
    # Create a DataFrame with duplicate rows
    df = pd.DataFrame({
        'A': [1, 2, 3, 2, 4],
        'B': ['a', 'b', 'c', 'b', 'd']
    })

    # Remove duplicate rows
    cleaned_df = pyclean.remove_duplicates(df)

    # Check if duplicate rows are removed
    assert len(cleaned_df) == len(df.drop_duplicates())

def generate_random_dataframe(num_rows, num_columns):
    # Create a random DataFrame
    data = {f'Column_{i}': np.random.randint(0, 100, size=num_rows) for i in range(num_columns)}
    return pd.DataFrame(data)

def test_compare_data():
    # Generate random raw and processed dataframes for testing
    num_rows = 100
    raw_data = generate_random_dataframe(num_rows, 5)  
    processed_data = generate_random_dataframe(num_rows, 5)  
    
    # Compare DataFrame
    comparison_results = compare.compare_data(raw_data, processed_data)
    
    # Check if missing values comparison is correct
    for column in raw_data.columns:
        assert comparison_results['missing_values'][column] == processed_data[column].isnull().sum() - raw_data[column].isnull().sum()
    
    # Check if unique values comparison is correct
    for column in raw_data.columns:
        assert comparison_results['unique_values'][column] == processed_data[column].nunique() - raw_data[column].nunique()

# Run tests
if __name__ == "__main__":
    pytest.main()