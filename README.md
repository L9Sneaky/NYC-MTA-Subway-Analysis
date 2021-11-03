# NYC MTA Subway Analysis
### The Blog Post
https://medium.com/@galghanim1999/nyc-mta-subway-analysis-project-6bf76d243d95
### Abstract

The main purpose of this analytical report is to provide clear insights of Metropolitan Transportation Authority (MTA) turnstiles data. Also, the objective of the descriptive analytic report is to reduce the electricity bill of MTA and provide high quality services that satisfy the customers needs. The first stage of analyzing the MTA turnstiles data is to clean, prepare, and handle data. The second stage is to apply the feature selection to MTA data frame and to reduce the compositional processing in a such a way that we achieve the goals of this analysis. Lastly, provide a clear visualization to make the data easier to understand and pull insights from. 


### Design

This project originated from our clients needs to reduce the electricity billand provide high quality services that satisfy the customers needs. The data is provided by NYC MTA traffic data. Our team uses NYC MTA data to locate the least 10 busiest stations in NYC in order to have an idea of each station's Traffic. After that, I have used the results of our analysis to determine which station would be most suitable to reduce turnstile.

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

### Cleaning 

After gathering the necessary data from New York City Metropolitan Transportation Authority Subway Database, I’ve done some Feature Engineering and Cleaning on the data some visualization to view what station is least used.

### Results

![alt text](https://github.com/L9Sneaky/Udacity-Project-1/blob/master/plot2?raw=true)

From this graph, we can see that Orchard Beach is the least commonly used Station. and from this, we check what days do people use this station.

![alt text](https://github.com/L9Sneaky/Udacity-Project-1/blob/master/plot1?raw=true)

From this, we can see that workdays are the least commonly used since the station is close to the beach.
And we check on average traffic on that station with respect to time.

![alt text](https://github.com/L9Sneaky/Udacity-Project-1/blob/master/plot3?raw=true)

We see that from 4 am to 8 am it's practically not used at all so we can shut down the station at that time during the workdays and that would reduce the electricity bill.

### Tools

- Numpy & Pandas for data cleaning and manipulation.
- Matplotlib & plotly for plotting.
