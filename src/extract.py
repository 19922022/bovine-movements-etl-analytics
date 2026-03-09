import os
import pandas as pd


def load_csv(filename: str) -> pd.DataFrame:
    """Load a CSV from the data/raw directory.

    Parameters
    ----------
    filename : str
        Name of the CSV file (relative to data/raw).

    Returns
    -------
    pd.DataFrame
        Loaded dataframe.

    Raises
    ------
    FileNotFoundError
        If the file does not exist in data/raw.
    """
    # build path
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    raw_dir = os.path.join(base_dir, "data", "raw")
    file_path = os.path.join(raw_dir, filename)

    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"CSV file not found: {file_path}")

    df = pd.read_csv(file_path, encoding="latin-1")
    print(f"Loaded {filename} with shape {df.shape}")
    return df
