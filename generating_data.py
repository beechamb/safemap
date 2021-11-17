#importing necessary packages
import pandas as pd
import random
import csv

#generating random latitudes and longitudes in kalamazoo
latitudes = []
longitudes = []

for i in range (0,1000):
    x = round(random.uniform(42.290646, 42.295677), 6)
    latitudes.append(x)

for i in range (0,1000):
    y = round(random.uniform(-85.589951, -85.594162), 6)
    longitudes.append(y)

#generating times of incidents occurred
time_ranges = ["6am to 10am", "10am to 2pm", "2pm to 6pm", "6pm to 10pm", "10pm to 2am",
               "2am to 6am"]
times = random.choices(time_ranges, weights =(20,10,10,30,80,90), k=1000)

#generating type of incidents occurred
types = ["catcalling", "stalking", "drugging", "groping", "sexual assault", "battery"]
incident_types = random.choices(types, weights=(80, 30, 30, 50, 10, 5), k=1000)

#creating a dataframe with generated values
df = pd.DataFrame()

df["Type"] = incident_types
df["Time"] = times
df["Latitude"] = latitudes
df["Longitude"] = longitudes

df.to_csv("C:/Users/beech/Documents/Graduate_School/CS6100/kzoo.csv")
