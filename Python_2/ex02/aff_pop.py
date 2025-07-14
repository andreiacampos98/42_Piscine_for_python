import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load


def pop(df: pd.DataFrame) -> pd.DataFrame:
    countries = ['Portugal', 'France']
    df_graph = df[df['country'].isin(countries)]
    df_graph = df_graph.set_index('country')
    print(df_graph.info())
    df_graph = df_graph.T
    df_graph.index = df_graph.index.astype(int)
    for country in countries:
        df_graph[country] = df_graph[country].apply(
            lambda x: (
                float(x[:-1]) * 1_000_000
                if isinstance(x, str) and x.endswith('M')
                else float(x)
            )
        )
    df_graph = df_graph / 1000000
    print(df_graph.columns)
    print(df_graph.head())
    return df_graph


def data_visualization(df: pd.DataFrame):
    df.plot(figsize=(10, 6))
    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population (millions)")
    plt.xticks(range(1800, 2101, 40), rotation=45)
    plt.savefig("pop.jpeg")
    return


def main():
    df = load("Python_2/population_total.csv")
    df_visualization = pop(df)
    data_visualization(df_visualization)


if __name__ == "__main__":
    main()
