import pandas as pd


def load(path: str) -> pd.DataFrame:
    """The function loads the csv file."""
    try:
        df = pd.read_csv(path)
        print(f"Loading {path} dataset of dimensions {df.shape}")
        return df
    except (FileNotFoundError, pd.errors.EmptyDataError, pd.errors.ParserError,
            OSError) as e:
        print(f"Error loading file: {e}")
        return None
