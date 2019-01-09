```ngMeta
name:  controlling-the-keyboard
```
# Controlling the Keyboard
PyAutoGUI also has functions for sending virtual keypresses to your computer, which enables you to fill out forms or enter text into applications.

# Sending a String from the Keyboard
The pyautogui.typewrite() function sends virtual keypresses to the computer. What these keypresses do depends on what window and text field have focus. You may want to first send a mouse click to the text field you want in order to ensure that it has focus.

As a simple example, let’s use Python to automatically type the words Hello world! into a file editor window. First, open a new file editor window and position it in the upper-left corner of your screen so that PyAutoGUI will click in the right place to bring it into focus. Next, enter the following into the interactive shell:

```python
>>> pyautogui.click(100, 100); pyautogui.typewrite('Hello world!')
```
Notice how placing two commands on the same line, separated by a semicolon, keeps the interactive shell from prompting you for input between running the two instructions. This prevents you from accidentally bringing a new window into focus between the click() and typewrite() calls, which would mess up the example.

Python will first send a virtual mouse click to the coordinates (100, 100), which should click the file editor window and put it in focus. The typewrite() call will send the text Hello world! to the window, making it look like Figure 18-3. You now have code that can type for you!

<!-- ![image](assets/0000108.jpg)
 -->
Figure 18-3. Using PyAutogGUI to click the file editor window and type Hello world! into it

By default, the typewrite() function will type the full string instantly. However, you can pass an optional second argument to add a short pause between each character. This second argument is an integer or float value of the number of seconds to pause. For example, pyautogui.typewrite('Hello world!', 0.25) will wait a quarter-second after typing H, another quarter-second after e, and so on. This gradual typewriter effect may be useful for slower applications that can’t process keystrokes fast enough to keep up with PyAutoGUI.

For characters such as A or !, PyAutoGUI will automatically simulate holding down the SHIFT key as well.
