import pandas as pd
#print(pd.__version__)

# A series is pandas 1 Dimensional labbeled array that can hold any data type, like a single column in spread sheet.

data = [100,200,300,20,30]

series = pd.Series(data, index = ["a","b","c","d","e"]) # Here indexing with list and tuple gives the same order, but with sets it reverses the order.
print(series)

print(series.loc["b"])

series.loc["a"]= 1000
print(series)

print(series.iloc[2])

print(series[series<=100])


# same with dictionaries,but no need to add labels, keys acts as labels.

Dict = {"Harry":98,"Korosuke":88,"Inosuke":73}

series = pd.Series(Dict)
print(series)
print(series.loc["Inosuke"])

series.loc["Inosuke"]+= 100
print(series.loc["Inosuke"])
print(series[series<=90])

# homework Qs

Pokemons = ["Bulbasaur","Pikachu","Totodile"]

series = pd.Series(Pokemons, index = [1,2,3])
print(series)

