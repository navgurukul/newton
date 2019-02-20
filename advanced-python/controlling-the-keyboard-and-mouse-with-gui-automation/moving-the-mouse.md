```ngMeta
name: moving-the-mouse
```
# Moving the Mouse
Now that you understand screen coordinates, let’s move the mouse. The pyautogui.moveTo() function will instantly move the mouse cursor to a specified position on the screen. Integer values for the x- and y-coordinates make up the function’s first and second arguments, respectively. An optional duration integer or float keyword argument specifies the number of seconds it should take to move the mouse to the destination. If you leave it out, the default is 0 for instantaneous movement. (All of the duration keyword arguments in PyAutoGUI functions are optional.) Enter the following into the interactive shell:

```python
>>> import pyautogui
>>> for i in range(10):
```
      pyautogui.moveTo(100, 100, duration=0.25)
      pyautogui.moveTo(200, 100, duration=0.25)
      pyautogui.moveTo(200, 200, duration=0.25)
      pyautogui.moveTo(100, 200, duration=0.25)
This example moves the mouse cursor clockwise in a square pattern among the four coordinates provided a total of ten times. Each movement takes a quarter of a second, as specified by the duration=0.25 keyword argument. If you hadn’t passed a third argument to any of the pyautogui.moveTo() calls, the mouse cursor would have instantly teleported from point to point.

The pyautogui.moveRel() function moves the mouse cursor relative to its current position. The following example moves the mouse in the same square pattern, except it begins the square from wherever the mouse happens to be on the screen when the code starts running:

```python
>>> import pyautogui
>>> for i in range(10):
```
      pyautogui.moveRel(100, 0, duration=0.25)
      pyautogui.moveRel(0, 100, duration=0.25)
      pyautogui.moveRel(-100, 0, duration=0.25)
      pyautogui.moveRel(0, -100, duration=0.25)
pyautogui.moveRel() also takes three arguments: how many pixels to move horizontally to the right, how many pixels to move vertically downward, and (optionally) how long it should take to complete the movement. A negative integer for the first or second argument will cause the mouse to move left or upward, respectively.
# Getting the Mouse Position
You can determine the mouse’s current position by calling the pyautogui.position() function, which will return a tuple of the mouse cursor’s x and y positions at the time of the function call. Enter the following into the interactive shell, moving the mouse around after each call:

```python
>>> pyautogui.position()
```
(311, 622)
```python
>>> pyautogui.position()
```
(377, 481)
```python
>>> pyautogui.position()
```
(1536, 637)
Of course, your return values will vary depending on where your mouse cursor is.