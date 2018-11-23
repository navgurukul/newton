```ngMeta
name: working-with-the-screen
completionMethod: manual
```
# Working with the Screen
Your GUI automation programs don’t have to click and type blindly. PyAutoGUI has screenshot features that can create an image file based on the current contents of the screen. These functions can also return a Pillow Image object of the current screen’s appearance. If you’ve been skipping around in this book, you’ll want to read Chapter 17 and install the pillow module before continuing with this section.

On Linux computers, the scrot program needs to be installed to use the screenshot functions in PyAutoGUI. In a Terminal window, run sudo apt-get install scrot to install this program. If you’re on Windows or OS X, skip this step and continue with the section.

# Getting a Screenshot
To take screenshots in Python, call the pyautogui.screenshot() function. Enter the following into the interactive shell:

```python
>>> import pyautogui
>>> im = pyautogui.screenshot()
```
The im variable will contain the Image object of the screenshot. You can now call methods on the Image object in the im variable, just like any other Image object. Enter the following into the interactive shell:

```python
>>> im.getpixel((0, 0))
```
(176, 176, 175)
```python
>>> im.getpixel((50, 200))
```
(130, 135, 144)
Pass getpixel() a tuple of coordinates, like (0, 0) or (50, 200), and it’ll tell you the color of the pixel at those coordinates in your image. The return value from getpixel() is an RGB tuple of three integers for the amount of red, green, and blue in the pixel. (There is no fourth value for alpha, because screenshot images are fully opaque.) This is how your programs can “see” what is currently on the screen.

