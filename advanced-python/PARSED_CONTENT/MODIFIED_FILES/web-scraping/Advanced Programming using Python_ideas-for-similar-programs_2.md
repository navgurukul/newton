```ngMeta
ideas-for-similar-programs_2_key1
```

ideas-for-similar-programs_2_key2
ideas-for-similar-programs_2_key3


ideas-for-similar-programs_2_key4


ideas-for-similar-programs_2_key5


ideas-for-similar-programs_2_key6


ideas-for-similar-programs_2_key7
ideas-for-similar-programs_2_key8


ideas-for-similar-programs_2_key9


ideas-for-similar-programs_2_key10


ideas-for-similar-programs_2_key11


ideas-for-similar-programs_2_key12


ideas-for-similar-programs_2_key13


ideas-for-similar-programs_2_key14


![image](asseta/000016.jpg)ideas-for-similar-programs_2_key15


ideas-for-similar-programs_2_key16


ideas-for-similar-programs_2_key17


ideas-for-similar-programs_2_key18


ideas-for-similar-programs_2_key19


ideas-for-similar-programs_2_key20


ideas-for-similar-programs_2_key21
ideas-for-similar-programs_2_key22
ideas-for-similar-programs_2_key23


ideas-for-similar-programs_2_key24


ideas-for-similar-programs_2_key25


ideas-for-similar-programs_2_key26


ideas-for-similar-programs_2_key27


ideas-for-similar-programs_2_key28



ideas-for-similar-programs_2_key29
ideas-for-similar-programs_2_key30
ideas-for-similar-programs_2_key31


ideas-for-similar-programs_2_key32
ideas-for-similar-programs_2_key33
ideas-for-similar-programs_2_key34


ideas-for-similar-programs_2_key35


ideas-for-similar-programs_2_key36


ideas-for-similar-programs_2_key37
ideas-for-similar-programs_2_key38



ideas-for-similar-programs_2_key39
ideas-for-similar-programs_2_key40
ideas-for-similar-programs_2_key41


ideas-for-similar-programs_2_key42
```python
    # Download the page.
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)
```
ideas-for-similar-programs_2_key43


ideas-for-similar-programs_2_key44
ideas-for-similar-programs_2_key45



ideas-for-similar-programs_2_key46
ideas-for-similar-programs_2_key47
ideas-for-similar-programs_2_key48


ideas-for-similar-programs_2_key49
```python
    # Find the URL of the comic image.
    comicElem = soup.select('#comic img')
    if comicElem == []:
         print('Could not find comic image.')
    else:
         try:
             comicUrl = 'http:' + comicElem[0].get('src')
             # Download the image.
             print('Downloading image %s...' % (comicUrl))
             res = requests.get(comicUrl)
             res.raise_for_status()
         except requests.exceptions.MissingSchema:
             # skip this comic
             prevLink = soup.select('a[rel="prev"]')[0]
             url = 'http://xkcd.com' + prevLink.get('href')
             continue
```
ideas-for-similar-programs_2_key50


ideas-for-similar-programs_2_key51


ideas-for-similar-programs_2_key52


ideas-for-similar-programs_2_key53
ideas-for-similar-programs_2_key54



ideas-for-similar-programs_2_key55


ideas-for-similar-programs_2_key56
```python
        # Save the image to ./xkcd.
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    # Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')
```
ideas-for-similar-programs_2_key57


ideas-for-similar-programs_2_key58


ideas-for-similar-programs_2_key59


ideas-for-similar-programs_2_key60


ideas-for-similar-programs_2_key61



ideas-for-similar-programs_2_key62


ideas-for-similar-programs_2_key63
ideas-for-similar-programs_2_key64


ideas-for-similar-programs_2_key65


ideas-for-similar-programs_2_key66


ideas-for-similar-programs_2_key67


ideas-for-similar-programs_2_key68
