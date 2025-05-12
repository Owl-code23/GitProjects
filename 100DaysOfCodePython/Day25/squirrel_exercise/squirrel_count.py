import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250512.csv")

squirrel_color = ["Gray", "Cinnamon", "Black"]
fur_count = []

for color in squirrel_color:
    primary_fur_color = data["Primary Fur Color"]
    fur_count.append(len(data[primary_fur_color == color]))
    # fur_count.append(data[primary_fur_color == color]["Primary Fur Color"].count())
    

squirrel_count = {
    "Fur Color": squirrel_color,
    "Count": fur_count,
}

data = pd.DataFrame(squirrel_count)
data.to_csv("squirrel_count.csv")