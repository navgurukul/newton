```ngMeta
drawing-text_key1
```
# drawing-text_key2
drawing-text_key3

drawing-text_key4

drawing-text_key5

drawing-text_key6

drawing-text_key7

drawing-text_key8

drawing-text_key9

drawing-text_key10

```python
>>> from PIL import ImageFont
```
drawing-text_key11

drawing-text_key12

drawing-text_key13

drawing-text_key14

drawing-text_key15

drawing-text_key16

drawing-text_key17

```python
   >>> from PIL import Image, ImageDraw, ImageFont
   >>> import os
❶ >>> im = Image.new('RGBA', (200, 200), 'white')
❷ >>> draw = ImageDraw.Draw(im)
❸ >>> draw.text((20, 150), 'Hello', fill='purple')
   >>> fontsFolder = 'FONT_FOLDER' # e.g. 'Library/Fonts'
❹ >>> arialFont = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 32)
❺ >>> draw.text((100, 150), 'Howdy', fill='gray', font=arialFont)
   >>> im.save('text.png')
```
drawing-text_key18

drawing-text_key19

drawing-text_key20

drawing-text_key21

## drawing-text_key22
drawing-text_key23

drawing-text_key24

drawing-text_key25

drawing-text_key26

