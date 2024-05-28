import pandas as pd
import webbrowser
import os

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file.readlines()]

def process_wind_data(dates, data, angles, temp):
    angles_values = [angle.strip() for angle in angles]
    temp_values = [t.strip() + "°" for t in temp]

def home_page(final_wind_data):
    html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Expanding Navbar</title>
    <style>
        body, html {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Arial', sans-serif;
        }}
        #navbar {{
            position: fixed;
            top: 0;
            width: 100%;
            background-color: #00bcd4;
            color: white;
            transition: height 0.5s ease, background-color 0.5s ease;
            overflow: hidden;
            border-radius: 0 0 10px 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }}
        #navbar.compact {{
            height: 20vh;
        }}
        #navbar.expanded {{
            height: 100vh;
        }}
        .nav-content {{
            display: grid;
            grid-template-columns: 8% repeat(4, 23%);
            gap: 2px;
            height: 100%;
        }}
        .category, .data {{
            border: 1px solid white;
            padding: 10px;
            text-align: center;
            border-radius: 5px;
            background-color: rgba(255, 255, 255, 0.2);
        }}
        .data.hidden {{
            display: none;
        }}
        #toggleButton {{
            position: absolute;
            right: 10px;
            bottom: 10px;
            width: 30px;
            height: 30px;
            background: white;
            border: none;
            border-radius: 50%;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            cursor: pointer;
            transition: transform 0.3s ease, background-color 0.3s ease, bottom 0.5s ease;
            padding: 0;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        #toggleButton.expanded {{
            transform: rotate(180deg);
            bottom: 10px;
        }}
        #toggleButton img {{
            width: 15px;
            height: 15px;
        }}
        @media (max-width: 768px) {{
            .nav-content {{
                grid-template-columns: 20% repeat(2, 40%);
            }}
        }}
        @media (max-width: 480px) {{
            .nav-content {{
                grid-template-columns: 30% 70%;
            }}
        }}
    </style>
</head>
<body>
    <nav id="navbar" class="compact">
        <div class="nav-content">
            <div class="category">Day</div>
            <div class="category">Wind Speed</div>
            <div class="category">Waves</div>
            <div class="category">Temperature</div>
            <div class="category">Activity</div>
            <div class="data">{day1}</div>
            <div class="data">10 km/h</div>
            <div class="data">3 ft</div>
            <div class="data">20°C</div>
            <div class="data">Running</div>
            <div class="data hidden">{day2}</div>
            <div class="data hidden">15 km/h</div>
            <div class="data hidden">2 ft</div>
            <div class="data hidden">22°C</div>
            <div class="data hidden">Swimming</div>
            <div class="data hidden">{day3}</div>
            <div class="data hidden">5 km/h</div>
            <div class="data hidden">1 ft</div>
            <div class="data hidden">18°C</div>
            <div class="data hidden">Walking</div>
            <div class="data hidden">{day4}</div>
            <div class="data hidden">20 km/h</div>
            <div class="data hidden">4 ft</div>
            <div class="data hidden">25°C</div>
            <div class="data hidden">Cycling</div>
            <div class="data hidden">{day5}</div>
            <div class="data hidden">12 km/h</div>
            <div class="data hidden">2 ft</div>
            <div class="data hidden">19°C</div>
            <div class="data hidden">Hiking</div>
            <div class="data hidden">{day6}</div>
            <div class="data hidden">8 km/h</div>
            <div class="data hidden">3 ft</div>
            <div class="data hidden">21°C</div>
            <div class="data hidden">Surfing</div>
            <div class="data hidden">{day7}</div>
            <div class="data hidden">14 km/h</div>
            <div class="data hidden">5 ft</div>
            <div class="data hidden">23°C</div>
            <div class="data hidden">Fishing</div>
            <div class="data hidden">{day8}</div>
            <div class="data hidden">14 km/h</div>
            <div class="data hidden">5 ft</div>
            <div class="data hidden">23°C</div>
            <div class="data hidden">Fishing</div>
            <div class="data hidden">{day9}</div>
            <div class="data hidden">14 km/h</div>
            <div class="data hidden">5 ft</div>
            <div class="data hidden">23°C</div>
            <div class="data hidden">Fishing</div>
            <div class="data hidden">{day10}</div>
            <div class="data hidden">14 km/h</div>
            <div class="data hidden">5 ft</div>
            <div class="data hidden">23°C</div>
            <div class="data hidden">Fishing</div>
        </div>
        <button id="toggleButton">
            <img src="C:\\Users\\Magsihim_AI\\Pictures\\arrow.png" alt="Toggle">
        </button>
    </nav>
    <script>
        document.addEventListener('DOMContentLoaded', function() {{
            const navbar = document.getElementById('navbar');
            const toggleButton = document.getElementById('toggleButton');
            const hiddenDataElements = document.querySelectorAll('.data.hidden');
            toggleButton.addEventListener('click', function() {{
                if (navbar.classList.contains('compact')) {{
                    navbar.classList.remove('compact');
                    navbar.classList.add('expanded');
                    toggleButton.classList.add('expanded');
                    hiddenDataElements.forEach(el => el.style.display = 'block');
                }} else {{
                    navbar.classList.remove('expanded');
                    navbar.classList.add('compact');
                    toggleButton.classList.remove('expanded');
                    hiddenDataElements.forEach(el => el.style.display = 'none');
                }}
            }});
        }});
    </script>
