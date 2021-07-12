import pandas as pd
import numpy as np
from pathlib import Path

print(Path.cwd())
df = pd.read_excel(
    Path(r"C:\Users\tgord\Documents\Linkedin\linkedin-learning\Week17") / "test.xlsx",
    engine="openpyxl",
)
df2 = pd.read_excel(
    Path(r"C:\Users\tgord\Documents\Linkedin\linkedin-learning\Week16") / "test.xlsx",
    engine="openpyxl",
)

### regex pattern to extract the currency and amount from unstructured text
pat = r"(?P<Currency>[($|£|¥|€)])(?P<Amount>\d+[.]\d+|\d+ )"
### extract from the text and separate
df_extract = df.line.str.extract(pat)

### regex pattern to extract the website details from unstructured text
pat = r"(?P<Username>[a-z0-9_\.-]+)@(?P<website>[\da-z\.-]+)\.(?P<domain>[a-z\.]{2,6})"
### extract from the text and separate
df_extract2 = df2.line.str.extract(pat)


df_subset = df_extract[df_extract.Currency == "£"]
print("Subsetting the dataframe by text (a symbol)")
print(df_subset, "\n")


print("Subsetting the dataframe by matching text anywhere in field")
df_subset2 = df_extract2[df_extract2["Username"].str.contains("gord")]
print(df_subset2)