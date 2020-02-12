# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here

# Load the dataframe from the given path
data = pd.read_csv(path)

# rename the column name Total to Total_medals
data = data.rename(columns={'Total':'Total_Medals'})
print(data.head(10))


# --------------
#Code starts here

# creating the new dataframe with new coulmn Better_Event which stores the data of Summer and winter
data['Better_Event'] = np.where(data['Total_Summer'] > data['Total_Winter'] , 'Summer', 'Winter')

data['Better_Event'] =np.where(data['Total_Summer'] ==data['Total_Winter'],'Both',data['Better_Event'])

better_event = data['Better_Event'].value_counts().idxmax()
print('Name of better event with respect to all the performing countries : ',better_event)


# --------------
#Code starts here

# Create a new dataframe subset 
top_countries = data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]

# Drop the last row from 'top_countries'
top_countries = top_countries.drop([146])

# Create a function called 'top_ten' 
def top_ten(top_countries, col_name):
    country_list = []
    top_10 = top_countries.nlargest(10, col_name)
    country_list = top_10.loc[:, 'Country_Name']
    return country_list

# calling the fuction
top_10_summer = list(top_ten(top_countries, 'Total_Summer'))
top_10_winter = list(top_ten(top_countries, 'Total_Winter'))
top_10 = list(top_ten(top_countries, 'Total_Medals'))

common = list(set(top_10_summer) & set(top_10_winter) & set(top_10))
print('common elements : ',common)



# --------------
#Code starts here

# creating subset of dataframe based on the country names present in the list using isin() function on the column Country_Name
summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]

# ploingt a bar graph between the country name and total medal count according to the event 
plt.bar(summer_df['Country_Name'],summer_df['Total_Summer'])
plt.xlabel('Country_Name')
plt.ylabel('Total_Summer')
plt.xticks(rotation=45)
plt.show()

plt.bar(winter_df['Country_Name'],winter_df['Total_Summer'])
plt.xlabel('Country_Name')
plt.ylabel('Total_Summer')
plt.xticks(rotation=45)
plt.show()

plt.bar(top_df['Country_Name'],top_df['Total_Summer'])
plt.xlabel('Country_Name')
plt.ylabel('Total_Summer')
plt.xticks(rotation=45)
plt.show()
#print(summer_df)



# --------------
#Code starts here

# create a new column Golden_Ratio which is the quotient after dividing the two columns Gold_Summer and Total_Summer
summer_df['Golden_Ratio'] = summer_df['Gold_Summer'] / summer_df['Total_Summer']
summer_max_ratio = max(summer_df['Golden_Ratio']) 
summer_country_gold = summer_df.loc[summer_df['Golden_Ratio'].idxmax(),'Country_Name']
print(summer_max_ratio)
print(summer_country_gold)

# create a new column Golden_Ratio which is the quotient after dividing the two columns Gold_Winter and Total_Winter
winter_df['Golden_Ratio'] = winter_df['Gold_Winter'] / winter_df['Total_Winter']
winter_max_ratio = max(winter_df['Golden_Ratio']) 
winter_country_gold = winter_df.loc[winter_df['Golden_Ratio'].idxmax(),'Country_Name']
print(winter_max_ratio)
print(winter_country_gold)

top_df['Golden_Ratio'] = top_df['Gold_Total'] / top_df['Total_Medals']
top_max_ratio = max(top_df['Golden_Ratio']) 
top_country_gold = top_df.loc[top_df['Golden_Ratio'].idxmax(),'Country_Name']
print(top_max_ratio)
print(top_country_gold)



# --------------
#Code starts here

# Drop the last row from the dataframe(
data_1 = data.iloc[:-1, :]
data_1['Total_Points'] = (data_1['Gold_Total'] * 3)+(data_1['Silver_Total'] * 2)+(data_1['Bronze_Total'])
most_points = max(data_1['Total_Points'])
best_country = data_1.loc[data_1['Total_Points'].idxmax(),'Country_Name']
print('Max Value : ',most_points)
print('The country assosciated with Max Value : ',best_country)



# --------------
#Code starts here

best = data[(data['Country_Name'] == best_country)]
best = best[['Gold_Total','Silver_Total','Bronze_Total']].copy()

best.plot(kind='bar', stacked=True, figsize=(15,10))
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)
plt.show()