</body>
</html>
    """
    return html_content

def main():
    dates = read_file('dates.txt')
    data = read_file('wind_speed_gust.txt')
    angles = read_file('angles.txt')
    temp = read_file('temp.txt')
    waves = read_file('waves.txt')
    hours = read_file('hours.txt')
    new_dates = []
    final_wind_data = {}
    info_list = []
    ten_days = []

    #make a list of dates where each value contains of hour, day and date
    for i in dates:
        new_dates.append(i.split())
        
    wind_speed=data[0].split()
    gust_speed=data[1].split()
    
    for i in range(len(new_dates)):
        if "h" in new_dates[i][0]:
            new_dates[i][0] = new_dates[i][0].replace("h", "")
        if new_dates[i][0].startswith("0"):
            new_dates[i][0] = new_dates[i][0].lstrip("0")
        if new_dates[i][0].isdigit():
            new_dates[i][0] = int(new_dates[i][0])
    print(len(new_dates))
    
    #creates a list where each value contains the wind speed, gust speed, and angle
    for i in range(len(wind_speed)):
        info_list.append([wind_speed[i], gust_speed[i],angles[i]])
    
    #take the first ten days from new_dates
    count=0
    ten_days=[]
    for i in range(len(new_dates)):
        if i+1 < len(new_dates) and new_dates[i+1][1]!=new_dates[i][1]:
            count+=1
        ten_days.append(new_dates[i])
        if count==10:
            ten_days.append(new_dates[i+1])
            break
    print(len(ten_days))
    
    switch_days=[]
    for i in range(len(ten_days)-1):
        if ten_days[i][1] != ten_days[i+1][1]:
            switch_days.append(i)
    print(switch_days)
    
    for i in switch_days:
        ten_days[i+1][1]=ten_days[i][1]

    #shorten the info list to the length of the ten_days list
    info_list=info_list[:len(ten_days)]    
        
    for i in range(len(ten_days)):
        if ten_days[i][1] =="Mo":
            ten_days[i][1]="Monday"
        elif ten_days[i][1] =="Tu":
            ten_days[i][1]="Tuesday"
        elif ten_days[i][1] =="We":
            ten_days[i][1]="Wednesday"
        elif ten_days[i][1] =="Th":
            ten_days[i][1]="Thursday"
        elif ten_days[i][1] =="Fr":
            ten_days[i][1]="Friday"
        elif ten_days[i][1] =="Sa":
            ten_days[i][1]="Saturday"
        elif ten_days[i][1] =="Su":
            ten_days[i][1]="Sunday"
            
    
    #seperate ten days into individual days
    for i in range(len(ten_days) - 1):  # Subtract 1 to prevent IndexError
        if ten_days[i+1][1] != ten_days[i][1]:
            if ten_days[i][1] not in final_wind_data:
                final_wind_data[ten_days[i][1]+" "+ten_days[i][2]] = []
    final_wind_data[ten_days[-1][1]+" "+ten_days[-1][2]] = []

    hours=[]
    for i in ten_days:
        hours.append(i[0])
        
    def split_list_by_indexes(main_list, indexes):
    # Sort the indexes to ensure they are in ascending order
        sorted_indexes = sorted(indexes)
    
    # Initialize the list to store the sublists
        sublists = []
    
        previous_index = 0
    
        for index in sorted_indexes:
            sublists.append(main_list[previous_index:index+2])
            previous_index = index+2
    
        sublists.append(main_list[previous_index:])
    
        return sublists
    
    result = split_list_by_indexes(hours, switch_days)
    result_info = split_list_by_indexes(info_list, switch_days)

    print("this is the result")
    print(result)
    
    for i in range(len(result)):
        for j in range(len(result[i])):
            result[i][j]=[result[i][j],result_info[i][j][0],result_info[i][j][1],result_info[i][j][2]] 
    print("this is the result")
    print(result)       
    
    #adds the list of hours and data into final wind data
    for i in range(len(result)):
        for j in range(len(result[i])):
            final_wind_data[list(final_wind_data.keys())[i]].append(result[i][j])


    
    print("this is the final wind data")
    print(final_wind_data)
    #print("this is the info list")
    #print(info_list)
    #print(len(info_list))
    #print("this is the ten days")
    #print(final_wind_data)
    #print(len(final_wind_data))
        
        
    html_content = home_page(final_wind_data).format(
        day1=list(final_wind_data.keys())[0],
        day2=list(final_wind_data.keys())[1],
        day3=list(final_wind_data.keys())[2],
        day4=list(final_wind_data.keys())[3],
        day5=list(final_wind_data.keys())[4],
        day6=list(final_wind_data.keys())[5],
        day7=list(final_wind_data.keys())[6],
        day8=list(final_wind_data.keys())[7],
        day9=list(final_wind_data.keys())[8],
        day10=list(final_wind_data.keys())[9]
)  

    html_file_path = 'home_page.html'
    with open(html_file_path, 'w', encoding='utf-8') as file:
        file.write(html_content)

    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    if os.path.exists(html_file_path):
        webbrowser.get(chrome_path).open('file://' + os.path.realpath(html_file_path))
    else:
        print("Error: HTML file does not exist.")


if __name__ == "__main__":
    main()
