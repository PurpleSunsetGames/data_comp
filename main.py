import numpy
import matplotlib

waste_read = ''
median_age_read = ''
with open("waste_data.csv", "r") as file:
    waste_read = file.read()

with open("waste_data.csv", "r") as file:
    median_age_read = file.read()


waste_data = []
median_age_data = []
column_names = []
column_names_read = False
for line in waste_read.split("\n"):
    if not column_names_read:
        column_names = line.split(",")
        column_names_read = True
    else:
        waste_data.append(line.split(","))
    


