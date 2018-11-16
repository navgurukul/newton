```ngMeta
name: key-names
completionMethod: manual
```
# Key Names
Not all keys are easy to represent with single text characters. For example, how do you represent SHIFT or the left arrow key as a single character? In PyAutoGUI, these keyboard keys are represented by short string values instead: 'esc' for the ESC key or 'enter' for the ENTER key.

Instead of a single string argument, a list of these keyboard key strings can be passed to typewrite(). For example, the following call presses the A key, then the B key, then the left arrow key twice, and finally the X and Y keys:

```python
>>> pyautogui.typewrite(['a', 'b', 'left', 'left', 'X', 'Y'])
```
Because pressing the left arrow key moves the keyboard cursor, this will output XYab. Table 18-1 lists the PyAutoGUI keyboard key strings that you can pass to typewrite() to simulate pressing any combination of keys.

You can also examine the pyautogui.KEYBOARD_KEYS list to see all possible keyboard key strings that PyAutoGUI will accept. The 'shift' string refers to the left SHIFT key and is equivalent to 'shiftleft'. The same applies for 'ctrl', 'alt', and 'win' strings; they all refer to the left-side key.

Table 18-1. PyKeyboard Attributes

Keyboard key string 															Meaning

'a', 'b', 'c', 'A', 'B', 'C', '1', '2', '3', '!', '@', '#', and so on     	The keys for single characters

'enter' (or 'return' or '\n') 												The ENTER key

'esc' 																		The ESC key

'shiftleft', 'shiftright'													The left and right SHIFT keys

'altleft', 'altright'														The left and right ALT keys

'ctrlleft', 'ctrlright' 													The left and right CTRL keys

'tab' (or '\t')																The TAB key

'backspace', 'delete' 														The BACKSPACE and DELETE keys

'pageup', 'pagedown' 														The PAGE UP and PAGE DOWN keys

'home', 'end' 																The HOME and END keys

'up', 'down', 'left', 'right' 												The up, down, left, and right arrow keys

'f1', 'f2', 'f3', and so on 												The F1 to F12 keys

'volumemute', 'volumedown', 'volumeup'											The mute, volume down, and volume up keys (some keyboards do not have these keys, but your operating system will still be able to understand these simulated keypresses)

'pause'																		The PAUSE key

'capslock', 'numlock', 'scrolllock'											The CAPS LOCK, NUM LOCK, and SCROLL LOCK keys

'insert' 																	The INS or INSERT key

'printscreen' 																The PRTSC or PRINT SCREEN key

'winleft', 'winright'														The left and right WIN keys (on Windows)

'command' 																	The Command () key (on OS X) 'option' The OPTION key (on OS X)