import csv

import pandas as pd

data = []

with open("final.csv",'r') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        data.append(row)

headers = data[0]
star_data = data[1:]

dataframe = pd.read_csv("final.csv")

stars_mass = dataframe["solar_mass"].tolist()
stars_radius = dataframe["solar_radius"].tolist()
star_names = dataframe["star_names"].tolist()

stars_mass.pop(0)
stars_radius.pop(0)
star_names.pop(0)

solar_mass = []

for row in solar_mass:
    si_unit = float(data)*1.989e+30
    solar_mass.append(si_unit)

solar_radius = []

for data in solar_radius:
    si_unit = float(data)* 6.957e+8
    solar_radius.append(si_unit)


star_mass = solar_mass
star_radius = solar_radius

star_gravities = []
for index,data in enumerate(star_names):
    gravity = (float(star_mass[index])*5.972e+24) / (float(star_radius[index])*float(star_radius[index])*6371000*6371000) * 6.674e-11
    star_gravities.append(gravity)

    print("The gravity of the", star_names[index], "star is", star_gravities)