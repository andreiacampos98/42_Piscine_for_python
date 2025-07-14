import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load


def treat_data_income(df: pd.DataFrame):
    df.set_index('country', inplace=True)
    df = df.T
    for col in df.columns:
        df[col] = df[col].apply(
            lambda x: (
                float(x[:-1]) * 1000
                if isinstance(x, str) and x.endswith('k')
                else float(x)
            )
        )
    print(df.head())
    print(df.info())
    return


def main():
    df_income = load(
        "Python_2/income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    df_life = load(
        "Python_2/life_expectancy_years.csv")
    print(df_income.columns)
    print(df_income.info())
    print(df_income.head())
    treat_data_income(df_income)
    print(df_life.columns)
    print(df_life.info())
    print(df_life.head())


if __name__ == "__main__":
    main()
