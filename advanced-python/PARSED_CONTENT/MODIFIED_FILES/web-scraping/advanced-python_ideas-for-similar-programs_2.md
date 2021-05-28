```ngMeta
ideas-for-similar-programs_2_key1
```
# ideas-for-similar-programs_2_key2
ideas-for-similar-programs_2_key3

ideas-for-similar-programs_2_key4

ideas-for-similar-programs_2_key5

ideas-for-similar-programs_2_key6

# ideas-for-similar-programs_2_key7
ideas-for-similar-programs_2_key8

ideas-for-similar-programs_2_key9ideas-for-similar-programs_2_key10ideas-for-similar-programs_2_key11

ideas-for-similar-programs_2_key12

ideas-for-similar-programs_2_key13

ideas-for-similar-programs_2_key14

ideas-for-similar-programs_2_key15

ideas-for-similar-programs_2_key16

ideas-for-similar-programs_2_key17

ideas-for-similar-programs_2_key18

ideas-for-similar-programs_2_key19

ideas-for-similar-programs_2_key20

ideas-for-similar-programs_2_key21

ideas-for-similar-programs_2_key22

ideas-for-similar-programs_2_key23# ideas-for-similar-programs_2_key24
ideas-for-similar-programs_2_key25

ideas-for-similar-programs_2_key26ideas-for-similar-programs_2_key27

ideas-for-similar-programs_2_key28ideas-for-similar-programs_2_key29ideas-for-similar-programs_2_key30

ideas-for-similar-programs_2_key31

ideas-for-similar-programs_2_key32ideas-for-similar-programs_2_key33ideas-for-similar-programs_2_key34

ideas-for-similar-programs_2_key35


ideas-for-similar-programs_2_key36# ideas-for-similar-programs_2_key37
ideas-for-similar-programs_2_key38

ideas-for-similar-programs_2_key39ideas-for-similar-programs_2_key40ideas-for-similar-programs_2_key41 ideas-for-similar-programs_2_key42
ideas-for-similar-programs_2_key43

ideas-for-similar-programs_2_key44[ideas-for-similar-programs_2_key45](http://xkcd.com&#39;)
ideas-for-similar-programs_2_key46

ideas-for-similar-programs_2_key47

# ideas-for-similar-programs_2_key48
ideas-for-similar-programs_2_key49


ideas-for-similar-programs_2_key50# ideas-for-similar-programs_2_key51
ideas-for-similar-programs_2_key52

ideas-for-similar-programs_2_key53ideas-for-similar-programs_2_key54ideas-for-similar-programs_2_key55```python
    # Download the page.
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)
```
ideas-for-similar-programs_2_key56

# ideas-for-similar-programs_2_key57
ideas-for-similar-programs_2_key58


ideas-for-similar-programs_2_key59# ideas-for-similar-programs_2_key60
ideas-for-similar-programs_2_key61

ideas-for-similar-programs_2_key62```python
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
ideas-for-similar-programs_2_key63ideas-for-similar-programs_2_key64ideas-for-similar-programs_2_key65ideas-for-similar-programs_2_key66

ideas-for-similar-programs_2_key67

ideas-for-similar-programs_2_key68ideas-for-similar-programs_2_key69ideas-for-similar-programs_2_key70

# ideas-for-similar-programs_2_key71
ideas-for-similar-programs_2_key72


ideas-for-similar-programs_2_key73

ideas-for-similar-programs_2_key74```python
        # Save the image to ./xkcd.
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    # Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')
```
ideas-for-similar-programs_2_key75

ideas-for-similar-programs_2_key76ideas-for-similar-programs_2_key77ideas-for-similar-programs_2_key78\)ideas-for-similar-programs_2_key79

ideas-for-similar-programs_2_key80

ideas-for-similar-programs_2_key81ideas-for-similar-programs_2_key82ideas-for-similar-programs_2_key83

ideas-for-similar-programs_2_key84


ideas-for-similar-programs_2_key85ideas-for-similar-programs_2_key86ideas-for-similar-programs_2_key87ideas-for-similar-programs_2_key88ideas-for-similar-programs_2_key89ideas-for-similar-programs_2_key90ideas-for-similar-programs_2_key91ideas-for-similar-programs_2_key92ideas-for-similar-programs_2_key93ideas-for-similar-programs_2_key94ideas-for-similar-programs_2_key95ideas-for-similar-programs_2_key96ideas-for-similar-programs_2_key97ideas-for-similar-programs_2_key98ideas-for-similar-programs_2_key99ideas-for-similar-programs_2_key100ideas-for-similar-programs_2_key101ideas-for-similar-programs_2_key102ideas-for-similar-programs_2_key103ideas-for-similar-programs_2_key104ideas-for-similar-programs_2_key105ideas-for-similar-programs_2_key106ideas-for-similar-programs_2_key107ideas-for-similar-programs_2_key108ideas-for-similar-programs_2_key109ideas-for-similar-programs_2_key110

# ideas-for-similar-programs_2_key111
ideas-for-similar-programs_2_key112

ideas-for-similar-programs_2_key113

ideas-for-similar-programs_2_key114

ideas-for-similar-programs_2_key115

ideas-for-similar-programs_2_key116