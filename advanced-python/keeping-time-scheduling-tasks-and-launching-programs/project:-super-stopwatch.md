```ngMeta
name: project:-super-stopwatch
```
# Project: Super Stopwatch
Say you want to track how much time you spend on boring tasks you haven’t automated yet. You don’t have a physical stopwatch, and it’s surprisingly difficult to find a free stopwatch app for your laptop or smartphone that isn’t covered in ads and doesn’t send a copy of your browser history to marketers. (It says it can do this in the license agreement you agreed to. You did read the license agreement, didn’t you?) You can write a simple stopwatch program yourself in Python.

At a high level, here’s what your program will do:

Track the amount of time elapsed between presses of the ENTER key, with each key press starting a new “lap” on the timer.

Print the lap number, total time, and lap time.

This means your code will need to do the following:

Find the current time by calling time.time() and store it as a timestamp at the start of the program, as well as at the start of each lap.

Keep a lap counter and increment it every time the user presses ENTER.

Calculate the elapsed time by subtracting timestamps.

Handle the KeyboardInterrupt exception so the user can press CTRL-C to quit.

Open a new file editor window and save it as stopwatch.py.

# Step 1: Set Up the Program to Track Times
The stopwatch program will need to use the current time, so you’ll want to import the time module. Your program should also print some brief instructions to the user before calling input(), so the timer can begin after the user presses ENTER. Then the code will start tracking lap times.

Enter the following code into the file editor, writing a TODO comment as a placeholder for the rest of the code:


# !python3
# stopwatch.py - A simple stopwatch program.

import time

# Display the program's instructions.
print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch.
Press Ctrl-C to quit.')
input()                    # press Enter to begin
print('Started.')
startTime = time.time()    # get the first lap's start time
lastTime = startTime
lapNum = 1

# TODO: Start tracking the lap times.
Now that we’ve written the code to display the instructions, start the first lap, note the time, and set our lap count to 1.

# Step 2: Track and Print Lap Times
Now let’s write the code to start each new lap, calculate how long the previous lap took, and calculate the total time elapsed since starting the stopwatch. We’ll display the lap time and total time and increase the lap count for each new lap. Add the following code to your program:


   #! python3
   # stopwatch.py - A simple stopwatch program.

   import time

   --snip--
```python
   # Start tracking the lap times.
❶ try:
❷    while True:
           input()
❸         lapTime = round(time.time() - lastTime, 2)
❹         totalTime = round(time.time() - startTime, 2)
❺         print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
           lapNum += 1
           lastTime = time.time() # reset the last lap time
❻ except KeyboardInterrupt:
```
       # Handle the Ctrl-C exception to keep its error message from displaying.
       print('\nDone.')
If the user presses CTRL-C to stop the stopwatch, the KeyboardInterrupt exception will be raised, and the program will crash if its execution is not a try statement. To prevent crashing, we wrap this part of the program in a try statement ❶. We’ll handle the exception in the except clause ❻, so when CTRL-C is pressed and the exception is raised, the program execution moves to the except clause to print Done, instead of the KeyboardInterrupt error message. Until this happens, the execution is inside an infinite loop ❷ that calls input() and waits until the user presses ENTER to end a lap. When a lap ends, we calculate how long the lap took by subtracting the start time of the lap, lastTime, from the current time, time.time() ❸. We calculate the total time elapsed by subtracting the overall start time of the stopwatch, startTime, from the current time ❹.

Since the results of these time calculations will have many digits after the decimal point (such as 4.766272783279419), we use the round() function to round the float value to two digits at ❸ and ❹.

At ❺, we print the lap number, total time elapsed, and the lap time. Since the user pressing ENTER for the input() call will print a newline to the screen, pass end='' to the print() function to avoid double-spacing the output. After printing the lap information, we get ready for the next lap by adding 1 to the count lapNum and setting lastTime to the current time, which is the start time of the next lap.

# Ideas for Similar Programs
Time tracking opens up several possibilities for your programs. Although you can download apps to do some of these things, the benefit of writing programs yourself is that they will be free and not bloated with ads and useless features. You could write similar programs to do the following:

Create a simple timesheet app that records when you type a person’s name and uses the current time to clock them in or out.

Add a feature to your program to display the elapsed time since a process started, such as a download that uses the requests module. (See Chapter 11.)

Intermittently check how long a program has been running and offer the user a chance to cancel tasks that are taking too long.