import pandas as pd

#CSV = comma seperated values
#Json = Javascript Object Notation

df = pd.read_csv("Pokedata.csv")
print(df.to_string()) #.to_string()for printing entire datafile

df = pd.read_json("pokemon_dataset.json")
print(df)
