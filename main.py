# %%
# import libraries

#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
import missingno as msno
import plotly.express as px


# In[2]:


def get_data(week_nums):
    url = "http://web.mta.info/developers/data/nyct/turnstile/turnstile_{}.txt"
    dfs = []
    for week_num in week_nums:
        file_url = url.format(week_num)
        dfs.append(pd.read_csv(file_url))
    return pd.concat(dfs)

week_nums = [210828, 210821, 210814, 210807, 210731, 210724, 210717, 210710, 210703, 210626,210619, 210612, 210605]
turnstiles_df = get_data(week_nums)


# In[3]:


turnstiles_df.head()


# In[4]:


turnstiles_df.tail()


# In[5]:


turnstiles_df.describe()


# In[6]:


turnstiles_df.info()


# In[7]:


# From importing the data from the website, we noticed some extra spaced columns
turnstiles_df.columns


# In[8]:


# The purpose of this line of code is to fix and adjust the extra spacing in the columns
turnstiles_df.columns = [column.strip() for column in turnstiles_df.columns]
turnstiles_df.columns


# In[9]:


# Three months of Data
turnstiles_df.DATE.value_counts().sort_index()


# In[10]:


# Since our imported data's date and time columns are object dtype, we need to put the date and time in a single column and change from object to datetime dtype to help us to access the data easily
turnstiles_df["DATE_TIME"] = pd.to_datetime(turnstiles_df.DATE + " " + turnstiles_df.TIME,format="%m/%d/%Y %H:%M:%S")


# In[11]:


turnstiles_df.head()


# In[12]:


# By applying the mask concept we can filter the data for such a specefic station
mask = ((turnstiles_df["C/A"] == "R504") &
(turnstiles_df["UNIT"] == "R276") &
(turnstiles_df["SCP"] == "00-00-01") &
(turnstiles_df["STATION"] == "VERNON-JACKSON"))

turnstiles_df[mask].head()


# In[13]:


# Sanity Check to verify that "C/A", "UNIT", "SCP", "STATION", "DATE_TIME" is unique
(turnstiles_df
 .groupby(["C/A", "UNIT", "SCP", "STATION", "DATE_TIME"])
 .ENTRIES.count()
 .reset_index()
 .sort_values("ENTRIES", ascending=False))


# In[14]:


# The detailed information about duplicated rows
turnstiles_df[turnstiles_df.duplicated(subset=["C/A", "UNIT", "SCP", "STATION", "DATE_TIME"])]


# In[15]:


# Number of diplicarted rows
turnstiles_df.duplicated(subset=["C/A", "UNIT", "SCP", "STATION", "DATE_TIME"]).sum()


# In[16]:


# By applying the mask concept we can filter the data for such a specefic station and time
mask1 = ((turnstiles_df["C/A"] == "R504") &
(turnstiles_df["UNIT"] == "R276") &
(turnstiles_df["SCP"] == "00-00-01") &
(turnstiles_df["STATION"] == "VERNON-JACKSON") &
(turnstiles_df["DATE_TIME"].dt.date == dt.datetime(2021, 8, 21).date()))


# In[17]:


turnstiles_df[mask1].head()


# In[18]:


# To check if there is any NULL value
turnstiles_df.info()


# In[19]:


# To check if there is any NULL value
turnstiles_df.isna().sum()


# In[20]:


# Visualize missing values as a matrix

msno.matrix(turnstiles_df)


# In[21]:


# Handle missing values if any
turnstiles_df.dropna()


# In[22]:


# Alternative methode to handle missing values if any
turnstiles_df.fillna(0)


# In[23]:


# By applying the mask concept we can filter the data for such a specefic station and time
mask2 = ((turnstiles_df["C/A"] == "R504")&(turnstiles_df["UNIT"] == "R276")&(turnstiles_df["SCP"] == "00-00-01")&(turnstiles_df["STATION"] == "VERNON-JACKSON")&(turnstiles_df["DESC"] == "RECOVR AUD")&(turnstiles_df["DATE_TIME"].dt.date == dt.datetime(2021, 8, 16).date()))
turnstiles_df[mask2].head()


