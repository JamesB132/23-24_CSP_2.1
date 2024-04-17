# a322_electricity_trends.py
# This program uses the pandas module to load a 3-dimensional data sheet into a pandas DataFrame object
# Then it will use the matplotlib module to plot comparative line graphs 

import matplotlib.pyplot as plt
import pandas as pd

# choose countries of interest
my_countries = ['Afghanistan', 'Dominican Republic','Malaysia', 'Zimbabwe']

# Load in the data with read_csv()
df = pd.read_csv("elec_access_data.csv", header=0)    # header=0 means there is a header in row 0

# get a list unique countries
unique_countries = df['Entity'].unique()

# Plot the data on a line graph
for c in unique_countries:
  if c in my_countries:
    
    # match country to one of our we want to look at and get a list of years
    years = df[df['Entity'] == c]['Year']

    # match country to one of our we want to look at and get a list of electriciy values
    sum_elec = df[df['Entity'] == c]['Access']

    plt.plot(years, sum_elec, label=c, marker='p', linestyle='-.')

  
plt.ylabel('Percentage of Country Population')
plt.xlabel('Year')
plt.title('Percent of Population with Access to Electricity')
plt.legend()
plt.show()

#North/South American Countries

na_countries = ['Colombia', 'Canada', 'El Salvador', 'Costa Rica', 'United States', 'Mexico']
df = pd.read_csv("elec_access_data.csv", header=0)
unique_countries = df['Entity'].unique()

for c in unique_countries:
  if c in na_countries:
    years = df[df['Entity'] == c]['Year']
    sum_elec = df[df['Entity'] == c]['Access']
    plt.plot(years, sum_elec, label=c, marker='s', linestyle='--')

plt.ylabel('Percentage of Country Population')
plt.xlabel('Year')
plt.title('Percent of Population with Access to Electricity in North and South America')
plt.legend()
plt.show()

#Europe

eu_countries = ['Austria', 'Belgium', 'Bulgaria', 'Croatia', 'Republic of Cyprus', 'Czech Republic']
df = pd.read_csv("elec_access_data.csv", header=0)
unique_countries = df['Entity'].unique()

for c in unique_countries:
  if c in eu_countries:
    years = df[df['Entity'] == c]['Year']
    sum_elec = df[df['Entity'] == c]['Access']
    plt.plot(years, sum_elec, label=c, marker='>', linestyle='-')

plt.ylabel('Percentage of Country Population')
plt.xlabel('Year')
plt.title('Percent of Population with Access to Electricity in Europe')
plt.legend()
plt.show()

#Asia

asian_countries = ['India', 'Nepal', 'China', 'Singapore', 'Bangladesh', 'North Korea']
df = pd.read_csv("elec_access_data.csv", header=0)
unique_countries = df['Entity'].unique()

for c in unique_countries:
  if c in asian_countries:
    years = df[df['Entity'] == c]['Year']
    sum_elec = df[df['Entity'] == c]['Access']
    plt.plot(years, sum_elec, label=c, marker='<', linestyle=':')

plt.ylabel('Percentage of Country Population')
plt.xlabel('Year')
plt.title('Percent of Population with Access to Electricity in Asia')
plt.legend()
plt.show()

#African

African_countries = ['South Africa', 'Nigeria', 'Morocco', 'Senegal', 'Uganda', 'Mali']
df = pd.read_csv("elec_access_data.csv", header=0)
unique_countries = df['Entity'].unique()

for c in unique_countries:
  if c in African_countries:
    years = df[df['Entity'] == c]['Year']
    sum_elec = df[df['Entity'] == c]['Access']
    plt.plot(years, sum_elec, label=c, marker='v', linestyle='-.')

plt.ylabel('Percentage of Country Population')
plt.xlabel('Year')
plt.title('Percent of Population with Access to Electricity in Europe')
plt.legend()
plt.show()

