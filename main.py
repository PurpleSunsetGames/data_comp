import numpy
import matplotlib

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
        L = line.split(",")
        if len(L)>1:
            waste_data[L[2]] = {"gdp_per_capita":L[4], "composition_food_organic_waste_percent":L[5],"composition_glass_percent":L[6],
                "composition_metal_percent":L[7],"composition_other_percent":L[8],"composition_paper_cardboard_percent":L[9],
                "composition_plastic_percent":L[10],"population_population_number_of_people":L[11],"special_waste_e_waste_tons_year":L[12],
                "total_msw_generated_tons_year":L[13]}

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
    print(country + median_age_data[country]["years"])
