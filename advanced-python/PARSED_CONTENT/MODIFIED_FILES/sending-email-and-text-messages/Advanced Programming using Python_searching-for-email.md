searching-for-email_key1
searching-for-email_key2


searching-for-email_key3
searching-for-email_key4


```python
>>> import pprint
>>> pprint.pprint(imapObj.list_folders())
```
searching-for-email_key5


searching-for-email_key6


searching-for-email_key7


searching-for-email_key8


searching-for-email_key9


```python
>>> imapObj.select_folder('INBOX', readonly=True)
```
searching-for-email_key10


searching-for-email_key11


searching-for-email_key12
searching-for-email_key13


searching-for-email_key14


searching-for-email_key15


searching-for-email_key16


searching-for-email_key17


searching-for-email_key18


searching-for-email_key19


searching-for-email_key20


searching-for-email_key21


searching-for-email_key22


searching-for-email_key23


searching-for-email_key24


searching-for-email_key25


searching-for-email_key26


searching-for-email_key27


searching-for-email_key28


searching-for-email_key29


searching-for-email_key30


searching-for-email_key31


searching-for-email_key32


searching-for-email_key33


searching-for-email_key34


searching-for-email_key35


searching-for-email_key36


searching-for-email_key37


searching-for-email_key38


searching-for-email_key39


searching-for-email_key40


searching-for-email_key41


searching-for-email_key42


searching-for-email_key43


searching-for-email_key44


searching-for-email_key45


searching-for-email_key46


searching-for-email_key47


searching-for-email_key48


searching-for-email_key49
searching-for-email_key50
searching-for-email_key51
searching-for-email_key52
searching-for-email_key53
searching-for-email_key54
searching-for-email_key55
searching-for-email_key56
searching-for-email_key57
searching-for-email_key58
searching-for-email_key59
searching-for-email_key60
searching-for-email_key61
searching-for-email_key62
searching-for-email_key63
searching-for-email_key64
searching-for-email_key65
searching-for-email_key66
searching-for-email_key67
[searching-for-email_key68](mailto:&#x62;&#111;&#98;&#x40;&#101;&#x78;&#x61;&#x6d;&#112;&#108;&#101;&#46;&#x63;&#x6f;&#109;)
searching-for-email_key69


searching-for-email_key70


searching-for-email_key71


searching-for-email_key72


```python
>>> UIDs = imapObj.search(['SINCE 05-Jul-2015'])
>>> UIDs
```
searching-for-email_key73


searching-for-email_key74
searching-for-email_key75


searching-for-email_key76


```python
>>> import imaplib
>>> imaplib._MAXLINE = 10000000
```
searching-for-email_key77


searching-for-email_key78


searching-for-email_key79


![image](assets/000087.jpg)
searching-for-email_key80


searching-for-email_key81


```python
>>> UIDs = imapObj.gmail_search('meaning of life')
>>> UIDs
```
searching-for-email_key82
