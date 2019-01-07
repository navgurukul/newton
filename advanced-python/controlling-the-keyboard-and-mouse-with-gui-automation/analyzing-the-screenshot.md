```ngMeta
name: analyzing-the-screenshot
```
# Analyzing the Screenshot
Say that one of the steps in your GUI automation program is to click a gray button. Before calling the click() method, you could take a screenshot and look at the pixel where the script is about to click. If it’s not the same gray as the gray button, then your program knows something is wrong. Maybe the window moved unexpectedly, or maybe a pop-up dialog has blocked the button. At this point, instead of continuing—and possibly wreaking havoc by clicking the wrong thing—your program can “see” that it isn’t clicking on the right thing and stop itself.

PyAutoGUI’s pixelMatchesColor() function will return True if the pixel at the given x- and y-coordinates on the screen matches the given color. The first and second arguments are integers for the x- and y-coordinates, and the third argument is a tuple of three integers for the RGB color the screen pixel must match. Enter the following into the interactive shell:

```python
   >>> import pyautogui
   >>> im = pyautogui.screenshot()
❶ >>> im.getpixel((50, 200))
```
   (130, 135, 144)
```python
❷ >>> pyautogui.pixelMatchesColor(50, 200, (130, 135, 144))
```
   True
```python
❸ >>> pyautogui.pixelMatchesColor(50, 200, (255, 135, 144))
```
   False
After taking a screenshot and using getpixel() to get an RGB tuple for the color of a pixel at specific coordinates ❶, pass the same coordinates and RGB tuple to pixelMatchesColor() ❷, which should return True. Then change a value in the RGB tuple and call pixelMatchesColor() again for the same coordinates ❸. This should return false. This method can be useful to call whenever your GUI automation programs are about to call click(). Note that the color at the given coordinates must exactly match. If it is even slightly different—for example, (255, 255, 254) instead of (255, 255, 255)—then pixelMatchesColor() will return False.