import pandas as pd
import numpy as np
from pathlib import Path


### regex pattern to extract the currency and amount from unstructured text
df = pd.DataFrame(
    np.random.normal(7.5, 2, size=(100, 6)),
    columns=["Math_1", "Math_2", "Math_3", "EngLit_1", "EngLit_2", "EngLit_3"],
)


print(df)

print(df.loc[:, "Math_3":"EngLit_2"].head())

math_mask = df.columns[df.columns.str.startswith("Math")]
print(df[math_mask])

numeric_mask = df.columns[df.columns.str.contains("1")]
print(df[numeric_mask])

print("Subsetting the dataframe by text (a symbol)")
# print(df_subset, "\n")


print("Subsetting the dataframe by matching text anywhere in field")
# df_subset2 = df_extract2[df_extract2["Username"].str.contains("gord")]
# print(df_subset2)