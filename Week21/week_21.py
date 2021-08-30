import pandas as pd
import numpy as np


### Create dataset
df = pd.DataFrame(
    np.random.normal(7.5, 2, size=(100, 6)),
    columns=["Math 1", "Math 2", "Math 3", "EngLit 1", "EngLit 2", "EngLit 3"],
)

print(f"Original dataframe names {df.columns.values} \n")


def clean_names(df: pd.DataFrame) -> pd.DataFrame:
    """ Function to clean column names and convert it into simple snakecase format. """
    df.columns = df.columns.str.lower()
    df.columns = df.columns.str.strip()
    df.columns = df.columns.str.replace(" ", "_")
    return df


print(clean_names(df))
