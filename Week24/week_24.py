from numpy.core.fromnumeric import size
import matplotlib.pyplot as plt
import seaborn
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder

### Create dataset
df = pd.DataFrame(
    np.random.normal(7.5, 2, size=(100, 6)),
    columns=["Math 1", "Math 2", "Math 3", "EngLit 1", "EngLit 2", "EngLit 3"],
)

teachers = np.random.choice(["Karen", "Dwight", "Doug"], size=100)
df["Teachers"] = teachers

print(f"Original dataframe names {df.columns.values} \n")


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

df_ohe = pd.get_dummies(df_clean_long, columns=["teachers"], drop_first=False)
# print(df_ohe)

features = ["year", "math", "englit", "teachers_Dwight", "teachers_Karen"]
features1 = [
    "year",
    "math",
    "englit",
    "teachers_Dwight",
    "teachers_Karen",
    "teachers_Doug",
]

# df_ohe["target"] = np.where((df_ohe["math"] >= 7) & (df_ohe["englit"] >= 7), 1, 0)
df_ohe["target"] = (df_ohe["math"] + df_ohe["englit"]) / 2


print(df_ohe[features1 + ["target"]].corr().multiply(100).round(4))
