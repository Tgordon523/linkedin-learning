import pandas as pd
import numpy as np


### Create dataset
df = pd.DataFrame(
    np.random.normal(7.5, 2, size=(100, 6)),
    columns=["Math_1", "Math_2", "Math_3", "EngLit_1", "EngLit_2", "EngLit_3"],
)

### Simple between filter
print(
    "Simple Filter everything between \n",
    df.loc[:, "Math_3":"EngLit_2"].head(),
)

### Simple filter for specific columns
print(
    "Simple Filter everything between \n",
    df.loc[:, ["Math_3", "EngLit_2"]].head(),
)


### Column starts with filter
math_mask = df.columns[df.columns.str.startswith("Math")]
print(
    "Filter to only include columns starting with Math \n",
    df[math_mask].head(),
)

### Column name has the number 1 included.
numeric_mask = df.columns[df.columns.str.contains("1")]
print(
    "Filter to only include columns with numeric or specific word in title \n",
    df[numeric_mask].head(),
)
