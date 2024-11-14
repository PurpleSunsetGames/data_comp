import numpy
import matplotlib
import pandas as pd
import pandas_datareader as pdr



waste_read = ''
median_age_read = ''
with open("waste_data.csv", "r") as file:
    waste_read = file.read()

with open("Median_age_atoz.csv", "r") as file:
    median_age_read = file.read()


waste_data = {}
median_age_data = {}
column_names = []
column_names_read = False
for line in waste_read.split("\n"):
    if not column_names_read:
        column_names = line.split(",")
        column_names_read = True
    else:
        waste_data.append(line.split(","))

median_age_read = "median.age.csw".split()
start = dt.date.today() - dt.timedelta(365)

for line in median_age_read.split("\n"):
    if not column_names_read:
        column_names = line.split(",")
        column_names_read = True
    else:
        L = line.split(",")
        median_age_data[L[0].strip('"')] = {"years":L[2].strip('"'), "ranking":L[4]}

shared_between_sets = set(waste_data.keys()).intersection(set(median_age_data.keys()))
for country in shared_between_sets:
    print(country + " GDP per Capita: " + waste_data[country]["gdp_per_capita"])
    print(country + " Median Age: " + median_age_data[country]["years"])
print(len(shared_between_sets))
