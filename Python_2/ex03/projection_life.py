import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load


def treat_data_income(df: pd.DataFrame) -> pd.DataFrame:
    """
        Treat the data of dataset df_income.
    """
    df.set_index('country', inplace=True)
    for col in df.columns:
        df[col] = df[col].apply(
            lambda x: (
                float(x[:-1]) * 1000
                if isinstance(x, str) and x.endswith('k')
                else float(x)
            )
        )
    df_graph = df['1900']
    df_graph.name = 'gross_domestic_product'
    return df_graph


def treat_data_life(df: pd.DataFrame) -> pd.DataFrame:
    """
        Treat the data of dataset df_life.
    """
    df.set_index('country', inplace=True)
    df_graph = df['1900']
    df_graph.name = 'life_expectancy'
    return df_graph


def display_graph(df: pd.DataFrame):
    """
        Take the data and display in a graph
    """
    plt.figure(figsize=(10, 6))
    plt.scatter(x=df['gross_domestic_product'], y=df['life_expectancy'])
    plt.title("1900")
    plt.ylabel("Life Expectancy")
    plt.xlabel("Gross domestic product")
    plt.savefig("scatter_plot.jpeg")
    return


def main():
    """
        A program that displays the projection of life expectancy in relation
        to the gross national product of the year 1900 for each country.
    """
    df_income = load(
        "Python_2/income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    df_life = load(
        "Python_2/life_expectancy_years.csv")
    df_graph_income = treat_data_income(df_income)
    df_graph_life = treat_data_life(df_life)
    df_final = pd.concat([df_graph_income, df_graph_life], axis=1)
    df_final.columns = ['gross_domestic_product', 'life_expectancy']
    display_graph(df_final)


if __name__ == "__main__":
    main()
