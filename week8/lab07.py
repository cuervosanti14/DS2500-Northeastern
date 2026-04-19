# LAB EXERCISE 07
import pandas as pd
from math import sqrt

# Converts dictionary into a dataframe pandas can read (table)
df = pd.DataFrame({
    'A': [1,2,3,4,5],
    'B': [4, None, None, None, None],
    'C': ["High", "Medium", "Medium", "High", "Low"]
})

# Problem 1
def compute_zscore(lst):
    """
    Compute z-score for a list of numbers

    Parameters: list of numbers
    Returns: list of z-scores for numbers
    NOTE: use sample standard deviation (hence variance)
    """
    # Variable Calculations
    mean = sum(lst) / len(lst)
    variance = sum([(x - mean) ** 2 for x in lst]) / (len(lst) - 1)
    stddev = sqrt(variance)

    # Z-Score Calculation
    return [(x - mean) / stddev for x in lst]

# Problem 2
def compute_mms(lst):
    """
    Compute min-max scaling for a list of numbers
    Scaling the data to a range between 0 and 1

    Parameters: list of numbers
    Returns: list of min-max scaling for numbers
    """
    # Get min & max of list
    x_min = min(lst)
    x_max = max(lst)

    # Min-Max Scaling Calculation
    return [(x - x_min) / (x_max - x_min) for x in lst]

# Problem 3
# Part 1
def remove_cols_with_missing(df):
    """
    Takes a pandas dataframe object
    Returns new dataframe after removing columns containing missing values

    Parameters: pandas dataframe object
    Returns: new dataframe with empty columns removed
    """
    # Scans along axis=1 (columns) & drops any columns that contain
    # at least one empty cell
    return df.dropna(axis=1)

# Part 2
def remove_rows_with_missing(df):
    """
    Takes a pandas dataframe object
    Returns a new dataframe after removing rows containing missing values

    Parameters: pandas dataframe object
    Returns: new dataframe with empty rows removed
    """
    # Scans along axis=0 (rows) & drops any rows that contain
    # at least one empty cell
    return df.dropna(axis=0)

def main():
    print("Original DataFrame:")
    print(df)

    # Testing Problem 1
    print("\nZ-Score of column A:")
    print(compute_zscore(df['A']))

    # Testing Problem 2
    print("\nMin-Max Scaling of column A:")
    print(compute_mms(df['A']))

    # Problem 3
    # Testing Part 1
    print("\nRemove COLUMNS with missing values:")
    print(remove_cols_with_missing(df))
    # Testing Part 2
    print("\nRemove ROWS with missing values")
    print(remove_rows_with_missing(df))

if __name__ == '__main__':
    main()