```ngMeta
name: manipulating-images-with-pillow
```
# Manipulating Images with Pillow
Now that you know how colors and coordinates work in Pillow, let’s use Pillow to manipulate an image. Figure 17-3 is the image that will be used for all the interactive shell examples in this chapter. You can download it from <span><a href="http://nostarch.com/automatestuff/">http://nostarch.com/automatestuff/</a></span>.

Once you have the image file Zophie.png in your current working directory, you’ll be ready to load the image of Zophie into Python, like so:

```python
>>> from PIL import Image
>>> catIm = Image.open('zophie.png')
```

<!-- ![image](assets/000039.jpg)
 -->
Figure 17-3. My cat Zophie. The camera adds 10 pounds (which is a lot for a cat).

To load the image, you import the Image module from Pillow and call Image.open(), passing it the image’s filename. You can then store the loaded image in a variable like CatIm. The module name of Pillow is PIL to make it backward compatible with an older module called Python Imaging Library, which is why you must run from PIL import Image instead of from Pillow import Image. Because of the way Pillow’s creators set up the pillow module, you must use the from PIL import Image form of import statement, rather than simply import PIL.

If the image file isn’t in the current working directory, change the working directory to the folder that contains the image file by calling the os.chdir() function.

```python
>>> import os
>>> os.chdir('C:\\folder_with_image_file')
```
The Image.open() function returns a value of the Image object data type, which is how Pillow represents an image as a Python value. You can load an Image object from an image file (of any format) by passing the Image.open() function a string of the filename. Any changes you make to the Image object can be saved to an image file (also of any format) with the save() method. All the rotations, resizing, cropping, drawing, and other image manipulations will be done through method calls on this Image object.

To shorten the examples in this chapter, I’ll assume you’ve imported Pillow’s Image module and that you have the Zophie image stored in a variable named catIm. Be sure that the zophie.png file is in the current working directory so that the Image.open() function can find it. Otherwise, you will also have to specify the full absolute path in the string argument to Image.open().

