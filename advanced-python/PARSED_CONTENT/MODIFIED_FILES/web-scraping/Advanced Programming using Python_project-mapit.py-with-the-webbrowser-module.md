project-mapit_key1
project-mapit_key2


```python
>>> import webbrowser
>>> webbrowser.open('http://inventwithpython.com/')
```
project-mapit_key3


project-mapit_key4


project-mapit_key5


project-mapit_key6


project-mapit_key7


project-mapit_key8


project-mapit_key9


project-mapit_key10


project-mapit_key11


project-mapit_key12
project-mapit_key13



project-mapit_key14


project-mapit_key15
[project-mapit_key16](http://maps.google.com/)
project-mapit_key17
[project-mapit_key18](https://www.google.com/maps/place/870+Valencia+St/@37.7590311,-122.4215096,17z/data=!3m1!4b1!4m2!3m1!1s0x808f7e3dadc07a37:0xc86b0b2bb93b73d8)
project-mapit_key19


project-mapit_key20
[project-mapit_key21](https://www.google.com/maps/place/870+Valencia+St+San+Francisco+CA/)
project-mapit_key22
[project-mapit_key23](https://www.google.com/maps/place/your_address_string&#39;)
project-mapit_key24


project-mapit_key25
project-mapit_key26



    #! python3
    # mapIt.py - Launches a map in the browser using an address from the
    # command line or clipboard.
```python
import webbrowser, sys
if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
```

project-mapit_key27
project-mapit_key28


project-mapit_key29


project-mapit_key30



project-mapit_key31



project-mapit_key32


project-mapit_key33
project-mapit_key34



project-mapit_key35
project-mapit_key36
project-mapit_key37
project-mapit_key38
```python
else:
    # Get address from clipboard.
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
```
project-mapit_key39


project-mapit_key40


project-mapit_key41


project-mapit_key42


project-mapit_key43


project-mapit_key44


project-mapit_key45


project-mapit_key46


project-mapit_key47


project-mapit_key48


project-mapit_key49


project-mapit_key50


 
project-mapit_key51


 
project-mapit_key52


 
project-mapit_key53


 
project-mapit_key54
