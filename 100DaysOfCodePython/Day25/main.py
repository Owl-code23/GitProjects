# with open('weather_data.csv') as weather_data:
#     data = weather_data.readlines()
#     print(data)

# import csv

# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas as pd

data = pd.read_csv('weather_data.csv')
# print(type(data))
# print(data)
# print(data['temp'])

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)
# print(len(temp_list))
# print(sum(temp_list) / len(temp_list))
print(data["temp"].mean())
print(data["temp"].max())

# Get Data in Columns
print(data["condition"])
print(data.condition)

# Get Data in Row
print(data[data["day"] == "Monday"])
print(data[data["temp"] == data["temp"].max()])

monday = data[data["day"] == "Monday"]
print(monday.condition)

# Convert Celsius to Fahrenheit
print(monday.temp * 9/5 + 32)

# Create a dataframe from scratch
st_data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65],
}
data = pd.DataFrame(st_data_dict)
data.to_csv("new_data.csv")
print(data)