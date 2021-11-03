# Udacity-Project-1
https://medium.com/@galghanim1999/nyc-mta-subway-analysis-project-6bf76d243d95
### Abstract


The main purpose of this analytical report is to provide clear insights of Metropolitan Transportation Authority (MTA) turnstiles data. Also, the objective of the descriptive analytic report is to reduce the electricity bill of MTA and provide high quality services that satisfy the customers needs. The first stage of analyzing the MTA turnstiles data is to clean, prepare, and handle data. The second stage is to apply the feature selection to MTA data frame and to reduce the compositional processing in a such a way that we achieve the goals of this analysis. Lastly, provide a clear visualization to make the data easier to understand and pull insights from.  

### Design

This project originated from our clients needs to reduce the electricity billand provide high quality services that satisfy the customers needs. The data is provided by NYC MTA traffic data. Our team uses NYC MTA data to locate the top 10 & least 10 busiest stations in NYC in order to have an idea of each station's Traffic. After that, our team used the results of our analysis to determine which station would be most suitable to reduce turnstile.

### Data

We will use data about the patterns of transit traffic in New York City: MTA turnstile data, collect and clean our data set and then we will perform EDA to better understand our data:  
1. Station:		Represents the station name the device is located at.
2. date:			Represents the date.
3. time:			Represents the time for a scheduled audit event.
4. entries:		The cumulative entry register value for a device.
5. exits:		The cumulative exit register value for a device.
6. station_code:	C/A + unit, locating a station.

The unit of analysis is the group. After modeling and analysis data economic companies will be able to benefit from crowded in each station and helping people to spend their waiting time in a fun and useful day.


### Algorithms

1. Performed data cleaning.
2. Visualized the data and removed outliers.
3. Aggregated the data by station and ordered by Highest & Lowest Traffic.
4. Visualized the resutled clean data.


### Tools

- Numpy & Pandas for data cleaning and manipulation.
- Matplotlib & plotly for plotting.
