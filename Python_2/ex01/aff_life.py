import matplotlib.pyplot as plt
from load_csv import load
import pandas as pd


def display_graph(df: pd.DataFrame):
    """Take the data and display in a graph"""
    portugal = df[df['country'] == 'Portugal']
    portugal_data = portugal.drop(columns=['country'])
    portugal_data = portugal_data.T.squeeze()
    portugal_data.index = portugal_data.index.astype(int)
    plt.figure(figsize=(10, 6))
    plt.plot(portugal_data.index, portugal_data.values, color='blue')
    plt.title("Portugal Life expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.xticks(range(1800, 2101, 50), rotation=45)
    plt.savefig("graph.jpg")


def main():
    """
        A program that loads the file life_expectancy_years.csv,
        and displays the country information of your campus.
    """
    df = load("Python_2/life_expectancy_years.csv")
    display_graph(df)


if __name__ == "__main__":
    main()
