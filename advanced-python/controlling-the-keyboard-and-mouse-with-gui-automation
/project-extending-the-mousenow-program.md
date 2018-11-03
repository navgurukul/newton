```ngMeta
name: project-extending-the-mousenow-program
completionMethod: manual
```
# Project: Extending the mouseNow Program
You could extend the mouseNow.py project from earlier in this chapter so that it not only gives the x- and y-coordinates of the mouse cursor’s current position but also gives the RGB color of the pixel under the cursor. Modify the code inside the while loop of mouseNow.py to look like this:


#! python3
# mouseNow.py - Displays the mouse cursor's current position.
--snip--
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
```python
        pixelColor = pyautogui.screenshot().getpixel((x, y))
        positionStr += ' RGB: (' + str(pixelColor[0]).rjust(3)
        positionStr += ', ' + str(pixelColor[1]).rjust(3)
        positionStr += ', ' + str(pixelColor[2]).rjust(3) + ')'
```
        print(positionStr, end='')
--snip--
Now, when you run mouseNow.py, the output will include the RGB color value of the pixel under the mouse cursor.


Press Ctrl-C to quit.
X:  406 Y:   17 RGB: (161, 50, 50)
This information, along with the pixelMatchesColor() function, should make it easy to add pixel color checks to your GUI automation scripts.