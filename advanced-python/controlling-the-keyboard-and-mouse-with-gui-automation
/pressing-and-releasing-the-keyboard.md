```ngMeta
name: pressing-and-releasing-the-keyboard
completionMethod: manual
```
# Pressing and Releasing the Keyboard
Much like the mouseDown() and mouseUp() functions, pyautogui.keyDown() and pyautogui.keyUp() will send virtual keypresses and releases to the computer. They are passed a keyboard key string (see Table 18-1) for their argument. For convenience, PyAutoGUI provides the pyautogui.press() function, which calls both of these functions to simulate a complete keypress.

Run the following code, which will type a dollar sign character (obtained by holding the SHIFT key and pressing 4):

```python
>>> pyautogui.keyDown('shift'); pyautogui.press('4'); pyautogui.keyUp('shift')
```
This line presses down SHIFT, presses (and releases) 4, and then releases SHIFT. If you need to type a string into a text field, the typewrite() function is more suitable. But for applications that take single-key commands, the press() function is the simpler approach.

Hotkey Combinations
A hotkey or shortcut is a combination of keypresses to invoke some application function. The common hotkey for copying a selection is CTRL-C (on Windows and Linux) or ⌘-C (on OS X). The user presses and holds the CTRL key, then presses the C key, and then releases the C and CTRL keys. To do this with PyAutoGUI’s keyDown() and keyUp() functions, you would have to enter the following:


pyautogui.keyDown('ctrl')
pyautogui.keyDown('c')
pyautogui.keyUp('c')
pyautogui.keyUp('ctrl')
This is rather complicated. Instead, use the pyautogui.hotkey() function, which takes multiple keyboard key string arguments, presses them in order, and releases them in the reverse order. For the CTRL-C example, the code would simply be as follows:


pyautogui.hotkey('ctrl', 'c')
This function is especially useful for larger hotkey combinations. In Word, the CTRL-ALT-SHIFT-S hotkey combination displays the Style pane. Instead of making eight different function calls (four keyDown() calls and four keyUp() calls), you can just call hotkey('ctrl', 'alt', 'shift', 's').

With a new IDLE file editor window in the upper-left corner of your screen, enter the following into the interactive shell (in OS X, replace 'alt' with 'ctrl'):

```python
   >>> import pyautogui, time
   >>> def commentAfterDelay():
❶       pyautogui.click(100, 100)
❷       pyautogui.typewrite('In IDLE, Alt-3 comments out a line.')
         time.sleep(2)
❸       pyautogui.hotkey('alt', '3')

   >>> commentAfterDelay()
```
This defines a function commentAfterDelay() that, when called, will click the file editor window to bring it into focus ❶, type In IDLE, Atl-3 comments out a line ❷, pause for 2 seconds, and then simulate pressing the ALT-3 hotkey (or CTRL-3 on OS X) ❸. This keyboard shortcut adds two # characters to the current line, commenting it out. (This is a useful trick to know when writing your own code in IDLE.)

