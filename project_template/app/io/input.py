import pandas as pd
def read_con() -> str:
    """
    reads text input from the console.
    returns:
        str: users text, string.
    """
    return input("enter text: ")
def read_file(file_path: str) -> str:
    """
    reads a text file.
    args:
        file_path (str): file path.
    returns:
        str: file content, string.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()
def read_pandas(file_path: str) -> pd.DataFrame:
    """
    reads a file using pandas.
    args:
        file_path (str): file pathPath to the file (csv or txt).
    returns:
        pd.DataFrame: data from the file, DataFrame.
    """
    return pd.read_csv(file_path)