# In[24]:


turnstiles_df.DESC.value_counts()


# In[25]:


# Get rid of the duplicate entry
turnstiles_df.sort_values(["C/A", "UNIT", "SCP", "STATION", "DATE_TIME"],
                          inplace=True, ascending=False)
turnstiles_df.drop_duplicates(subset=["C/A", "UNIT", "SCP", "STATION", "DATE_TIME"], inplace=True)


# In[26]:


# Sanity Check to verify that "C/A", "UNIT", "SCP", "STATION", "DATE_TIME" is unique
(turnstiles_df.groupby(["C/A", "UNIT", "SCP", "STATION", "DATE_TIME"]).ENTRIES.count().reset_index().sort_values("ENTRIES", ascending=False)).head(5)


# In[27]:


# No more duplicated rows
turnstiles_df.duplicated(subset=["C/A", "UNIT", "SCP", "STATION", "DATE_TIME"]).sum()


# In[28]:


# The detailed information about non-duplicated rows
turnstiles_df[turnstiles_df.duplicated(subset=["C/A", "UNIT", "SCP", "STATION", "DATE_TIME"])]


# In[29]:


# The sum of number of entries for each unique turnstile at a specefict time and date
turnstiles_daily = (turnstiles_df.groupby(["C/A", "UNIT", "SCP", "STATION", "DATE","TIME"],as_index=False).ENTRIES.first())

turnstiles_daily.head(20)


# In[30]:


turnstiles_daily[["PREV_DATE", "PREV_ENTRIES"]] = (turnstiles_daily.groupby(["C/A", "UNIT", "SCP", "STATION"])["DATE", "ENTRIES"].apply(lambda grp: grp.shift(1)))


# Drop the rows for the earliest date in the df
turnstiles_daily.dropna(subset=["PREV_DATE"], axis=0, inplace=True)

# Handle missing values if any
turnstiles_daily.dropna()

turnstiles_daily[turnstiles_daily["ENTRIES"] < turnstiles_daily["PREV_ENTRIES"]].head()


# What's the deal with counter being in reverse
mask = ((turnstiles_df["C/A"] == "A011")&(turnstiles_df["UNIT"] == "R080")&(turnstiles_df["SCP"] == "01-00-00")&(turnstiles_df["STATION"] == "57 ST-7 AV")&(turnstiles_df["DATE_TIME"].dt.date == dt.datetime(2021, 8, 27).date()))
turnstiles_df[mask].head()

(turnstiles_daily[turnstiles_daily["ENTRIES"] < turnstiles_daily["PREV_ENTRIES"]].groupby(["C/A", "UNIT", "SCP", "STATION"]).size())


# In[31]:


def get_daily_counts(row, max_counter):
    counter = row["ENTRIES"] - row["PREV_ENTRIES"]
    if counter < 0:
        # Maybe counter is reversed?
        counter = -counter
    if counter > max_counter:
        # Maybe counter was reset to 0?
        print(row["ENTRIES"], row["PREV_ENTRIES"])
        counter = min(row["ENTRIES"], row["PREV_ENTRIES"])
    if counter > max_counter:
        # Check it again to make sure we're not still giving a counter that's too big
        return 0
    return counter

# If counter is > 1Million, then the counter might have been reset.
# Just set it to zero as different counters have different cycle limits
# It'd probably be a good idea to use a number even significantly smaller than 1 million as the limit!
turnstiles_daily["DAILY_ENTRIES"] = turnstiles_daily.apply(get_daily_counts, axis=1, max_counter=1000000)

turnstiles_daily.head(15)


# In[32]:


