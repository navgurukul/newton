```ngMeta
name: scrolling-the-mouse
completionMethod: manual
```
# Scrolling the Mouse
The final PyAutoGUI mouse function is scroll(), which you pass an integer argument for how many units you want to scroll the mouse up or down. The size of a unit varies for each operating system and application, so you’ll have to experiment to see exactly how far it scrolls in your particular situation. The scrolling takes place at the mouse cursor’s current position. Passing a positive integer scrolls up, and passing a negative integer scrolls down. Run the following in IDLE’s interactive shell while the mouse cursor is over the IDLE window:

```python
>>> pyautogui.scroll(200)
```
You’ll see IDLE briefly scroll upward—and then go back down. The downward scrolling happens because IDLE automatically scrolls down to the bottom after executing an instruction. Enter this code instead:

```python
>>> import pyperclip
>>> numbers = ''
>>> for i in range(200):
      numbers = numbers + str(i) + '\n'

>>> pyperclip.copy(numbers)
```
This imports pyperclip and sets up an empty string, numbers. The code then loops through 200 numbers and adds each number to numbers, along with a newline. After pyperclip.copy(numbers), the clipboard will be loaded with 200 lines of numbers. Open a new file editor window and paste the text into it. This will give you a large text window to try scrolling in. Enter the following code into the interactive shell:

```python
>>> import time, pyautogui
>>> time.sleep(5); pyautogui.scroll(100)
```
On the second line, you enter two commands separated by a semicolon, which tells Python to run the commands as if they were on separate lines. The only difference is that the interactive shell won’t prompt you for input between the two instructions. This is important for this example because we want to the call to pyautogui.scroll() to happen automatically after the wait. (Note that while putting two commands on one line can be useful in the interactive shell, you should still have each instruction on a separate line in your programs.)

After pressing ENTER to run the code, you will have five seconds to click the file editor window to put it in focus. Once the pause is over, the pyautogui.scroll() call will cause the file editor window to scroll up after the five-second delay.

