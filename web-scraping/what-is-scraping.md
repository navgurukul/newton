```ngMeta
name: What is Scraping?
```

# Introduction

How can we scrape in Python?
- HTML is rendered by browsers. But we can get the same HTML in Python using requests. Show how to install requests.
- Print the same HTML in the Terminal which you got.
- Install BeautifulSoup and show how we can get the title and a few other tags to give a basic glimpse into BeautifulSoup of a page using Beautiful Soup?

# Packages need to Scrape Data and why we use them
What is pip?
- Hum pip ko install iss liye krte hai because it is a package management system jisse ki help karta hai python ke Module ko - install karne main.
- pip is a package management system used to install and manage software packages written in Python.

Why we use module requests?
- Hum yha moduale requesta ka use is liye krte hai ki hum jis web page ko scrape kr rhe hai to requests humko ek sample data collect kr dega.
- we use import the Requests module so that we can collect a sample web page:

Why we use pip install beautifulsoup4?
- Beautifulsoup4 yeh ek python package hai jo ki HTML and xml Document ko parse prta hai
- Beautiful Soup is a Python package for parsing HTML and XML documents.

how to install these packages
Use only python3
```
   $ sudo apt-get install python3-pip
   $ pip3 install requests Or pip3 --user requests
   $ pip3 install beautifulsoup4
   
```

@[youtube](https://youtu.be/9sG87-w7wVQ)

**Created by Naresh Kumar Gautam (naresh18@navgurukul.org)**

# Let's start
Sabse phle humko [some important things](https://www.pythonforbeginners.com/beautifulsoup/beautifulsoup-4-python) ke bare main pata hona chahiye.

@[youtube](https://youtu.be/3lPijXMLF6U)

**Created by Naresh Kumar Gautam (naresh18@navgurukul.org)**
 
```
Step 1. import requests
Step 2. URL = "Yha per apka url hoga jis bhi web page ko aap scrape karna chahte ho"
Step 3. sample = requests.get(URL)
Step 4. from bs4 import BeautifulSoup
Step 5. soup = BeautifulSoup(sample.text,"html.parser") # iss object ke throw hum kahi bhi khel sakte hai
Step 6. Title = soup.title

print(Title)#ye apke web page ka title print karega
```
Ab aap yha se scraping start karenge ..............


