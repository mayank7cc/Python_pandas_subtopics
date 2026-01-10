'''
Aggregation = Reduce a set of values into a single summary value
              Used to summarize and analyze data
              Often used with the group by function.
'''
import pandas as pd

df = pd.read_csv("Pokedata.csv")
#Applys to whole dataframe
#print(df.mean(numeric_only = True))
#print(df.sum(numeric_only = True))
#print(df.min(numeric_only = True))
#print(df.max(numeric_only = True))
#print(df.count())

#Single column

#print(df["Speed"].mean())           #same with all
#print(df.sum(numeric_only = True))
#print(df.min(numeric_only = True))
#print(df.max(numeric_only = True))
#print(df.count())

group = df.groupby("Type")
print(group["Speed"].max())
#Same all with sum,max,min

