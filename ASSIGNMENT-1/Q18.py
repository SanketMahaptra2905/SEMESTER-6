print("NAME:- SANKET MAHAPATRA")
print("REGISTRATION NUMBER:- 2241013017\n")
import pandas as pd
import matplotlib.pyplot as plt
celsius_to_kelvin = lambda celsius: celsius + 273.15
celsius_temps = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
kelvin_temps = list(map(celsius_to_kelvin, celsius_temps))
data = {
    'Celsius': celsius_temps,
    'Kelvin': kelvin_temps
}
df = pd.DataFrame(data)
df.to_csv('temperature_data.csv', index=False)
plt.figure(figsize=(10, 6))
plt.plot(df['Celsius'], df['Kelvin'], marker='o', linestyle='-', color='b')
plt.title('Temperature Conversion: Celsius to Kelvin')
plt.xlabel('Celsius (°C)')
plt.ylabel('Kelvin (K)')
plt.grid(True)
plt.show()