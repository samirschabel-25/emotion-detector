import pandas as pd

df = pd.read_csv("C:\\Users\\samir\\Desktop\\Programme_Samir\\emotion-detector\\data\\emotions.csv")

print(df.head())
print()
print("Anzahl Datensätze:", len(df))
print()
print(df["emotion"].value_counts())