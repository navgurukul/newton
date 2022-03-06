```ngMeta
name:  image-recognition
```
# Image Recognition
But what if you do not know beforehand where PyAutoGUI should click? You can use image recognition instead. Give PyAutoGUI an image of what you want to click and let it figure out the coordinates.

For example, if you have previously taken a screenshot to capture the image of a Submit button in submit.png, the locateOnScreen() function will return the coordinates where that image is found. To see how locateOnScreen() works, try taking a screenshot of a small area on your screen; then save the image and enter the following into the interactive shell, replacing 'submit. png' with the filename of your screenshot:

```python
>>> import pyautogui
>>> pyautogui.locateOnScreen('submit.png')
```
(643, 745, 70, 29)
The four-integer tuple that locateOnScreen() returns has the x-coordinate of the left edge, the y-coordinate of the top edge, the width, and the height for the first place on the screen the image was found. If you’re trying this on your computer with your own screenshot, your return value will be different from the one shown here.

If the image cannot be found on the screen, locateOnScreen() will return None. Note that the image on the screen must match the provided image perfectly in order to be recognized. If the image is even a pixel off, locateOnScreen() will return None.

If the image can be found in several places on the screen, locateAllOnScreen() will return a Generator object, which can be passed to list() to return a list of four-integer tuples. There will be one four-integer tuple for each location where the image is found on the screen. Continue the interactive shell example by entering the following (and replacing 'submit.png' with your own image filename):

```python
>>> list(pyautogui.locateAllOnScreen('submit.png'))
```
[(643, 745, 70, 29), (1007, 801, 70, 29)]
Each of the four-integer tuples represents an area on the screen. If your image is only found in one area, then using list() and locateAllOnScreen() just returns a list containing one tuple.

Once you have the four-integer tuple for the area on the screen where your image was found, you can click the center of this area by passing the tuple to the center() function to return x- and y-coordinates of the area’s center. Enter the following into the interactive shell, replacing the arguments with your own filename, four-integer tuple, and coordinate pair:

```python
>>> pyautogui.locateOnScreen('submit.png')
```
(643, 745, 70, 29)
```python
>>> pyautogui.center((643, 745, 70, 29))
```
(678, 759)
```python
>>> pyautogui.click((678, 759))
```
Once you have center coordinates from center(), passing the coordinates to click() should click the center of the area on the screen that matches the image you passed to locateOnScreen().