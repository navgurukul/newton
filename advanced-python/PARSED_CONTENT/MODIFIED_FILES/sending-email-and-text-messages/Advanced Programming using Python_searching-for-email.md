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


```python
>>> UIDs = imapObj.search(['SINCE 05-Jul-2015'])
>>> UIDs
```
searching-for-email_key53


searching-for-email_key54
searching-for-email_key55


searching-for-email_key56


```python
>>> import imaplib
>>> imaplib._MAXLINE = 10000000
```
searching-for-email_key57


searching-for-email_key58


searching-for-email_key59


![image](assets/000087.jpg)
searching-for-email_key60


searching-for-email_key61


```python
>>> UIDs = imapObj.gmail_search('meaning of life')
>>> UIDs
```
searching-for-email_key62
