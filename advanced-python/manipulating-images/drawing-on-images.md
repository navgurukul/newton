```ngMeta
name:  drawing-on-images
```
# Drawing on Images
If you need to draw lines, rectangles, circles, or other simple shapes on an image, use Pillow’s ImageDraw module. Enter the following into the interactive shell:

```python
>>> from PIL import Image, ImageDraw
>>> im = Image.new('RGBA', (200, 200), 'white')
>>> draw = ImageDraw.Draw(im)
```
First, we import Image and ImageDraw. Then we create a new image, in this case, a 200×200 white image, and store the Image object in im. We pass the Image object to the ImageDraw.Draw() function to receive an ImageDraw object. This object has several methods for drawing shapes and text onto an Image object. Store the ImageDraw object in a variable like draw so you can use it easily in the following example.

# Drawing Shapes
The following ImageDraw methods draw various kinds of shapes on the image. The fill and outline parameters for these methods are optional and will default to white if left unspecified.

## Points
The point(xy, fill) method draws individual pixels. The xy argument represents a list of the points you want to draw. The list can be a list of x- and y-coordinate tuples, such as [(x, y), (x, y), ...], or a list of x- and y-coordinates without tuples, such as [x1, y1, x2, y2, ...]. The fill argument is the color of the points and is either an RGBA tuple or a string of a color name, such as 'red'. The fill argument is optional.

## Lines
The line(xy, fill, width) method draws a line or series of lines. xy is either a list of tuples, such as [(x, y), (x, y), ...], or a list of integers, such as [x1, y1, x2, y2, ...]. Each point is one of the connecting points on the lines you’re drawing. The optional fill argument is the color of the lines, as an RGBA tuple or color name. The optional width argument is the width of the lines and defaults to 1 if left unspecified.

## Rectangles
The rectangle(xy, fill, outline) method draws a rectangle. The xy argument is a box tuple of the form (left, top, right, bottom). The left and top values specify the x- and y-coordinates of the upper-left corner of the rectangle, while right and bottom specify the lower-right corner. The optional fill argument is the color that will fill the inside of the rectangle. The optional outline argument is the color of the rectangle’s outline.

## Ellipses
The ellipse(xy, fill, outline) method draws an ellipse. If the width and height of the ellipse are identical, this method will draw a circle. The xy argument is a box tuple (left, top, right, bottom) that represents a box that precisely contains the ellipse. The optional fill argument is the color of the inside of the ellipse, and the optional outline argument is the color of the ellipse’s outline.

## Polygons
The polygon(xy, fill, outline) method draws an arbitrary polygon. The xy argument is a list of tuples, such as [(x, y), (x, y), ...], or integers, such as [x1, y1, x2, y2, ...], representing the connecting points of the polygon’s sides. The last pair of coordinates will be automatically connected to the first pair. The optional fill argument is the color of the inside of the polygon, and the optional outline argument is the color of the polygon’s outline.

Drawing Example
Enter the following into the interactive shell:

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
After making an Image object for a 200×200 white image, passing it to ImageDraw.Draw() to get an ImageDraw object, and storing the ImageDraw object in draw, you can call drawing methods on draw. Here we make a thin, black outline at the edges of the image ❶, a blue rectangle with its top-left corner at (20, 30) and bottom-right corner at (60, 60) ❷, a red ellipse defined by a box from (120, 30) to (160, 60) ❸, a brown polygon with five points ❹, and a pattern of green lines drawn with a for loop ❺. The resulting drawing.png file will look like Figure 17-14.

<!-- ![image](assets/000070.jpg)
 -->
Figure 17-14. The resulting drawing.png image

There are several other shape-drawing methods for ImageDraw objects. The full documentation is available at <span><a href="http://pillow.readthedocs.org/en/latest/reference/ImageDraw.html.">http://pillow.readthedocs.org/en/latest/reference/ImageDraw.html.</a></span>