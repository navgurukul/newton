what-is-scraping_key1
what-is-scraping_key2
- what-is-scraping_key3
- what-is-scraping_key4
- what-is-scraping_key5
what-is-scraping_key6
what-is-scraping_key7
- what-is-scraping_key8
- what-is-scraping_key9
what-is-scraping_key10
- what-is-scraping_key11
- what-is-scraping_key12
what-is-scraping_key13
- what-is-scraping_key14
- what-is-scraping_key15
what-is-scraping_key16
```
   $ sudo apt-get install python3-pip
   $ pip3 install requests Or pip3 --user requests
   $ pip3 install beautifulsoup4
   
```
@[youtube](https://youtu.be/9sG87-w7wVQ)

what-is-scraping_key17


what-is-scraping_key18
what-is-scraping_key19[what-is-scraping_key20](https://www.pythonforbeginners.com/beautifulsoup/beautifulsoup-4-python)
what-is-scraping_key21

@[youtube](https://youtu.be/3lPijXMLF6U)

what-is-scraping_key22

 
```
Step 1. import requests
Step 2. URL = "Yha per apka url hoga jis bhi web page ko aap scrape karna chahte ho"
Step 3. sample = requests.get(URL)
Step 4. from bs4 import BeautifulSoup
Step 5. soup = BeautifulSoup(sample.text,"html.parser") # iss object ke throw hum kahi bhi khel sakte hai
Step 6. Title = soup.title

print(Title)#ye apke web page ka title print karega
```
what-is-scraping_key23
