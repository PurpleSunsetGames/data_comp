import numpy as np
import matplotlib
import matplotlib.pyplot as plt
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
        L = line.split(",")
        if len(L)>1:
            waste_data[L[2]] = {"gdp_per_capita":float(L[4]), "composition_food_organic_waste_percent":float(L[5]),"composition_glass_percent":L[6],
                "composition_metal_percent":float(L[7]),"composition_other_percent":float(L[8]),"composition_paper_cardboard_percent":float(L[9]),
                "composition_plastic_percent":float(L[10]),"population_population_number_of_people":float(L[11]),"special_waste_e_waste_tons_year":float(L[12]),
                "total_msw_generated_tons_year":float(L[13])}
column_names_read=False

for line in median_age_read.split("\n"):
    if not column_names_read:
        column_names = line.split(",")
        column_names_read = True
    else:
        L = line.split(",")
        median_age_data[L[0].strip('"')] = {"years":float(L[2].strip('"')), "ranking":L[4]}

shared_between_sets = set(waste_data.keys()).intersection(set(median_age_data.keys()))
median_age_list = []
gdp_per_capita_list = []
composition_food_organic_waste_percent_list = []
composition_glass_percent_list = []
composition_metal_percent_list = []
composition_other_percent_list = []
composition_paper_cardboard_percent_list = []
composition_plastic_percent_list = []
population_population_number_of_people_list = []
special_waste_e_waste_tons_year_list = []
total_msw_generated_tons_year_list = []
for country in shared_between_sets:
    # Creating lists of each attribute
    median_age_list.append(median_age_data[country]["years"])
    gdp_per_capita_list.append(waste_data[country]["gdp_per_capita"])
    composition_food_organic_waste_percent_list.append(waste_data[country]["composition_food_organic_waste_percent"])
    composition_glass_percent_list.append(waste_data[country]["composition_glass_percent"])
    composition_metal_percent_list.append(waste_data[country]["composition_metal_percent"])
    composition_other_percent_list.append(waste_data[country]["composition_other_percent"])
    composition_paper_cardboard_percent_list.append(waste_data[country]["composition_paper_cardboard_percent"])
    composition_plastic_percent_list.append(waste_data[country]["composition_plastic_percent"])
    population_population_number_of_people_list.append(waste_data[country]["population_population_number_of_people"])
    special_waste_e_waste_tons_year_list.append(waste_data[country]["special_waste_e_waste_tons_year"])
    total_msw_generated_tons_year_list.append(waste_data[country]["total_msw_generated_tons_year"])

    #print(country + " GDP per Capita: " + str(waste_data[country]["gdp_per_capita"]))
    #print(country + " Median Age: " + str(median_age_data[country]["years"]))

# Converting them all to np arrays
median_age_list = np.array(median_age_list)
gdp_per_capita_list = np.array(gdp_per_capita_list)
composition_food_organic_waste_percent_list = np.array(composition_food_organic_waste_percent_list)
composition_glass_percent_list = np.array(composition_glass_percent_list)
composition_metal_percent_list = np.array(composition_metal_percent_list)
composition_other_percent_list = np.array(composition_other_percent_list)
composition_paper_cardboard_percent_list = np.array(composition_paper_cardboard_percent_list)
composition_plastic_percent_list = np.array(composition_plastic_percent_list)
population_population_number_of_people_list = np.array(population_population_number_of_people_list)
special_waste_e_waste_tons_year_list = np.array(special_waste_e_waste_tons_year_list)
total_msw_generated_tons_year_list = np.array(total_msw_generated_tons_year_list)

print(len(shared_between_sets))

print("--")
#print(median_age_data)
#print(median_age_list)

# Shows the amount of e_waste per person with respect to median age.
# Our initial hypothesis was that e_waste would be higher in countries with a lower median age, but this graph
# shows the opposite, suggesting that e_waste is probably correlated with another factor that is associated
# with median age, such as GDP. So, I also added the GDP graph, and the correlation looks almost exactly the same.
fig, axs = plt.subplots(2)
axs[0].set(ylabel="e-waste per person")
axs[1].set(xlabel="median age", ylabel="gdp per capita")

axs[0].scatter(x=median_age_list, y = special_waste_e_waste_tons_year_list / population_population_number_of_people_list)
axs[1].scatter(x=median_age_list, y = gdp_per_capita_list)
plt.show()

reg=np.polyfit(median_age_list, gdp_per_capita_list, deg = 1)
print(reg)

