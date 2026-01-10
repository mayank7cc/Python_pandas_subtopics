import pandas as pd

# Data Cleaning = Prcoess of fixing/removing incomplete , irrelevant or incorrect data.
#                 Approx 75% of work done with Pandas in data cleaning

df = pd.read_csv("Pokedata.csv")

#1.Drop irrelevant columns

df= df.drop(columns = ["HP","Defense"])
print(df)

# 2.Handle missing Data
#df = df.dropna(subset = ["Speed"]) # This one when a row content doesnt have column value.(N/A) wala term in brocode type2.
#print(df)

#df = df.fillna({"Type 2" == "None"})
#print(df)

#3.Fixing Inconsistent values

df["Type"] = df["Type"].replace({"Flying":"FLYING"})
print(df)

# Standardize Text

df["Name"] = df["Name"].str.lower()
print(df)

#Fix data type
# Suppose HP column was loaded as string
df["HP"] = df["HP"].astype(int)
print(df)

#Removing Dublicate values
df = df.drop_duplicates()
