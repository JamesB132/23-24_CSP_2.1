import pandas as pd
import matplotlib.pyplot as plt

co2_data = pd.read_csv("co2_data.csv", header=0)

plt.plot(co2_data['Year'], co2_data['Average'], color='gray')
plt.ylabel('CO2 Levels in ppm')
plt.xlabel('Years')
plt.title('Change in Carbon Dioxide')
plt.show()


