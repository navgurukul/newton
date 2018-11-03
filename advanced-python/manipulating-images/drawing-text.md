```ngMeta
name: drawing-text
completionMethod: manual
```
# Drawing Text
The ImageDraw object also has a text() method for drawing text onto an image. The text() method takes four arguments: xy, text, fill, and font.

The xy argument is a two-integer tuple specifying the upper-left corner of the text box.

The text argument is the string of text you want to write.

The optional fill argument is the color of the text.

The optional font argument is an ImageFont object, used to set the type-face and size of the text. This is described in more detail in the next section.

Since it’s often hard to know in advance what size a block of text will be in a given font, the ImageDraw module also offers a textsize() method. Its first argument is the string of text you want to measure, and its second argument is an optional ImageFont object. The textsize() method will then return a two-integer tuple of the width and height that the text in the given font would be if it were written onto the image. You can use this width and height to help you calculate exactly where you want to put the text on your image.

The first three arguments for text() are straightforward. Before we use text() to draw text onto an image, let’s look at the optional fourth argument, the ImageFont object.

Both text() and textsize() take an optional ImageFont object as their final arguments. To create one of these objects, first run the following:

```python
>>> from PIL import ImageFont
```
Now that you’ve imported Pillow’s ImageFont module, you can call the ImageFont.truetype() function, which takes two arguments. The first argument is a string for the font’s TrueType file—this is the actual font file that lives on your hard drive. A TrueType file has the .ttf file extension and can usually be found in the following folders:

On Windows: C:\Windows\Fonts

On OS X: /Library/Fonts and /System/Library/Fonts

On Linux: /usr/share/fonts/truetype

You don’t actually need to enter these paths as part of the TrueType file string because Python knows to automatically search for fonts in these directories. But Python will display an error if it is unable to find the font you specified.

The second argument to ImageFont.truetype() is an integer for the font size in points (rather than, say, pixels). Keep in mind that Pillow creates PNG images that are 72 pixels per inch by default, and a point is 1/72 of an inch.

Enter the following into the interactive shell, replacing FONT_FOLDER with the actual folder name your operating system uses:

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
After importing Image, ImageDraw, ImageFont, and os, we make an Image object for a new 200×200 white image ❶ and make an ImageDraw object from the Image object ❷. We use text() to draw Hello at (20, 150) in purple ❸. We didn’t pass the optional fourth argument in this text() call, so the typeface and size of this text aren’t customized.

To set a typeface and size, we first store the folder name (like /Library/Fonts) in fontsFolder. Then we call ImageFont.truetype(), passing it the .ttf file for the font we want, followed by an integer font size ❹. Store the Font object you get from ImageFont.truetype() in a variable like arialFont, and then pass the variable to text() in the final keyword argument. The text() call at ❺ draws Howdy at (100, 150) in gray in 32-point Arial.

The resulting text.png file will look like Figure 17-15.

<!-- ![image](assets/000073.jpg)
 -->
Figure 17-15. The resulting text.png image

## Summary
Images consist of a collection of pixels, and each pixel has an RGBA value for its color and its addressable by x- and y-coordinates. Two common image formats are JPEG and PNG. The pillow module can handle both of these image formats and others.

When an image is loaded into an Image object, its width and height dimensions are stored as a two-integer tuple in the size attribute. Objects of the Image data type also have methods for common image manipulations: crop(), copy(), paste(), resize(), rotate(), and transpose(). To save the Image object to an image file, call the save() method.

If you want your program to draw shapes onto an image, use ImageDraw methods to draw points, lines, rectangles, ellipses, and polygons. The module also provides methods for drawing text in a typeface and font size of your choosing.

Although advanced (and expensive) applications such as Photoshop provide automatic batch processing features, you can use Python scripts to do many of the same modifications for free. In the previous chapters, you wrote Python programs to deal with plaintext files, spreadsheets, PDFs, and other formats. With the pillow module, you’ve extended your programming powers to processing images as well!

