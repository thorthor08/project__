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
    
    for i in range(len(wind_speed)):
        info_list.append([wind_speed[i], gust_speed[i],angles[i]])
    print(len(info_list))
    print(info_list)
    
    new_dates=new_dates[0:len(info_list)]
    print(len(new_dates))
    for i in range(len(new_dates)):
            if new_dates[i][1] not in final_wind_data.keys():
                final_wind_data[new_dates[i][1]] = {}
            final_wind_data[new_dates[i][1]][new_dates[i][0]] = info_list[i]        
    


    html_content = home_page(final_wind_data).format(
        day1=list(final_wind_data.keys())[0],
        day2=list(final_wind_data.keys())[1],
        day3=list(final_wind_data.keys())[2],
        day4=list(final_wind_data.keys())[3],
        day5=list(final_wind_data.keys())[4],
        day6=list(final_wind_data.keys())[5],
        day7=list(final_wind_data.keys())[6]
    )

    html_file_path = 'home_page.html'
    with open(html_file_path, 'w', encoding='utf-8') as file:
        file.write(html_content)

    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    if os.path.exists(html_file_path):
        webbrowser.get(chrome_path).open('file://' + os.path.realpath(html_file_path))
    else:
        print("Error: HTML file does not exist.")

    print(final_wind_data)

if __name__ == "__main__":
    main()
