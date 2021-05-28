```ngMeta
creating-a-beautifulsoup-object-fromhtml_key1
```
# creating-a-beautifulsoup-object-fromhtml_key2
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

# creating-a-beautifulsoup-object-fromhtml_key7
creating-a-beautifulsoup-object-fromhtml_key8

creating-a-beautifulsoup-object-fromhtml_key9creating-a-beautifulsoup-object-fromhtml_key10creating-a-beautifulsoup-object-fromhtml_key11

creating-a-beautifulsoup-object-fromhtml_key12

creating-a-beautifulsoup-object-fromhtml_key13

creating-a-beautifulsoup-object-fromhtml_key14

creating-a-beautifulsoup-object-fromhtml_key15

creating-a-beautifulsoup-object-fromhtml_key16

creating-a-beautifulsoup-object-fromhtml_key17

creating-a-beautifulsoup-object-fromhtml_key18creating-a-beautifulsoup-object-fromhtml_key19

creating-a-beautifulsoup-object-fromhtml_key20creating-a-beautifulsoup-object-fromhtml_key21creating-a-beautifulsoup-object-fromhtml_key22

creating-a-beautifulsoup-object-fromhtml_key23creating-a-beautifulsoup-object-fromhtml_key24

creating-a-beautifulsoup-object-fromhtml_key25creating-a-beautifulsoup-object-fromhtml_key26

creating-a-beautifulsoup-object-fromhtml_key27creating-a-beautifulsoup-object-fromhtml_key28

creating-a-beautifulsoup-object-fromhtml_key29

```python
>>> import bs4
>>> exampleFile = open('example.html')
>>> exampleSoup = bs4.BeautifulSoup(exampleFile.read())
>>> elems = exampleSoup.select('#author')
>>> type(elems)
```
creating-a-beautifulsoup-object-fromhtml_key30```python
>>> len(elems)
```
creating-a-beautifulsoup-object-fromhtml_key31```python
>>> type(elems[0])
```
creating-a-beautifulsoup-object-fromhtml_key32creating-a-beautifulsoup-object-fromhtml_key33creating-a-beautifulsoup-object-fromhtml_key34creating-a-beautifulsoup-object-fromhtml_key35creating-a-beautifulsoup-object-fromhtml_key36```python
>>> elems[0].attrs
```
creating-a-beautifulsoup-object-fromhtml_key37

creating-a-beautifulsoup-object-fromhtml_key38

creating-a-beautifulsoup-object-fromhtml_key39creating-a-beautifulsoup-object-fromhtml_key40

```python
>>> pElems = exampleSoup.select('p')
>>> str(pElems[0])
```
creating-a-beautifulsoup-object-fromhtml_key41creating-a-beautifulsoup-object-fromhtml_key42creating-a-beautifulsoup-object-fromhtml_key43creating-a-beautifulsoup-object-fromhtml_key44creating-a-beautifulsoup-object-fromhtml_key45creating-a-beautifulsoup-object-fromhtml_key46creating-a-beautifulsoup-object-fromhtml_key47```python
>>> pElems[0].getText()
```
creating-a-beautifulsoup-object-fromhtml_key48```python
>>> str(pElems[1])
```
creating-a-beautifulsoup-object-fromhtml_key49creating-a-beautifulsoup-object-fromhtml_key50creating-a-beautifulsoup-object-fromhtml_key51```python
>>> pElems[1].getText()
```
creating-a-beautifulsoup-object-fromhtml_key52```python
>>> str(pElems[2])
```
creating-a-beautifulsoup-object-fromhtml_key53creating-a-beautifulsoup-object-fromhtml_key54creating-a-beautifulsoup-object-fromhtml_key55creating-a-beautifulsoup-object-fromhtml_key56```python
>>> pElems[2].getText()
```
creating-a-beautifulsoup-object-fromhtml_key57# creating-a-beautifulsoup-object-fromhtml_key58
creating-a-beautifulsoup-object-fromhtml_key59

```python
>>> import bs4
>>> soup = bs4.BeautifulSoup(open('example.html'))
>>> spanElem = soup.select('span')[0]
>>> str(spanElem)
```
creating-a-beautifulsoup-object-fromhtml_key60creating-a-beautifulsoup-object-fromhtml_key61creating-a-beautifulsoup-object-fromhtml_key62```python
>>> spanElem.get('id')
```
creating-a-beautifulsoup-object-fromhtml_key63```python
>>> spanElem.get('some_nonexistent_addr') == None
```
creating-a-beautifulsoup-object-fromhtml_key64```python
>>> spanElem.attrs
```
creating-a-beautifulsoup-object-fromhtml_key65creating-a-beautifulsoup-object-fromhtml_key66