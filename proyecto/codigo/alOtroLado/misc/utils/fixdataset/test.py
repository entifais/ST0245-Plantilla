import pandas as pd
p=pd.read_csv("new.csv",on_bad_lines='skip',sep=";")
print(p)

print(p.index[25303])