turnstiles_dailye = (turnstiles_df.groupby(["C/A", "UNIT", "SCP", "STATION", "DATE","TIME"],as_index=False).EXITS.first())
turnstiles_dailye[["PREV_DATE", "PREV_EXITS"]] = (turnstiles_dailye.groupby(["C/A", "UNIT", "SCP", "STATION"])["DATE", "EXITS"].apply(lambda grp: grp.shift(1)))
turnstiles_dailye.dropna(subset=["PREV_DATE"], axis=0, inplace=True)
turnstiles_dailye.dropna()
turnstiles_dailye[turnstiles_dailye["EXITS"] < turnstiles_dailye["PREV_EXITS"]].head()


# In[33]:


def get_daily_countsy(row, max_counter):
    counter = row["EXITS"] - row["PREV_EXITS"]
    if counter < 0:
        # Maybe counter is reversed?
        counter = -counter
    if counter > max_counter:
        # Maybe counter was reset to 0?
        print(row["EXITS"], row["PREV_EXITS"])
        counter = min(row["EXITS"], row["PREV_EXITS"])
    if counter > max_counter:
        # Check it again to make sure we're not still giving a counter that's too big
        return 0
    return counter

# If counter is > 1Million, then the counter might have been reset.
# Just set it to zero as different counters have different cycle limits
# It'd probably be a good idea to use a number even significantly smaller than 1 million as the limit!
turnstiles_dailye["DAILY_EXITS"] = turnstiles_dailye.apply(get_daily_countsy, axis=1, max_counter=1000000)


turnstiles_daily["DAILY_EXITS"]= turnstiles_dailye["DAILY_EXITS"]

turnstiles_daily


# In[34]:

#adding trafic and day columns
turnstiles_daily['TRAFIC'] = turnstiles_daily['DAILY_EXITS'] + turnstiles_daily['DAILY_ENTRIES']
turnstiles_daily["DATE_TIME"] = pd.to_datetime(turnstiles_daily.DATE + " " + turnstiles_daily.TIME,format="%m/%d/%Y %H:%M:%S")

turnstiles_daily['DAY']=turnstiles_daily.DATE_TIME.dt.day_name()

turnstiles_daily=turnstiles_daily[['C/A','UNIT','SCP','STATION','DATE','TIME','DATE_TIME','DAY','DAILY_ENTRIES','DAILY_EXITS','TRAFIC']]


# In[35]:

#top 10 crowded stations
turnstiles_stations = turnstiles_daily.groupby('STATION').mean().reset_index().sort_values('TRAFIC',ascending=False).head(15)
fig = px.bar(turnstiles_stations, x='STATION', y='TRAFIC',title="TOP CROWDED STATIONS", labels={'TRAFIC':'TRAFFIC (mean)'})
fig.show()


# In[36]:

#and 10 least crowded station
turnstiles_stations = turnstiles_daily.groupby('STATION').mean().reset_index().sort_values('TRAFIC',ascending=True).head(15)

fig = px.bar(turnstiles_stations, x='STATION', y='TRAFIC',title="LEAST CROWDED STATIONS", labels={'TRAFIC':'TRAFFIC (mean)'})
fig.show()


# In[37]:
#most crowded day for 75 AV
turnstile_OB =turnstiles_daily[turnstiles_daily['STATION']=='ORCHARD BEACH']
turnstile_OBb = turnstile_OB.groupby('DAY').mean().reset_index()
fig = px.bar(turnstile_OBb, x="DAY", y="TRAFIC",title="DAILY TRAFFIC LEAST CROWDED STATIONS", labels={'TRAFIC':'TRAFFIC (mean)'})
fig.show()


# In[38]:


#most crowded time for 75 AV
turnstile_OB=turnstile_OB.groupby("TIME").mean().sort_values('TIME',ascending=True).reset_index()
fig = px.line(turnstile_OB,x='TIME',y='TRAFIC',title="LEAST CROWDED STATIONS WITH RESPECT TO TIME", labels={'TRAFIC':'TRAFFIC (mean)'})
fig.show()
