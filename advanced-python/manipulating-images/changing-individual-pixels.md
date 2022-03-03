```ngMeta
name: changing-individual-pixels
```
# Changing Individual Pixels
The color of an individual pixel can be retrieved or set with the getpixel() and putpixel() methods. These methods both take a tuple representing the x- and y-coordinates of the pixel. The putpixel() method also takes an additional tuple argument for the color of the pixel. This color argument is a four-integer RGBA tuple or a three-integer RGB tuple. Enter the following into the interactive shell:

Let's hear Instagram creator, Kevin and Photographer, Piper. In the following video they explains how digital images works and how it's stored in computers. They also explained how RGB values creates a image and how images can be enhanced by changing this values.

@[youtube](15aqFQQVBWU)

```python
❶ >>> im = Image.new('RGBA', (100, 100))
❷ >>> im.getpixel((0, 0))
```
   (0, 0, 0, 0)
```python
❸ >>> for x in range(100):
```
           for y in range(50):
❹             im.putpixel((x, y), (210, 210, 210))
```python
   >>> from PIL import ImageColor
❺ >>> for x in range(100):
           for y in range(50, 100):
```
❻             im.putpixel((x, y), ImageColor.getcolor('darkgray', 'RGBA'))
```python
   >>> im.getpixel((0, 0))
```
   (210, 210, 210, 255)
```python
   >>> im.getpixel((0, 50))
```
   (169, 169, 169, 255)
```python
   >>> im.save('putPixel.png')
```
At ❶ we make a new image that is a 100×100 transparent square. Calling getpixel() on some coordinates in this image returns (0, 0, 0, 0) because the image is transparent ❷. To color pixels in this image, we can use nested for loops to go through all the pixels in the top half of the image ❸ and color each pixel using putpixel() ❹. Here we pass putpixel() the RGB tuple (210, 210, 210), a light gray.

Say we want to color the bottom half of the image dark gray but don’t know the RGB tuple for dark gray. The putpixel() method doesn’t accept a standard color name like 'darkgray', so you have to use ImageColor.getcolor() to get a color tuple from 'darkgray'. Loop through the pixels in the bottom half of the image ❺ and pass putpixel() the return value of ImageColor.getcolor() ❻, and you should now have an image that is light gray in its top half and dark gray in the bottom half, as shown in Figure 17-10. You can call getpixel() on some coordinates to confirm that the color at any given pixel is what you expect. Finally, save the image to putPixel.png.

<!-- ![image](assets/000083.jpg)
 -->
Figure 17-10. The putPixel.png image

Of course, drawing one pixel at a time onto an image isn’t very convenient. If you need to draw shapes, use the ImageDraw functions explained later in this chapter.

