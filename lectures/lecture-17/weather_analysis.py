import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO  # Add proper import for StringIO

# Read the weather data
with open('weather_data.txt', 'r') as f:
    lines = f.readlines()

# Skip the header comment
data_str = ''.join(lines[1:])
df = pd.read_csv(StringIO(data_str), sep=r'\s+')  # Fix StringIO import and use raw string for regex

# Print basic statistics
print("Weather Data Analysis:")
print("=====================")
print(f"Number of days: {len(df)}")
print(f"Average high temperature: {df['temp_high'].mean():.1f}°F")
print(f"Average low temperature: {df['temp_low'].mean():.1f}°F")
print(f"Maximum temperature: {df['temp_high'].max():.1f}°F on {df.loc[df['temp_high'].idxmax(), 'date']}")
print(f"Minimum temperature: {df['temp_low'].min():.1f}°F on {df.loc[df['temp_low'].idxmin(), 'date']}")
print(f"Days with precipitation > 1 inch: {len(df[df['precipitation'] > 1])}")

# Create a visualisation
plt.figure(figsize=(12, 6))
sns.set_style("whitegrid")

# Plot temperature range
plt.fill_between(df['date'], df['temp_low'], df['temp_high'], alpha=0.3, color='skyblue')
plt.plot(df['date'], df['temp_high'], marker='o', color='red', label='High Temp')
plt.plot(df['date'], df['temp_low'], marker='o', color='blue', label='Low Temp')

# Add precipitation as bars on a secondary axis
ax2 = plt.twinx()
ax2.bar(df['date'], df['precipitation'], alpha=0.3, color='navy', width=0.5, label='Precipitation')
ax2.set_ylabel('Precipitation (inches)', color='navy')
ax2.tick_params(axis='y', labelcolor='navy')

# Formatting
plt.title('30-Day Weather Report: Temperature Range and Precipitation', fontsize=16)
plt.xticks(rotation=45, ha='right')
plt.ylabel('Temperature (°F)')
plt.legend(loc='upper left')
plt.tight_layout()

# Save the figure
plt.savefig('weather_analysis.png')
print("Analysis complete. Results saved to 'weather_analysis.png'")