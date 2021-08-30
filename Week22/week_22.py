from numpy.core.fromnumeric import size
import pandas as pd
import numpy as np


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


print(clean_names(df))
df1 = clean_names(df)
df1["id"] = df1.index
# print(df1)

df2 = pd.wide_to_long(df1, stubnames=["math", "englit"], sep="_", i=["id"], j="year")
print(df2)
