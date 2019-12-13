import pandas as pd
import matplotlib.pyplot as plt

serie1 = pd.Series([1,2,3])
serie2 = pd.Series([4,5,6])

df = pd.DataFrame()
df["col_serie1"] = serie1
df["col_serie2"] = serie2
df["times"] = df["col_serie1"] * df["col_serie2"]
print(df)

nuevo_renglon = pd.Series({"col_serie1": 4, "col_serie2": 7})
df = df.append(nuevo_renglon, ignore_index=True)
print(df)

df = df.drop(3)
print(df)

df = df.transpose()
print(df)


df = pd.DataFrame([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20]], ["ren1", "ren2", "ren3", "ren4", "ren5"], ["col1", "col2", "col3", "col4"])
print(df)
print(df.columns)
print(df.index)
print(df.shape)
print(df.info())
print(df.describe())
print(df.describe()[["col1", "col2"]])

df.boxplot()
df.hist()


df = df.sort_values(by = "col3", ascending=True)
print(df)
df = df.sort_values(by = ["col3", "col1"], ascending=[False, True])
print(df)

print(df[df["col1"] > 5])
print(df[(df["col1"] > 5) & (df["col3"] > 12)])
print(df[(df["col1"] > 5) | (df["col3"] > 12)])

print(df.iloc[[0,2], [0,3]])
print(df.loc[["ren1", "ren3"], ["col1", "col4"]])

print(df[1:3])
print(df[:3])
print(df[2:])

df.loc["ren2", "col1"] = 1000
print(df)

df.loc[["ren2", "ren5"], "col1"] = 1000
print(df)

