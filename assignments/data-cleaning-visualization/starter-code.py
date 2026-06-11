import pandas as pd
import matplotlib.pyplot as plt

DATA_PATH = "data.csv"


def load_dataset(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def clean_dataset(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["city"] = df["city"].str.title().str.strip()
    df["category"] = df["category"].str.title().str.strip()
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df["sales"] = pd.to_numeric(df["sales"], errors="coerce")
    df["sales"] = df["sales"].fillna(df["sales"].mean())
    return df


def create_plots(df: pd.DataFrame) -> None:
    plt.figure(figsize=(8, 4))
    df.groupby("city")["sales"].sum().plot(kind="bar")
    plt.title("Total Sales by City")
    plt.ylabel("Sales")
    plt.tight_layout()
    plt.savefig("sales_by_city.png")

    plt.figure(figsize=(8, 4))
    df.plot(x="date", y="sales", kind="line", marker="o")
    plt.title("Sales Over Time")
    plt.ylabel("Sales")
    plt.tight_layout()
    plt.savefig("sales_over_time.png")


def summarize_insights(df: pd.DataFrame) -> None:
    print("Summary statistics:")
    print(df[["price", "sales"]].describe())
    print("\nCleaned data preview:")
    print(df.head())


if __name__ == "__main__":
    df = load_dataset(DATA_PATH)
    df_clean = clean_dataset(df)
    create_plots(df_clean)
    summarize_insights(df_clean)
