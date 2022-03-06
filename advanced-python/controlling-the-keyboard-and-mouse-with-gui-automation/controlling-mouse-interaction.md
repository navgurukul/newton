```ngMeta
name: controlling-mouse-interaction
```
# Controlling Mouse Interaction
Now that you know how to move the mouse and figure out where it is on the screen, you’re ready to start clicking, dragging, and scrolling.

# Clicking the Mouse
To send a virtual mouse click to your computer, call the pyautogui.click() method. By default, this click uses the left mouse button and takes place wherever the mouse cursor is currently located. You can pass x- and y-coordinates of the click as optional first and second arguments if you want it to take place somewhere other than the mouse’s current position.

If you want to specify which mouse button to use, include the button keyword argument, with a value of 'left', 'middle', or 'right'. For example, pyautogui.click(100, 150, button='left') will click the left mouse button at the coordinates (100, 150), while pyautogui.click(200, 250, button='right') will perform a right-click at (200, 250).

Enter the following into the interactive shell:

```python
>>> import pyautogui
>>> pyautogui.click(10, 5)
```
You should see the mouse pointer move to near the top-left corner of your screen and click once. A full “click” is defined as pushing a mouse button down and then releasing it back up without moving the cursor. You can also perform a click by calling pyautogui.mouseDown(), which only pushes the mouse button down, and pyautogui.mouseUp(), which only releases the button. These functions have the same arguments as click(), and in fact, the click() function is just a convenient wrapper around these two function calls.

As a further convenience, the pyautogui.doubleClick() function will perform two clicks with the left mouse button, while the pyautogui.rightClick() and pyautogui.middleClick() functions will perform a click with the right and middle mouse buttons, respectively.

