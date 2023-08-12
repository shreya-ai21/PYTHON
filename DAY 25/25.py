# this method bad
# with open('weather_data.csv') as data:
#     content=data.readlines()

# this method batter
# import csv
# with open("DAY 25\weather_data.csv") as file:
#     data = csv.reader(file)
#     data_list = list(data)
#     temperatures = []
#     for i in range(1, len(data_list)):
#         temperatures.append(int(data_list[i][1]))
#     print(temperatures)

# this method best
import pandas as pd
# import pandas
# data = pandas.read_csv('DAY 25\weather_data.csv')
# print(data['temp'])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data['temp'].to_list()
# print(temp_list)

# avg = sum(temp_list)/len(temp_list)
# print(avg)
# print(data['temp'].mean())
# print(data['temp'].max())

# monday = data[data.day == "Monday"]
# print(data[data.temp == data['temp'].max()])
# monday_temp = int(monday.temp)
# ans = (monday_temp * 9/5) + 32
# print(ans)

data = pd.read_csv("DAY 25\squirrel.csv")
gray = len(data[data["Primary Fur Color"] == 'Gray'])
cinnamon = len(data[data["Primary Fur Color"] == 'Cinnamon'])
black = len(data[data["Primary Fur Color"] == 'Black'])
print(gray)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray, cinnamon, black]
}

df = pd.DataFrame(data_dict)
df.to_csv('squirrel_count.csv')
