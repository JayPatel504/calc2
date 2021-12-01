import pandas as pd

df = pd.read_csv("division2-result.csv")
for c in df['result']:
    print(type(c))