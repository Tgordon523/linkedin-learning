import pandas as pd
import numpy as np


### Create dataset
df1 = pd.DataFrame(
    np.random.normal(7.5, 2, size=(100, 6)),
    columns=["Math_1", "Math_2", "Math_3", "EngLit_1", "EngLit_2", "EngLit_3"],
)

### Create different ordering
df2 = df1.copy(deep=True)
df2 = df2.sort_index(axis=1)
print(
    f" Original column order {df1.columns.values} \n",
    f" Adjustred column order {df2.columns.values} \n",
    "-------" * 10,
)

df3 = df2.reindex_like(df1)

print("Reindexed back to original order \n", df3.columns.values)
