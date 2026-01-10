import pandas as pd

df = pd.read_csv("Pokedata.csv")

#Filtering = Keeping the rows that match a condition.

Flare_Pokemon = df[(df["Type"] == "Fire")&(df["Speed"]>=100)]
print(Flare_Pokemon)

