# Minority-Report

## Team
Rute Souza de Abreu
Yuri Thomas Pinheiro Nunes

## Objectives

The objectives of the project are to analyze police incident data and extract information that can help predict and respond efficiently. The occurrences were recorded in the Montgomery County Police Database in the state of Maryland, United States. Data refer to the last six months of 2013. Data that may harm an individual's privacy has been removed and information such as address has been rounded up to 100 homes.

To accomplish the objectives, the occurrences will be categorized by the calling code used in radio communication. Analyzes related to location and time will be performed. For time analysis a time profile related to the time of day will be created and another event profile related to the days of the week. For location profiles were created by city and by police district.

## Division of notebooks

3 notebooks and a python script were created. The python script makes some changes to the original dataset; they are: the categorization of crimes according to the county police regiment, the creation of the category column reporting the category to which the crime belongs, and the conversion of the date of the occurrences to DateTime type. This script is imported to other notebooks. The first notebook is a Dataset Description, containing the description and explanation of all columns, as well as the answers to the initial questions raised by the activity. The second notebook (Time Analysis) makes a temporal analysis of occurrences, the analyzes contained in this notebook are: hourly, weekly, by period of the day (day and night) and the analysis of the interval between occurrences of the same category. The third notebook (Location Analysis) comprises location-related analyzes, where crime rates by city and police district are calculated, and the top 10 types of occurrences in each location are also surveyed.

## Conclusions

In the weekly profile it was possible to perceive seasonality issues as the highest number of theft occurrences and drug related occurrences during the week. In contrast, there are a higher number of suicide occurrences on weekends. This information can help in planning to ensure a higher level of patrolling during the week and to manage staff for psychological help for people more likely to commit suicide.

In the hourly profile one can clearly note that drug-related occurrences occur at night while thefts during the day.

Regarding the analyzes that relate the crimes with the localities, that is, crimes by city and crimes by police district, we could realize that the crime of 'Lacerny', which concerns theft / theft, was the crime with the highest percentage of occurrence. in 20 of the 32 cities and in 6 of the 8 districts.


## Requirements

- NumPy
- Pandas
- Matploblib
