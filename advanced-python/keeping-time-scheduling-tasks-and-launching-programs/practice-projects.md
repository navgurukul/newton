```ngMeta
name: practice-projects
completionMethod: manual
```
# Practice Projects
For practice, write programs that do the following.

# Prettified Stopwatch
Expand the stopwatch project from this chapter so that it uses the rjust() and ljust() string methods to “prettify” the output. (These methods were covered in Chapter 6.) Instead of output such as this:


Lap #1: 3.56 (3.56)
Lap #2: 8.63 (5.07)
Lap #3: 17.68 (9.05)
Lap #4: 19.11 (1.43)
... the output will look like this:


Lap # 1:  3.56 (  3.56)
Lap # 2:  8.63 (  5.07)
Lap # 3: 17.68 (  9.05)
Lap # 4: 19.11 (  1.43)
Note that you will need string versions of the lapNum, lapTime, and totalTime integer and float variables in order to call the string methods on them.

Next, use the pyperclip module introduced in Chapter 6 to copy the text output to the clipboard so the user can quickly paste the output to a text file or email.

# Scheduled Web Comic Downloader
Write a program that checks the websites of several web comics and automatically downloads the images if the comic was updated since the program’s last visit. Your operating system’s scheduler (Scheduled Tasks on Windows, launchd on OS X, and cron on Linux) can run your Python program once a day. The Python program itself can download the comic and then copy it to your desktop so that it is easy to find. This will free you from having to check the website yourself to see whether it has updated. (A list of web comics is available at <span><a href="http://nostarch.com/automatestuff/.)">http://nostarch.com/automatestuff/.</a></span>