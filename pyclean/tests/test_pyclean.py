import pandas as pd
import pytest
import sys
sys.path.append('src')
from pyclean import pyclean

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

# Run tests
if __name__ == "__main__":
    pytest.main()