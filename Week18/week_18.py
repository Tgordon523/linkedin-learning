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
    "Simple filter for multiple specific columns \n",
    df.loc[:, ["Math_3", "EngLit_2"]].head(),
)
