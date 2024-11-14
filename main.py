import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader as pdr


HDI_read = ''
waste_read = ''
median_age_read = ''
with open("waste_data.csv", "r") as file:
    waste_read = file.read()

with open("Median_age_atoz.csv", "r") as file:
    median_age_read = file.read()

with open("HDR23-24_Statistical_Annex_HDI_Table.csv") as file:
    HDI_read = file.read()



waste_data = {}
median_age_data = {}
HDI_data = {}

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

column_names_read=False
for line in HDI_read.split("\n"):
    if not column_names_read:
        column_names = line.split(",")
        column_names_read=True
    else:
        L=line.split(",")
        #Name and HDI Itself only
        HDI_data[L[1].strip('"')] = {"HDI":float(L[2].strip('"'))}


shared_between_sets = set(waste_data.keys()).intersection(set(median_age_data.keys()).intersection(set(HDI_data.keys())))
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
HDI_list = []
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
    HDI_list.append(HDI_data[country]["HDI"])

    #print(country + " GDP per Capita: " + str(waste_data[country]["gdp_per_capita"]))
    #print(country + " Median Age: " + str(median_age_data[country]["years"]))

print(HDI_list)




# Converting them all to np arrays
HDI_list=np.array(HDI_list)
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
fig, axs = plt.subplots(3,3)
axs[0, 0].set(ylabel="e-waste per person")
axs[1, 0].set(ylabel="organic waste %")
axs[2, 0].set(xlabel="median age", ylabel="plastic waste %")

axs[0, 0].scatter(x=median_age_list, y = special_waste_e_waste_tons_year_list / population_population_number_of_people_list)
axs[1, 0].scatter(x=median_age_list, y = composition_food_organic_waste_percent_list)
axs[2, 0].scatter(x=median_age_list, y = composition_plastic_percent_list)

axs[2, 1].set(xlabel="gdp per capita")

axs[0, 1].scatter(x=gdp_per_capita_list, y = special_waste_e_waste_tons_year_list / population_population_number_of_people_list)
axs[1, 1].scatter(x=gdp_per_capita_list, y = composition_food_organic_waste_percent_list)
axs[2, 1].scatter(x=gdp_per_capita_list, y = composition_plastic_percent_list)

axs[2, 2].set(xlabel="gdp per capita")

# still have to put hdi data into a list
axs[0, 2].scatter(x=hdi_list, y = special_waste_e_waste_tons_year_list / population_population_number_of_people_list)
axs[1, 2].scatter(x=hdi_list, y = composition_food_organic_waste_percent_list)
axs[2, 2].scatter(x=hdi_list, y = composition_plastic_percent_list)

# Linear regressions
reg0=np.polyfit(median_age_list, special_waste_e_waste_tons_year_list / population_population_number_of_people_list, deg = 1)
axs[0, 0].plot(range(15,51), reg0[0]*np.array(range(15,51))+reg0[1], 'tab:red')

reg1=np.polyfit(median_age_list, composition_food_organic_waste_percent_list, deg = 1)
axs[1, 0].plot(range(15,51), reg1[0]*np.array(range(15,51))+reg1[1], 'tab:red')

reg2=np.polyfit(median_age_list, composition_plastic_percent_list, deg = 1)
axs[2, 0].plot(range(15,51), reg2[0]*np.array(range(15,51))+reg2[1], 'tab:red')

reg01=np.polyfit(gdp_per_capita_list, special_waste_e_waste_tons_year_list / population_population_number_of_people_list, deg = 1)
axs[0, 1].plot(range(0,120000,10000), reg01[0]*np.array(range(0,120000,10000))+reg01[1], 'tab:red')

reg11=np.polyfit(gdp_per_capita_list, composition_food_organic_waste_percent_list, deg = 1)
axs[1, 1].plot(range(0,120000,10000), reg11[0]*np.array(range(0,120000,10000))+reg11[1], 'tab:red')

reg21=np.polyfit(gdp_per_capita_list, composition_plastic_percent_list, deg = 1)
axs[2, 1].plot(range(0,120000,10000), reg21[0]*np.array(range(0,120000,10000))+reg21[1], 'tab:red')

reg02=np.polyfit(hdi_list, special_waste_e_waste_tons_year_list / population_population_number_of_people_list, deg = 1)
axs[0, 2].plot(range(0,1), reg02[0]*np.array(range(0,1))+reg02[1], 'tab:red')

reg12=np.polyfit(hdi_list, composition_food_organic_waste_percent_list, deg = 1)
axs[1, 2].plot(range(0,1), reg12[0]*np.array(range(0,1))+reg12[1], 'tab:red')

reg22=np.polyfit(hdi_list, composition_plastic_percent_list, deg = 1)
axs[2, 2].plot(range(0,1), reg22[0]*np.array(range(0,1))+reg22[1], 'tab:red')

# Exponential regressions
expreg0=np.polyfit(median_age_list, np.log(special_waste_e_waste_tons_year_list / population_population_number_of_people_list), deg = 1)
expreg0=[np.exp(expreg0[0]),np.exp(expreg0[1])]
axs[0, 0].plot(range(15,51), expreg0[1]*(expreg0[0]**np.array(range(15,51))), 'tab:orange')

expreg1=np.polyfit(median_age_list, np.log(composition_food_organic_waste_percent_list), deg = 1)
expreg1=[np.exp(expreg1[0]),np.exp(expreg1[1])]
axs[1, 0].plot(range(15,51), expreg1[1]*(expreg1[0]**np.array(range(15,51))), 'tab:orange')

expreg2=np.polyfit(median_age_list, np.log(composition_plastic_percent_list), deg = 1)
expreg2=[np.exp(expreg2[0]),np.exp(expreg2[1])]
axs[2, 0].plot(range(15,51), expreg2[1]*(expreg2[0]**np.array(range(15,51))), 'tab:orange')

plt.show()