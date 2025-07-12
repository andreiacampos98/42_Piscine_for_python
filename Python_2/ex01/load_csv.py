import pandas as pd


def load(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    print(f'Loading dataset of dimentsions {df.shape}')
    return df
