changing-individual-pixels_key1
changing-individual-pixels_key2


```python
❶ >>> im = Image.new('RGBA', (100, 100))
❷ >>> im.getpixel((0, 0))
```
changing-individual-pixels_key3
```python
❸ >>> for x in range(100):
```
           for y in range(50):
changing-individual-pixels_key4
```python
   >>> from PIL import ImageColor
❺ >>> for x in range(100):
           for y in range(50, 100):
```
changing-individual-pixels_key5
```python
   >>> im.getpixel((0, 0))
```
changing-individual-pixels_key6
```python
   >>> im.getpixel((0, 50))
```
changing-individual-pixels_key7
```python
   >>> im.save('putPixel.png')
```
changing-individual-pixels_key8


changing-individual-pixels_key9


![image](assets/000083.jpg)
changing-individual-pixels_key10


changing-individual-pixels_key11
