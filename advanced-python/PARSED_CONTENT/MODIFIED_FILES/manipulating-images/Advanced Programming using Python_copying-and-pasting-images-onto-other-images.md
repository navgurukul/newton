```ngMeta
copying-and-pasting-images-onto-other-images_key1
```

copying-and-pasting-images-onto-other-images_key2
copying-and-pasting-images-onto-other-images_key3


```python
>>> catIm = Image.open('zophie.png')
>>> catCopyIm = catIm.copy()
```
copying-and-pasting-images-onto-other-images_key4


copying-and-pasting-images-onto-other-images_key5


```python
>>> faceIm = catIm.crop((335, 345, 565, 560))
>>> faceIm.size
```
copying-and-pasting-images-onto-other-images_key6
```python
>>> catCopyIm.paste(faceIm, (0, 0))
>>> catCopyIm.paste(faceIm, (400, 500))
>>> catCopyIm.save('pasted.png')
```
copying-and-pasting-images-onto-other-images_key7


![image](assets/000031.jpg)copying-and-pasting-images-onto-other-images_key8


copying-and-pasting-images-onto-other-images_key9


copying-and-pasting-images-onto-other-images_key10


copying-and-pasting-images-onto-other-images_key11


```python
   >>> catImWidth, catImHeight = catIm.size
   >>> faceImWidth, faceImHeight = faceIm.size
❶  >>> catCopyTwo = catIm.copy()
❷ >>> for left in range(0, catImWidth, faceImWidth):
❸         for top in range(0, catImHeight, faceImHeight):
               print(left, top)
               catCopyTwo.paste(faceIm, (left, top))
```
copying-and-pasting-images-onto-other-images_key12
```python
   >>> catCopyTwo.save('tiled.png')
```
copying-and-pasting-images-onto-other-images_key13


![image](assets/000049.jpg)copying-and-pasting-images-onto-other-images_key14


copying-and-pasting-images-onto-other-images_key15


copying-and-pasting-images-onto-other-images_key16
