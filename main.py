import pandas as pd
import webbrowser
import os

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
angles_values = [angle.strip() for angle in angles]
temp_values = [temp.strip() + "°" for temp in temp]

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


# Create DataFrame for wind data
wind_df = pd.DataFrame({
    'Date': dates,
    'Speed': speed_values,
    'Gust': gust_values,
    'Angle': angles_values,
    'Temperature': temp_values
})

# Process data for wave data
hours = [hour.strip() for hour in hours]
waves = [wave.strip() for wave in waves]

# Create DataFrame for wave data
wave_df = pd.DataFrame({
    'Hour': hours,
    'Wave': waves
})

def main():
    # Create a list from the first item in each row and split each item
    dates_list = []
    final_wind_data = {}
    #wind_df['hour']=wind_df.Date.str.split(' ')[0].
    for i in range(wind_df.shape[0]):
        row = wind_df.iloc[i]
        dates_list.append(row['Date'].split(" "))

    info_list = []
    for i in range(wind_df.shape[0]):
        row = wind_df.iloc[i]
        info_list.append([row['Speed'], row["Gust"], row["Angle"]])
    for i in range(len(dates_list)):
        dates_list[i][0]=dates_list[i][0]
    for date in range(len(dates_list)):
        if dates_list[date][1] not in final_wind_data.keys():
            final_wind_data[dates_list[date][1]] = {}
        final_wind_data[dates_list[date][1]][dates_list[date][0]] = info_list[date]

    # Opening the HTML file in the default web browser
    html_file_path = r'C:\Users\Magsihim_AI\Documents\GitHub\project__\home_page.html'  # Use a raw string
    if os.path.exists(html_file_path):
        webbrowser.open('file://' + os.path.realpath(html_file_path))
    else:
        print("Error: HTML file does not exist.")

if __name__ == "__main__":
    main()




