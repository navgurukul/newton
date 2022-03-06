```ngMeta
name: controlling-mouse-movement
```
# Controlling Mouse Movement
In this section, you’ll learn how to move the mouse and track its position on the screen using PyAutoGUI, but first you need to understand how PyAutoGUI works with coordinates.

The mouse functions of PyAutoGUI use x- and y-coordinates. Figure 18-1 shows the coordinate system for the computer screen; it’s similar to the coordinate system used for images, discussed in Chapter 17. The origin, where x and y are both zero, is at the upper-left corner of the screen. The x-coordinates increase going to the right, and the y-coordinates increase going down. All coordinates are positive integers; there are no negative coordinates.

<!-- ![image](assets/000011.jpg)
 -->
Figure 18-1. The coordinates of a computer screen with 1920×1080 resolution

Your resolution is how many pixels wide and tall your screen is. If your screen’s resolution is set to 1920×1080, then the coordinate for the upper-left corner will be (0, 0), and the coordinate for the bottom-right corner will be (1919, 1079).

The pyautogui.size() function returns a two-integer tuple of the screen’s width and height in pixels. Enter the following into the interactive shell:

```python
>>> import pyautogui
>>> pyautogui.size()
```
(1920, 1080)
```python
>>> width, height = pyautogui.size()
```
pyautogui.size() returns (1920, 1080) on a computer with a 1920×1080 resolution; depending on your screen’s resolution, your return value may be different. You can store the width and height from pyautogui.size() in variables like width and height for better readability in your programs.

