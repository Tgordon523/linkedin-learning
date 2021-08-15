import pandas as pd
import numpy as np


### Create dataset
df = pd.DataFrame(
    np.random.normal(7.5, 2, size=(100, 6)),
    columns=["Math 1", "Math 2", "Math 3", "EngLit 1", "EngLit 2", "EngLit 3"],
)

print(df)

[print(i) for i in df.columns]


def clean_names(df: pd.DataFrame):
    """ Function to clean column names similar to the clean_names function from the janitory package in R. """
    df.columns = df.columns.str.lower()
    df.columns = df.columns.str.replace(" ", "_")
    return df


for col in df.columns:
    for t in col:
        print("".join(t.lower()))
