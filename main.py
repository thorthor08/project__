import pandas as pd
import streamlit as st
import data_scraper

# Read data from files with utf-8 encoding
with open('dates.txt', 'r', encoding='utf-8') as file:
    dates = file.readlines()
dates = [date.strip() for date in dates]

with open('wind_speed_gust.txt', 'r', encoding='utf-8') as file:
    data = file.readlines()

with open('angles.txt', 'r', encoding='utf-8') as file:
    angles = file.readlines()

with open('temp.txt', 'r', encoding='utf-8') as file:
    temp = file.readlines()

with open('waves.txt', 'r', encoding='utf-8') as file:
    waves = file.readlines()

with open('hours.txt', 'r', encoding='utf-8') as file:
    hours = file.readlines()

# Process data for wind data
angles_values = []
temp_values = []
for i in angles:
    angles_values.append(i)
for i in temp:
    temp_values.append(i + "°")

speed_values = data[0].split(" ")
gust_values = data[1].split(" ")
if len(dates) > len(speed_values):
    dates = dates[:len(speed_values)]
elif len(dates) < len(speed_values):
    dates += [''] * (len(speed_values) - len(dates))
if len(angles_values) > len(speed_values):
    angles_values = angles_values[:len(speed_values)]
elif len(angles_values) < len(speed_values):
    angles_values += [''] * (len(speed_values) - len(angles_values))
if len(temp_values) > len(speed_values):
    temp_values = temp_values[:len(speed_values)]
elif len(temp_values) < len(speed_values):
    temp_values += [''] * (len(speed_values) - len(temp_values))
if len(gust_values) > len(speed_values):
    gust_values = gust_values[:len(speed_values)]
elif len(gust_values) < len(speed_values):
    gust_values += [''] * (len(speed_values) - len(gust_values))

# Process data for wave data
hours = [hour.strip() for hour in hours]
waves = [wave.strip() for wave in waves]

# Main function to run the Streamlit app
def main():
    st.title("Thor Wind Website")

    with st.spinner("Loading data..."):
        import data_scraper

    # Create DataFrame for wind data
    wind_df = pd.DataFrame({
        'Date': dates,
        'Speed': speed_values,
        'Gust': gust_values,
        'Angle': angles_values,
        'Temperature': temp_values
    })

    # Create DataFrame for wave data
    wave_df = pd.DataFrame({
        'Hour': hours,
        'Wave': waves
    })

    # Create a list from the first item in each row and split each item
    dates_list = []
    final_wind_data={}
    for i in range(wind_df.shape[0]):
        row = wind_df.iloc[i]
        dates_list.append(row['Date'].split(" "))

    info_list = []
    for i in range(wind_df.shape[0]):
        row = wind_df.iloc[i]
        info_list.append([row['Speed'], row["Gust"], row["Angle"]])

    for date in dates_list:
        if date[1] not in final_wind_data.keys():
            final_wind_data[date[1]] = {}
        final_wind_data[date[1]][date[0]] = {}

    for i in info_list:
        j = 0
        while len(final_wind_data[dates_list[j][1]]) >= i:












    # Display data in tables
    st.header("Wind Data")
    st.table(wind_df)

    st.header("Wave Data")
    st.table(wave_df)

    # Display the dates_list
    st.write(final_wind_data)
    st.write(info_list)


if __name__ == "__main__":
    main()
