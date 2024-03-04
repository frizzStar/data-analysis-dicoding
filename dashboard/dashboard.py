import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import os

st.set_option('deprecation.showPyplotGlobalUse', False)

current_dir = os.path.dirname(__file__)
csv_file_path = os.path.join(current_dir, 'main.csv')

df = pd.read_csv(csv_file_path)

with st.sidebar:
  st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
  st.write("Fahriza Gymnastiar L")

st.header('Bike Rentals Dashboard :sparkles:')
st.write('By: Fahriza Gymnastiar L')


st.subheader('\n1. Average Bike Rental on Different Weather Condition')

col1, col2 = st.columns(2)

with col1:
  total_hour = str(round(df.cnt.sum(), 2)) + (" hours")
  st.metric("Total hours", value=total_hour)

with col2:
  total_days = str(round((df.cnt.sum())/24)) + (" days")
  st.metric("Total days", value=total_days)

weather_group_df = df.groupby('weathersit')[['cnt']].mean()

label = ['Clear', 'Cloudy', 'Light Rain', 'Heavy Rain']

weather_group_df.plot(kind='bar')
# plt.title('Average Bike Rentals by Weather Condition')
plt.xlabel(None)
plt.ylabel('Average Total Rentals (Hours)')
plt.xticks(weather_group_df.index -1, label, rotation=0)
st.pyplot()

st.write("The graph illustrates that the average number of bike rental users tends to be higher during clear weather conditions compared to cloudy, light rain, or heavy rain conditions. This suggests a correlation between weather conditions and bike rental demand, with clearer weather being associated with increased usage.")

st.subheader("\n2. Average Bike Rental on Weekend Compared to Weekdays")

columns = st.columns([1])
total_weeks = str(round(((df.cnt.sum())/24)/7)) + " weeks"
columns[0].metric("Total Weeks", value=total_weeks)

sum_df = df.groupby('workingday')[['cnt']].mean()
def adjusted_total(row):
    if row.name == 1:
        row['cnt'] /= 5
    else:
        row['cnt'] /= 2
    return row

adjusted_total_df = sum_df.apply(adjusted_total, axis=1)

adjusted_total_df.plot(kind='bar', legend=None)

plt.ylabel('Average Total Rentals (hours)')
plt.xlabel(None)
plt.xticks([0, 1], ['Weekend', 'Weekday'], rotation=0)
st.pyplot()

st.write("The depicted graph reveals a notable trend: the average number of bike rental users significantly surges during weekends, presenting a stark contrast to the subdued usage observed on weekdays. This pattern suggests a discernible preference among users to engage in biking activities during their leisure time, particularly on Saturdays and Sundays")