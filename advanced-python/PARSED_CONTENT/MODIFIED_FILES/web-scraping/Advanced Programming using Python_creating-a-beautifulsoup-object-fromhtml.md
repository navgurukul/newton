```ngMeta
creating-a-beautifulsoup-object-fromhtml_key1
```

creating-a-beautifulsoup-object-fromhtml_key2
creating-a-beautifulsoup-object-fromhtml_key3


```python
>>> import requests, bs4
>>> res = requests.get('http://nostarch.com')
>>> res.raise_for_status()
>>> noStarchSoup = bs4.BeautifulSoup(res.text)
>>> type(noStarchSoup)
```
creating-a-beautifulsoup-object-fromhtml_key4


creating-a-beautifulsoup-object-fromhtml_key5


```python
>>> exampleFile = open('example.html')
>>> exampleSoup = bs4.BeautifulSoup(exampleFile)
>>> type(exampleSoup)
```
creating-a-beautifulsoup-object-fromhtml_key6


creating-a-beautifulsoup-object-fromhtml_key7
creating-a-beautifulsoup-object-fromhtml_key8


creating-a-beautifulsoup-object-fromhtml_key9


creating-a-beautifulsoup-object-fromhtml_key10


creating-a-beautifulsoup-object-fromhtml_key11


creating-a-beautifulsoup-object-fromhtml_key12


creating-a-beautifulsoup-object-fromhtml_key13


creating-a-beautifulsoup-object-fromhtml_key14


creating-a-beautifulsoup-object-fromhtml_key15


creating-a-beautifulsoup-object-fromhtml_key16


creating-a-beautifulsoup-object-fromhtml_key17


creating-a-beautifulsoup-object-fromhtml_key18


creating-a-beautifulsoup-object-fromhtml_key19


creating-a-beautifulsoup-object-fromhtml_key20


creating-a-beautifulsoup-object-fromhtml_key21


```python
>>> import bs4
>>> exampleFile = open('example.html')
>>> exampleSoup = bs4.BeautifulSoup(exampleFile.read())
>>> elems = exampleSoup.select('#author')
>>> type(elems)
```
creating-a-beautifulsoup-object-fromhtml_key22
```python
>>> len(elems)
```
creating-a-beautifulsoup-object-fromhtml_key23
```python
>>> type(elems[0])
```
creating-a-beautifulsoup-object-fromhtml_key24
```
>>> elems[0].getText()
```
creating-a-beautifulsoup-object-fromhtml_key25
```
>>> str(elems[0])
```
creating-a-beautifulsoup-object-fromhtml_key26
```python
>>> elems[0].attrs
```
creating-a-beautifulsoup-object-fromhtml_key27


creating-a-beautifulsoup-object-fromhtml_key28


creating-a-beautifulsoup-object-fromhtml_key29


```python
>>> pElems = exampleSoup.select('p')
>>> str(pElems[0])
```
creating-a-beautifulsoup-object-fromhtml_key30
```python
>>> pElems[0].getText()
```
creating-a-beautifulsoup-object-fromhtml_key31
```python
>>> str(pElems[1])
```
creating-a-beautifulsoup-object-fromhtml_key32
```python
>>> pElems[1].getText()
```
creating-a-beautifulsoup-object-fromhtml_key33
```python
>>> str(pElems[2])
```
creating-a-beautifulsoup-object-fromhtml_key34
```python
>>> pElems[2].getText()
```
creating-a-beautifulsoup-object-fromhtml_key35
creating-a-beautifulsoup-object-fromhtml_key36
creating-a-beautifulsoup-object-fromhtml_key37


```python
>>> import bs4
>>> soup = bs4.BeautifulSoup(open('example.html'))
>>> spanElem = soup.select('span')[0]
>>> str(spanElem)
```
creating-a-beautifulsoup-object-fromhtml_key38
```python
>>> spanElem.get('id')
```
creating-a-beautifulsoup-object-fromhtml_key39
```python
>>> spanElem.get('some_nonexistent_addr') == None
```
creating-a-beautifulsoup-object-fromhtml_key40
```python
>>> spanElem.attrs
```
creating-a-beautifulsoup-object-fromhtml_key41
