import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load


def pop(df: pd.DataFrame) -> pd.DataFrame:
    """
        Treat the data of dataset.
    """
    countries = ['Portugal', 'France']
    df_graph = df[df['country'].isin(countries)]
    df_graph = df_graph.set_index('country')

    df_graph = df_graph.T
    df_graph.index = df_graph.index.astype(int)
    df_graph = df_graph[(df_graph.index >= 1800) & (df_graph.index <= 2050)]
    for country in countries:
        df_graph[country] = df_graph[country].apply(
            lambda x: (
                float(x[:-1]) * 1_000_000
                if isinstance(x, str) and x.endswith('M')
                else float(x)
            )
        )
    df_graph = df_graph / 1000000
    return df_graph


def data_visualization(df: pd.DataFrame):
    """
        Take the data and display in a graph
    """
    df.plot(figsize=(10, 6))
    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population (millions)")
    plt.xticks(range(1800, 2051, 40), rotation=45)
    plt.savefig("pop.jpeg")
    return


def main():
    """
        A program that loads the file population_total.csv,
        and displays the country information of your campus
        versus other country.
    """
    df = load("Python_2/population_total.csv")
    if df is not None:
        df_visualization = pop(df)
        data_visualization(df_visualization)
    else:
        print("Dataset not loaded. Exiting.")


if __name__ == "__main__":
    main()
