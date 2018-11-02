```ngMeta
name: chapter-18
completionMethod: manual
```
# Chapter 18
Move the mouse to the top-left corner of the screen, that is, the (0, 0) coordinates.

pyautogui.size() returns a tuple with two integers for the width and height of the screen.

pyautogui.position() returns a tuple with two integers for the x- and y-coordinates of the mouse cursor.

The moveTo() function moves the mouse to absolute coordinates on the screen, while the moveRel() function moves the mouse relative to the mouse’s current position.

pyautogui.dragTo() and pyautogui.dragRel()

pyautogui.typewrite('Hello world!')

Either pass a list of keyboard key strings to pyautogui.typewrite() (such as 'left') or pass a single keyboard key string to pyautogui.press().

pyautogui.screenshot('screenshot.png')

pyautogui.PAUSE = 2