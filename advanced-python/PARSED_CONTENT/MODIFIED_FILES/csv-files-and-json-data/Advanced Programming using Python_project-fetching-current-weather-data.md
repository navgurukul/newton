project-fetching-current-weather-data_key1
project-fetching-current-weather-data_key2


project-fetching-current-weather-data_key3


project-fetching-current-weather-data_key4


project-fetching-current-weather-data_key5


project-fetching-current-weather-data_key6


project-fetching-current-weather-data_key7


project-fetching-current-weather-data_key8


project-fetching-current-weather-data_key9


project-fetching-current-weather-data_key10


project-fetching-current-weather-data_key11


project-fetching-current-weather-data_key12


project-fetching-current-weather-data_key13


project-fetching-current-weather-data_key14


project-fetching-current-weather-data_key15
project-fetching-current-weather-data_key16



    #! python3
    # quickWeather.py - Prints the weather for a location from the command line.

project-fetching-current-weather-data_key17


    # Compute location from command line arguments.
project-fetching-current-weather-data_key18


    # TODO: Download the JSON data from OpenWeatherMap.org's API.

    # TODO: Load JSON data into a Python variable.
project-fetching-current-weather-data_key19


project-fetching-current-weather-data_key20


project-fetching-current-weather-data_key21
project-fetching-current-weather-data_key22



project-fetching-current-weather-data_key23


project-fetching-current-weather-data_key24


    # Download the JSON data from OpenWeatherMap.org's API.

project-fetching-current-weather-data_key25


    # TODO: Load JSON data into a Python variable.
project-fetching-current-weather-data_key26


project-fetching-current-weather-data_key27
project-fetching-current-weather-data_key28



project-fetching-current-weather-data_key29


project-fetching-current-weather-data_key30



project-fetching-current-weather-data_key31
project-fetching-current-weather-data_key32
project-fetching-current-weather-data_key33
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
project-fetching-current-weather-data_key34


project-fetching-current-weather-data_key35



project-fetching-current-weather-data_key36


project-fetching-current-weather-data_key37


project-fetching-current-weather-data_key38


project-fetching-current-weather-data_key39


project-fetching-current-weather-data_key40


project-fetching-current-weather-data_key41


project-fetching-current-weather-data_key42


project-fetching-current-weather-data_key43
project-fetching-current-weather-data_key44


project-fetching-current-weather-data_key45


project-fetching-current-weather-data_key46
