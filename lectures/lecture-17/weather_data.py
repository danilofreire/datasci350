import pandas as pd
import numpy as np
import datetime

# Set seed for reproducibility
np.random.seed(42)

# Generate dates for the past 30 days
dates = pd.date_range(end=datetime.datetime.now(), periods=30).tolist()
dates = [d.strftime('%Y-%m-%d') for d in dates]

# Generate temperature data with some randomness
temp_high = np.random.normal(75, 8, 30)
temp_low = temp_high - np.random.uniform(10, 20, 30)
precipitation = np.random.exponential(0.5, 30)
humidity = np.random.normal(65, 10, 30)

# Create a structured dataset
weather_data = pd.DataFrame({
    'date': dates,
    'temp_high': temp_high,
    'temp_low': temp_low,
    'precipitation': precipitation,
    'humidity': humidity
})

# Save to a text file
with open('weather_data.txt', 'w') as f:
    f.write("# Weather data for the past 30 days\n")
    f.write(weather_data.to_string(index=False))
    
print("Weather data saved to weather_data.txt")