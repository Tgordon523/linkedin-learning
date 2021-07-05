import pandas as pd 
import numpy as np
from pathlib import Path

df = pd.read_excel(Path.cwd()/'test.xlsx', engine="openpyxl")

print(df.line.tail())
### regex pattern to extract the website details from unstructured text
pat = r'(?P<Username>[a-z0-9_\.-]+)@(?P<website>[\da-z\.-]+)\.(?P<domain>[a-z\.]{2,6})'
### extract from the text and separate
df_extract = df.line.str.extract(pat)

print(df_extract.info())
### showcase results
print(df_extract)