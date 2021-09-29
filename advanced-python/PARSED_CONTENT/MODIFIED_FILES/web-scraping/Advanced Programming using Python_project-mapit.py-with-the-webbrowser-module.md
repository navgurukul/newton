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


project-mapit_key16


project-mapit_key17
project-mapit_key18



    #! python3
    # mapIt.py - Launches a map in the browser using an address from the
    # command line or clipboard.
```python
import webbrowser, sys
if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
```

project-mapit_key19
project-mapit_key20


project-mapit_key21


project-mapit_key22



project-mapit_key23



project-mapit_key24


project-mapit_key25
project-mapit_key26



project-mapit_key27
project-mapit_key28
project-mapit_key29
project-mapit_key30
```python
else:
    # Get address from clipboard.
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
```
project-mapit_key31


project-mapit_key32


project-mapit_key33


project-mapit_key34


project-mapit_key35


project-mapit_key36


project-mapit_key37


project-mapit_key38


project-mapit_key39


project-mapit_key40


project-mapit_key41


project-mapit_key42


 
project-mapit_key43


 
project-mapit_key44


 
project-mapit_key45


 
project-mapit_key46
