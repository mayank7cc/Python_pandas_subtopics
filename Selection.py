import pandas as pd

df = pd.read_csv("Pokedata.csv",index_col = "Name")

#SELECTION BY COLUMN

#print(df["Name"])
#print(df[["Name","Type","Speed"]]) # here double list to select multiple columns

#SELECTION BY ROWS

#print(df)
#print(df.loc["Slowking"])

# for Index to be names we can do the (df = pd.read_csv("Pokedata.csv",index_col="Name"))

#print(df.loc["Charizard":"Blastoise",["Attack","Type"]])
#If I don't want every bit of detail info of a name
#then and also a range between rows.
          
#print(df.iloc[0:11:3,0:3])  #We can edit to see specific columns as well


Pokemon = input("Enter your Pokemon Name:")

try:
    print(df.loc[Pokemon])
          
except KeyError:
    print(f"{Pokemon} not found")
