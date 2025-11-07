#BIKE COLLISION ANALYSIS - TINA TRAN
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import numpy as np
import calendar
from scipy.stats import pearsonr


df =pd.read_csv(r"C:\Users\tinat\Desktop\Traffic_Collisions_Open_Data_3719442797094142699.csv")
#print(df.head()) #check data

df_2019 = df[(df['OCC_YEAR'] >= 2019) & (df['OCC_YEAR'] < 2025)]

#df_2019 = df.dropna()
#print(df_2019.isnull().sum()) #check for null
#print(df_2019.duplicated().sum()) #check for duplicate


df_2019["OCC_DATE"] = pd.to_datetime(df["OCC_DATE"])
df_2019['OCC_HOUR'] = pd.to_numeric(df_2019['OCC_HOUR'])
#df_2019.info()

#print(len(df_2019))

bike_acc_df = df_2019[df_2019['BICYCLE']=='YES']
year_counts = bike_acc_df.groupby('OCC_YEAR').size()

#print(len(bike_acc_df))
#analyze year vs bike accident
plt.figure(figsize =(6,6))
plt.bar(year_counts.index, year_counts.values) 
plt.title('Bike Accidents per Year (2019+)')
plt.xlabel('Year')
plt.ylabel('Number of Accidents')
plt.show()

print("Mean bike accidents per year:", int(year_counts.mean()))

heatmap_data = bike_acc_df.pivot_table(
    index='OCC_HOUR',        
    columns='OCC_DOW',       
    values='OBJECTID', 
    aggfunc='count'          
)

weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
heatmap_data = heatmap_data.reindex(columns = weekday_order)
heatmap_data = heatmap_data / bike_acc_df['OCC_YEAR'].nunique()

plt.figure(figsize=(12,6))
sns.heatmap(heatmap_data, cmap = 'YlOrRd')
plt.title("Bike Accidents Heatmap: Hour vs Weekday (2019-2025)")
plt.xlabel("Weekday")
plt.ylabel("Hour of Day")
plt.show()

weather_df = pd.read_csv(r"C:\Users\tinat\Desktop\weatherstats_toronto_normal_daily.csv")


weather_df['date'] = pd.to_datetime(weather_df['date'])

# Filter data from 2019 onwards
data_2019 = weather_df[(weather_df['date'] >= '2019-01-01') & (weather_df['date'] <= '2024-12-31')]
data_2019['Year'] = data_2019['date'].dt.year
data_2019['Month'] = data_2019['date'].dt.month

# Create pivot table for rainfall data
rainfall_v = data_2019.pivot_table(index='Month', columns='Year', values="rain_v")
grand_avg_per_month = round(rainfall_v.mean(axis=1), 1)

# Prepare monthly names and ordering
grand_avg_per_month.index = grand_avg_per_month.index.map(lambda m: calendar.month_name[m])
month_order = ['January', 'February', 'March', 'April', 'May', 'June', 
               'July', 'August', 'September', 'October', 'November', 'December']
grand_avg_per_month = grand_avg_per_month.reindex(month_order)

# Calculate bike accident monthly averages
month_counts = bike_acc_df.groupby('OCC_MONTH').size()
month_counts = month_counts / bike_acc_df['OCC_YEAR'].nunique()
month_counts = month_counts.reindex(index=month_order)

# Create combined bar and line plot
plt.figure(figsize=(14, 6))
plt.bar(grand_avg_per_month.index, grand_avg_per_month.values, alpha=0.7, label='Rainfall (mm)')
plt.plot(month_counts.index, month_counts.values, color='red', marker='o', linewidth=2, label='Bike Accidents')
plt.xlabel('Month of the Year')
plt.ylabel('Values')
plt.title("Rainfall and Bike Accidents from 2019-2025")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Linear regression analysis
x = grand_avg_per_month.values
y = month_counts.values
m, b = np.polyfit(x, y, 1)
predicted_Y = m * x + b

correlation, p_value = pearsonr(x, y)

print(f"Pearson Correlation Coefficient: {correlation:.3f}")
print(f"P-value: {p_value:.3f}")
print(f"Statistical significance: {'Significant' if p_value < 0.05 else 'Not significant'}")


# Create scatter plot with regression line
plt.figure(figsize=(10, 6))
plt.scatter(x, y, s=80, alpha=0.7)
plt.plot(x, predicted_Y, color='red', linewidth=2, label=f'Regression line: y = {m:.4f}x + {b:.4f}')
plt.xlabel("Rainfall Volume (mm)")
plt.ylabel("Bike Accidents")
plt.title("Linear Regression of Rainfall vs Bike Accidents from 2019-2025")
plt.title(f"Linear Regression (r = {correlation:.3f})")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()




