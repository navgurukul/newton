```ngMeta
name: project-“where-is-the-mouse-right-now?”
```
# Project: “Where Is the Mouse Right Now?”
Being able to determine the mouse position is an important part of setting up your GUI automation scripts. But it’s almost impossible to figure out the exact coordinates of a pixel just by looking at the screen. It would be handy to have a program that constantly displays the x- and y-coordinates of the mouse cursor as you move it around.

At a high level, here’s what your program should do:

Display the current x- and y-coordinates of the mouse cursor.

Update these coordinates as the mouse moves around the screen.

This means your code will need to do the following:

Call the position() function to fetch the current coordinates.

Erase the previously printed coordinates by printing \b backspace characters to the screen.

Handle the KeyboardInterrupt exception so the user can press CTRL-C to quit.

Open a new file editor window and save it as mouseNow.py.

# Step 1: Import the Module
Start your program with the following:


#! python3
# mouseNow.py - Displays the mouse cursor's current position.
import pyautogui
print('Press Ctrl-C to quit.')
#TODO: Get and print the mouse coordinates.
The beginning of the program imports the pyautogui module and prints a reminder to the user that they have to press CTRL-C to quit.

# Step 2: Set Up the Quit Code and Infinite Loop
You can use an infinite while loop to constantly print the current mouse coordinates from mouse.position(). As for the code that quits the program, you’ll need to catch the KeyboardInterrupt exception, which is raised whenever the user presses CTRL-C. If you don’t handle this exception, it will display an ugly traceback and error message to the user. Add the following to your program:


   #! python3
   # mouseNow.py - Displays the mouse cursor's current position.
   import pyautogui
   print('Press Ctrl-C to quit.')
```python
   try:
       while True:
           # TODO: Get and print the mouse coordinates.
❶ except KeyboardInterrupt:
❷     print('\nDone.')
```
To handle the exception, enclose the infinite while loop in a try statement. When the user presses CTRL-C, the program execution will move to the except clause ❶ and Done. will be printed in a new line ❷.

# Step 3: Get and Print the Mouse Coordinates
The code inside the while loop should get the current mouse coordinates, format them to look nice, and print them. Add the following code to the inside of the while loop:


#! python3
# mouseNow.py - Displays the mouse cursor's current position.
import pyautogui
print('Press Ctrl-C to quit.')
--snip--
```python
        # Get and print the mouse coordinates.
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
```
--snip--
Using the multiple assignment trick, the x and y variables are given the values of the two integers returned in the tuple from pyautogui.position(). By passing x and y to the str() function, you can get string forms of the integer coordinates. The rjust() string method will right-justify them so that they take up the same amount of space, whether the coordinate has one, two, three, or four digits. Concatenating the right-justified string coordinates with 'X: ' and ' Y: ' labels gives us a neatly formatted string, which will be stored in positionStr.

At the end of your program, add the following code:


   #! python3
   # mouseNow.py - Displays the mouse cursor's current position.
   --snip--
```python
           print(positionStr, end='')
❶         print('\b' * len(positionStr), end='', flush=True)
```
This actually prints positionStr to the screen. The end='' keyword argument to print() prevents the default newline character from being added to the end of the printed line. It’s possible to erase text you’ve already printed to the screen—but only for the most recent line of text. Once you print a newline character, you can’t erase anything printed before it.

To erase text, print the \b backspace escape character. This special character erases a character at the end of the current line on the screen. The line at ❶ uses string replication to produce a string with as many \b characters as the length of the string stored in positionStr, which has the effect of erasing the positionStr string that was last printed.

For a technical reason beyond the scope of this book, always pass flush=True to print() calls that print \b backspace characters. Otherwise, the screen might not update the text as desired.

Since the while loop repeats so quickly, the user won’t actually notice that you’re deleting and reprinting the whole number on the screen. For example, if the x-coordinate is 563 and the mouse moves one pixel to the right, it will look like only the 3 in 563 is changed to a 4.

When you run the program, there will be only two lines printed. They should look like something like this:


Press Ctrl-C to quit.
X: 290 Y: 424
The first line displays the instruction to press CTRL-C to quit. The second line with the mouse coordinates will change as you move the mouse around the screen. Using this program, you’ll be able to figure out the mouse coordinates for your GUI automation scripts.

