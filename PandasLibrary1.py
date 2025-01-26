#/////READ CSV FILE
import datetime

import pandas as pd
file = 'C:\\Users\sosangle\OneDrive - Capgemini\Microsoft Teams Chat Files\employee.csv'
df = pd.read_csv(file)
print(df)
print(type(df))

df.columns = ["", ""]       #syntax for adding column name in df if not existed


import pandas as pd
emp = {"name":["Sonali", "Vikas", "Prasad", "Pooja", "Sarthak", "Viraj", "Hrishikesh"],
       "Role": ["Data Scientist", "Web Developer", "Analyst", "Consultant", "Full Stack Developer", "Consultant", "Web Developer"],
       "Mob": [9815878745, 8664531903, 6665469023, 8787345601, 8990036472, 7637785390, 9823138535],
       "Age":[23, 21, 26, 23, 20, 21, 23]}
print(emp)

emp_df = pd.DataFrame(emp)
print(emp_df)
print(emp_df["Role"])
print(emp_df.loc[3,"Mob"])
print(emp_df["Age"]>=23)                            #### It only return the boolean values
print(emp_df[emp_df["Age"]>=23])

####### DATAFRAME TO CSV #######
df2 = emp_df[emp_df["Age"]>=23]
df2.to_csv("emp1.csv")

print(emp_df.head())


#/////READ EXCEL FILE
import pandas as pd
exc = "C:\\Users\sosangle\OneDrive - Capgemini\Documents\employee.xlsx"
emp_df1 = pd.read_excel(exc)
print(emp_df1.head())
print(emp_df1['LAST_NAME'])
print(emp_df1[['LAST_NAME']])
print(type(emp_df1[['LAST_NAME']]))
print(emp_df1[['FIRST_NAME', 'LAST_NAME', 'SALARY']])

print(emp_df1.iloc[0,1], "\n\n", emp_df1.iloc[0:4,1:4])
print(emp_df1.iloc[0:2,1], "\n\n", emp_df1.iloc[2,1:3])
print(emp_df1.loc[0,'FIRST_NAME'])
print(emp_df1.loc[6,'FIRST_NAME'])
print(emp_df1.loc[1:6,'FIRST_NAME':'SALARY'])

# ////CHANGE INDEX OF DF
index1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
new_df = emp_df
new_df.index = index1
print(new_df.index)
print(new_df)
print(new_df.loc['a':'c', 'name'])




#//////       JSON FILE
import json
with open("C:\\Users\sosangle\Downloads\\author_with_header.json", "r") as json_file:
       json_obj = json.load(json_file)
print(json_obj)

json_df = pd.read_json("C:\\Users\sosangle\Downloads\\author_with_header.json")
print(json_df)

from datetime import datetime
print(datetime.datetime())


from datetime import datetime, timedelta
delta = datetime.now() + timedelta(
    days=50,
    seconds=27,
    microseconds=10,
    milliseconds=29000,
    minutes=5,
    hours=8,
    weeks=2
)
datetime.datetime.delta

datetime.today()
