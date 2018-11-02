```ngMeta
name: working-with-the-image-data-type
completionMethod: manual
```
# Working with the Image Data Type
An Image object has several useful attributes that give you basic information about the image file it was loaded from: its width and height, the filename, and the graphics format (such as JPEG, GIF, or PNG).

For example, enter the following into the interactive shell:

```python
   >>> from PIL import Image
   >>> catIm = Image.open('zophie.png')
   >>> catIm.size
```
❶ (816, 1088)
```python
❷ >>> width, height = catIm.size
❸ >>> width
```
   816
```python
❹ >>> height
```
   1088
```python
   >>> catIm.filename
```
   'zophie.png'
```python
   >>> catIm.format
```
   'PNG'
```python
   >>> catIm.format_description
```
   'Portable network graphics'
```python
❺ >>> catIm.save('zophie.jpg')
```
After making an Image object from Zophie.png and storing the Image object in catIm, we can see that the object’s size attribute contains a tuple of the image’s width and height in pixels ❶. We can assign the values in the tuple to width and height variables ❷ in order to access with width ❸ and height ❹ individually. The filename attribute describes the original file’s name. The format and format_description attributes are strings that describe the image format of the original file (with format_description being a bit more verbose).

Finally, calling the save() method and passing it 'zophie.jpg' saves a new image with the filename zophie.jpg to your hard drive ❺. Pillow sees that the file extension is .jpg and automatically saves the image using the JPEG image format. Now you should have two images, zophie.png and zophie.jpg, on your hard drive. While these files are based on the same image, they are not identical because of their different formats.

Pillow also provides the Image.new() function, which returns an Image object—much like Image.open(), except the image represented by Image.new()’s object will be blank. The arguments to Image.new() are as follows:

The string 'RGBA', which sets the color mode to RGBA. (There are other modes that this book doesn’t go into.)

The size, as a two-integer tuple of the new image’s width and height.

The background color that the image should start with, as a four-integer tuple of an RGBA value. You can use the return value of the ImageColor.getcolor() function for this argument. Alternatively, Image.new() also supports just passing the string of the standard color name.

For example, enter the following into the interactive shell:

```python
   >>> from PIL import Image
❶ >>> im = Image.new('RGBA', (100, 200), 'purple')
   >>> im.save('purpleImage.png')
❷ >>> im2 = Image.new('RGBA', (20, 20))
   >>> im2.save('transparentImage.png')
```
Here we create an Image object for an image that’s 100 pixels wide and 200 pixels tall, with a purple background ❶. This image is then saved to the file purpleImage.png. We call Image.new() again to create another Image object, this time passing (20, 20) for the dimensions and nothing for the background color ❷. Invisible black, (0, 0, 0, 0), is the default color used if no color argument is specified, so the second image has a transparent background; we save this 20×20 transparent square in transparentImage.png.

