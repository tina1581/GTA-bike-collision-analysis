# 🚴‍♂️ Toronto Bike Collision Analysis (2019–2024)
This project analyzes bike collisions in Toronto from 2019 to 2024.
The goal: Identify collision paterns across time, geography, weather, and seasonality to better understand factors that contributes to cyclist accidents. 

## Focusing area:
- Yearly trends
- Hourly & weekday patterns
- Seasonal changes
- Weather impact
- Geographic collision hotspots
  
### 🛠 Tools Used
- Python
- Power BI
- DAX

## 🐍 Data Processing
- Importing and cleaning raw collision and weather data  
- Handling missing and duplicated values
- Generating date features (year, month, weekday, hour)  
- Merging weather data with collision data
- Exploration analysis: trend visualizations, heatmap, linear regression model, statistical analysis
- Libraries including: pandas numpy  matplotlib seaborn
  
## 🔗 Live Dashboard
View the interactive Power BI dashboard:

## 📊 Dashboard Overview
The Dashboard report includes:
- **KPI Summary**
  - Annual average collisions
  - CAGR (2019–2024)

- **Visualizations**
  - Geographic collision hotspot map  
  - Trend of yearly collisions (2019–2024)  
  - Hour × weekday collision heatmap  
  - Seasonal collision trends  
  - Weather vs collision patterns  

## 🔑 Key Insights
- Accidents significantly increased when comparing 2019–2024. This may be due to the pandemic, which decreased the number of cyclists during the lockdown.  
- From 2019 to 2024, bike accidents peak between 3 PM and 7 PM, likely due to rush hour traffic. 
- Accidents decrease from September to December and increase from April to August, reflecting higher cycling activity during warmer months.
- **Limitations:**
   - Linear regression is not ideal for count data; a Poisson model would be more appropriate.  
   - The R value of 0.7 indicates only a moderate linear relationship between rain and bike collisions.  
   - Monthly rainfall data may hide whether accidents occurred on rainy days; daily data would provide clearer insights.  



