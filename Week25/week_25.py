from numpy.core.fromnumeric import size
import pandas as pd
import numpy as np
from pandas.core import series
from sklearn.preprocessing import OneHotEncoder

### Create dataset
df = pd.DataFrame(
    np.random.normal(7.5, 2, size=(100, 6)),
    columns=["Math 1", "Math 2", "Math 3", "EngLit 1", "EngLit 2", "EngLit 3"],
)

teachers = np.random.choice(["Karen", "Dwight", "Doug"], size=100)
df["Teachers"] = teachers


def clean_names(df: pd.DataFrame) -> pd.DataFrame:
    """ Function to clean column names and convert it into simple snakecase format. """
    df.columns = df.columns.str.lower()
    df.columns = df.columns.str.replace(" ", "_")
    return df


# print(clean_names(df.head()))
df_clean = clean_names(df)
df_clean["id"] = df_clean.index
# print(df1)

df_clean_long = pd.wide_to_long(
    df_clean, stubnames=["math", "englit"], sep="_", i=["id"], j="year"
).reset_index(drop=False)

df_ohe = pd.get_dummies(df_clean_long, columns=["teachers"], drop_first=True)
# print(df_ohe)


features = ["year", "math", "englit", "teachers_Dwight", "teachers_Karen"]

# df_ohe["target"] = np.where((df_ohe["math"] >= 7) & (df_ohe["englit"] >= 7), 1, 0)
df_ohe["target"] = (df_ohe["math"] + df_ohe["englit"]) / 2


def extract_correlated_features(df: pd.DataFrame) -> pd.Series:
    """ Function to clean column names and convert it into simple snakecase format. """
    correlated_features = []
    if np.abs(df.target) >= 0.6:
        correlated_features.append(df["target"])
    return pd.Series(correlated_features)  # [~features.isna()]


# print(df_ohe[features + ["target"]].corr().multiply(100).round(4))
df_corr = df_ohe[features + ["target"]].corr()
# print(df_ohe[features + ["target"]])
# print(df_corr)
series_a = df_corr.apply(extract_correlated_features, 1).reset_index()

print(series_a[(~series_a[0].isnull()) & (series_a["index"] != "target")])
# print(df_corr.apply(extract_correlated_features, 1))