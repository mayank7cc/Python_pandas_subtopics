import pandas as pd

#A Pandas DataFrame is a two-dimensional, size-mutable, and potentially heterogeneous tabular data structure
#in the Python programming language. It is a core component of the Pandas library, widely used for data manipulation and analysis.

data = {
        "Name":["Naruto","Rocklee","Tsunade"],
        "Age" :[17,19,53]
       }

df = pd.DataFrame(data,index=["Employee1","Employee2","Employee3"])
print(df)

print(df.loc["Employee1"])
print(df.iloc[2])

#Adding new column
df["Job"] = ["MC","Woodcutter","#$%*%@#"]
print(df)

#Adding new Rows

new_rows = pd.DataFrame([{"Name":"Sakura","Age":19,"Job":"Hokage"},
                         {"Name":"Pikachu","Age":20,"Job":"EE"},
                        {"Name":"Kakashi","Age":18,"Job":"SC"}]
                    
                        ,index =["Employee4","Employee5","Employee6"])
df = pd.concat([df,new_rows])
print(df)
