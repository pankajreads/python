# import csv
# max_temp=[]
# with open("weather.csv") as file:
#     weather=csv.reader(file)
#     for row in weather:
#         try:
#             max_temp.append(int(row[2]))
#         except:   
#             continue
# print(max_temp)
import pandas as pd
#read any file using pandas
data=pd.read_csv("weather.csv")
print(data)
#fetching a series using pandas
print(data["Date"])
#creating a dataframe using Pandas
created_data=pd.DataFrame(
    {
    "Name":["ramu","keshav","bhadva"]
    }
    )
#creating a series
ages=pd.Series([22,35,58],name="Age")
#adding the created series in dataframe
# data["Age"]=ages
created_data["Age"]=ages 
#checking the added series and also use head to display first four items
print(data.head(7))
print(created_data)
#display statistics
print(data.describe())
#genereting an ouput file
created_data.to_excel("Created_data.xlsx",index=False)
#check the type of all series name
print(data["Max Temp (°C)"].dtypes)
#sheet_name is the name of sheet in the excel file
#  titanic = pd.read_excel("titanic.xlsx", sheet_name="passengers")

#technical summary like name of series and and how many values have been filled
# print(data.info())
above_20=data[data["Max Temp (°C)"]>20]
print(above_20.shape)#print no. of rows,column in a tuple
print(above_20.head())