drawing-on-images_key1
drawing-on-images_key2


```python
>>> from PIL import Image, ImageDraw
>>> im = Image.new('RGBA', (200, 200), 'white')
>>> draw = ImageDraw.Draw(im)
```
drawing-on-images_key3


drawing-on-images_key4
drawing-on-images_key5


drawing-on-images_key6
drawing-on-images_key7


drawing-on-images_key8
drawing-on-images_key9


drawing-on-images_key10
drawing-on-images_key11


drawing-on-images_key12
drawing-on-images_key13


drawing-on-images_key14
drawing-on-images_key15


drawing-on-images_key16


```python
   >>> from PIL import Image, ImageDraw
   >>> im = Image.new('RGBA', (200, 200), 'white')
   >>> draw = ImageDraw.Draw(im)
❶ >>> draw.line([(0, 0), (199, 0), (199, 199), (0, 199), (0, 0)], fill='black')
❷ >>> draw.rectangle((20, 30, 60, 60), fill='blue')
❸ >>> draw.ellipse((120, 30, 160, 60), fill='red')
❹ >>> draw.polygon(((57, 87), (79, 62), (94, 85), (120, 90), (103, 113)), fill='brown')
❺ >>> for i in range(100, 200, 10):
```
           draw.line([(i, 0), (200, i - 100)], fill='green')
```python
   >>> im.save('drawing.png')
```
drawing-on-images_key17


![image](assets/000070.jpg)
drawing-on-images_key18


drawing-on-images_key19
