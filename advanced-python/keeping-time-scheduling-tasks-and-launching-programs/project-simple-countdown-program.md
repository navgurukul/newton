```ngMeta
name: project-simple-countdown-program
```
# Project: Simple Countdown Program
Just like it’s hard to find a simple stopwatch application, it can be hard to find a simple countdown application. Let’s write a countdown program that plays an alarm at the end of the countdown.

At a high level, here’s what your program will do:

Count down from 60.

Play a sound file (alarm.wav) when the countdown reaches zero.

This means your code will need to do the following:

Pause for one second in between displaying each number in the countdown by calling time.sleep().

Call subprocess.Popen() to open the sound file with the default application.

Open a new file editor window and save it as countdown.py.

# Step 1: Count Down
This program will require the time module for the time.sleep() function and the subprocess module for the subprocess.Popen() function. Enter the following code and save the file as countdown.py:


   #! python3
   # countdown.py - A simple countdown script.
```python
import time, subprocess

❶ timeLeft = 60
   while timeLeft > 0:
❷     print(timeLeft, end='')
❸     time.sleep(1)
❹     timeLeft = timeLeft - 1
```

  # TODO: At the end of the countdown, play a sound file.
After importing time and subprocess, make a variable called timeLeft to hold the number of seconds left in the countdown ❶. It can start at 60—or you can change the value here to whatever you need or even have it get set from a command line argument.

In a while loop, you display the remaining count ❷, pause for one second ❸, and then decrement the timeLeft variable ❹ before the loop starts over again. The loop will keep looping as long as timeLeft is greater than 0. After that, the countdown will be over.

# Step 2: Play the Sound File
While there are third-party modules to play sound files of various formats, the quick and easy way is to just launch whatever application the user already uses to play sound files. The operating system will figure out from the .wav file extension which application it should launch to play the file. This .wav file could easily be some other sound file format, such as .mp3 or .ogg.

You can use any sound file that is on your computer to play at the end of the countdown, or you can download alarm.wav from <span><a href="http://nostarch.com/automatestuff/.">http://nostarch.com/automatestuff/.</a></span>

Add the following to your code:


# !python3
# countdown.py - A simple countdown script.

import time, subprocess

--snip--
```python
# At the end of the countdown, play a sound file.
subprocess.Popen(['start', 'alarm.wav'], shell=True)
```
After the while loop finishes, alarm.wav (or the sound file you choose) will play to notify the user that the countdown is over. On Windows, be sure to include 'start' in the list you pass to Popen() and pass the keyword argument shell=True. On OS X, pass 'open' instead of 'start' and remove shell=True.

Instead of playing a sound file, you could save a text file somewhere with a message like Break time is over! and use Popen() to open it at the end of the countdown. This will effectively create a pop-up window with a message. Or you could use the webbrowser.open() function to open a specific website at the end of the countdown. Unlike some free countdown application you’d find online, your own countdown program’s alarm can be anything you want!

# Ideas for Similar Programs
A countdown is a simple delay before continuing the program’s execution. This can also be used for other applications and features, such as the following:

Use time.sleep() to give the user a chance to press CTRL-C to cancel an action, such as deleting files. Your program can print a “Press CTRL-C to cancel” message and then handle any KeyboardInterrupt exceptions with try and except statements.

For a long-term countdown, you can use timedelta objects to measure the number of days, hours, minutes, and seconds until some point (a birthday? an anniversary?) in the future.

# Summary
The Unix epoch (January 1, 1970, at midnight, UTC) is a standard reference time for many programming languages, including Python. While the time.time() function module returns an epoch timestamp (that is, a float value of the number of seconds since the Unix epoch), the datetime module is better for performing date arithmetic and formatting or parsing strings with date information.

The time.sleep() function will block (that is, not return) for a certain number of seconds. It can be used to add pauses to your program. But if you want to schedule your programs to start at a certain time, the instructions at <span><a href="http://nostarch.com/automatestuff/">http://nostarch.com/automatestuff/</a></span> can tell you how to use the scheduler already provided by your operating system.

The threading module is used to create multiple threads, which is useful when you need to download multiple files or do other tasks simultaneously. But make sure the thread reads and writes only local variables, or you might run into concurrency issues.

Finally, your Python programs can launch other applications with the subprocess.Popen() function. Command line arguments can be passed to the Popen() call to open specific documents with the application. Alternatively, you can use the start, open, or see program with Popen() to use your computer’s file associations to automatically figure out which application to use to open a document. By using the other applications on your computer, your Python programs can leverage their capabilities for your automation needs.