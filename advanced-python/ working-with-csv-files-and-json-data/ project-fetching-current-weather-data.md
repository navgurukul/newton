```ngMeta
name:  project-fetching-current-weather-data
completionMethod: manual
```
# Project: Fetching Current Weather Data
Checking the weather seems fairly trivial: Open your web browser, click the address bar, type the URL to a weather website (or search for one and then click the link), wait for the page to load, look past all the ads, and so on.

Actually, there are a lot of boring steps you could skip if you had a program that downloaded the weather forecast for the next few days and printed it as plaintext. This program uses the requests module from Chapter 11 to download data from the Web.

Overall, the program does the following:

Reads the requested location from the command line.

Downloads JSON weather data from OpenWeatherMap.org.

Converts the string of JSON data to a Python data structure.

Prints the weather for today and the next two days.

So the code will need to do the following:

Join strings in sys.argv to get the location.

Call requests.get() to download the weather data.

Call json.loads() to convert the JSON data to a Python data structure.

Print the weather forecast.

For this project, open a new file editor window and save it as quickWeather.py.

# Step 1: Get Location from the Command Line Argument
The input for this program will come from the command line. Make quickWeather.py look like this:


	#! python3
	# quickWeather.py - Prints the weather for a location from the command line.

import json, requests, sys

	# Compute location from command line arguments.
if len(sys.argv) < 2:
    print('Usage: quickWeather.py location')
    sys.exit()
location = ' '.join(sys.argv[1:])

	# TODO: Download the JSON data from OpenWeatherMap.org's API.

	# TODO: Load JSON data into a Python variable.
In Python, command line arguments are stored in the sys.argv list. After the #! shebang line and import statements, the program will check that there is more than one command line argument. (Recall that sys.argv will always have at least one element, sys.argv[0], which contains the Python script’s filename.) If there is only one element in the list, then the user didn’t provide a location on the command line, and a “usage” message will be provided to the user before the program ends.

Command line arguments are split on spaces. The command line argument San Francisco, CA would make sys.argv hold ['quickWeather.py', 'San', 'Francisco,', 'CA']. Therefore, call the join() method to join all the strings except for the first in sys.argv. Store this joined string in a variable named location.

# Step 2: Download the JSON Data
OpenWeatherMap.org provides real-time weather information in JSON format. Your program simply has to download the page at <span><a href="http://api.openweathermap.org/data/2.5/forecast/daily?q=">http://api.openweathermap.org/data/2.5/forecast/daily?q=</a></span><Location>&cnt=3, where <Location> is the name of the city whose weather you want. Add the following to quickWeather.py.


`#! python3
`# quickWeather.py - Prints the weather for a location from the command line.

--snip--

	# Download the JSON data from OpenWeatherMap.org's API.

url =<span><a href="http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3'">http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3'</a></span> % (location)
response = requests.get(url)
response.raise_for_status()

	# TODO: Load JSON data into a Python variable.
We have location from our command line arguments. To make the URL we want to access, we use the %s placeholder and insert whatever string is stored in location into that spot in the URL string. We store the result in url and pass url to requests.get(). The requests.get() call returns a Response object, which you can check for errors by calling raise_for_status(). If no exception is raised, the downloaded text will be in response.text.

# Step 3: Load JSON Data and Print Weather
The response.text member variable holds a large string of JSON-formatted data. To convert this to a Python value, call the json.loads() function. The JSON data will look something like this:


{'city': {'coord': {'lat': 37.7771, 'lon': -122.42},
          'country': 'United States of America',
          'id': '5391959',
          'name': 'San Francisco',
          'population': 0},
'cnt': 3,
'cod': '200',
'list': [{'clouds': 0,
          'deg': 233,
          'dt': 1402344000,
          'humidity': 58,
          'pressure': 1012.23,
          'speed': 1.96,
          'temp': {'day': 302.29,
                   'eve': 296.46,
                   'max': 302.29,
                   'min': 289.77,
                   'morn': 294.59,
                   'night': 289.77},
          'weather': [{'description': 'sky is clear',
                       'icon': '01d',
--snip--
You can see this data by passing weatherData to pprint.pprint(). You may want to check <span><a href="http://openweathermap.org/">http://openweathermap.org/</a></span> for more documentation on what these fields mean. For example, the online documentation will tell you that the 302.29 after 'day' is the daytime temperature in Kelvin, not Celsius or Fahrenheit.

The weather descriptions you want are after 'main' and 'description'. To neatly print them out, add the following to quickWeather.py.


   ! python3
   # quickWeather.py - Prints the weather for a location from the command line.

   --snip--
```python
   # Load JSON data into a Python variable.
   weatherData = json.loads(response.text)
   # Print weather descriptions.
❶ w = weatherData['list']
   print('Current weather in %s:' % (location))
   print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
   print()
   print('Tomorrow:')
   print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
   print()
   print('Day after tomorrow:')
   print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
```
Notice how the code stores weatherData['list'] in the variable w to save you some typing ❶. You use w[0], w[1], and w[2] to retrieve the dictionaries for today, tomorrow, and the day after tomorrow’s weather, respectively. Each of these dictionaries has a 'weather' key, which contains a list value. You’re interested in the first list item, a nested dictionary with several more keys, at index 0. Here, we print the values stored in the 'main' and 'description' keys, separated by a hyphen.

When this program is run with the command line argument quickWeather.py San Francisco, CA, the output looks something like this:


Current weather in San Francisco, CA:
Clear - sky is clear

Tomorrow:
Clouds - few clouds

Day after tomorrow:
Clear - sky is clear
(The weather is one of the reasons I like living in San Francisco!)

Ideas for Similar Programs
Accessing weather data can form the basis for many types of programs. You can create similar programs to do the following:

Collect weather forecasts for several campsites or hiking trails to see which one will have the best weather.

Schedule a program to regularly check the weather and send you a frost alert if you need to move your plants indoors. (Chapter 15 covers scheduling, and Chapter 16 explains how to send email.)

Pull weather data from multiple sites to show all at once, or calculate and show the average of the multiple weather predictions.

# Summary
CSV and JSON are common plaintext formats for storing data. They are easy for programs to parse while still being human readable, so they are often used for simple spreadsheets or web app data. The csv and json modules greatly simplify the process of reading and writing to CSV and JSON files.

The last few chapters have taught you how to use Python to parse information from a wide variety of file formats. One common task is taking data from a variety of formats and parsing it for the particular information you need. These tasks are often specific to the point that commercial software is not optimally helpful. By writing your own scripts, you can make the computer handle large amounts of data presented in these formats.

In Chapter 15, you’ll break away from data formats and learn how to make your programs communicate with you by sending emails and text messages.