```ngMeta
name: project-mapit.py-with-the-webbrowser-module
completionMethod: manual
```
# Project: mapit.py with the webbrowser Module
The webbrowser module’s open() function can launch a new browser to a specified URL. Enter the following into the interactive shell:

```python
>>> import webbrowser
>>> webbrowser.open('http://inventwithpython.com/')
```
A web browser tab will open to the URL <span><a href=" http://inventwithpython.com/"> http://inventwithpython.com/</a></span>. This is about the only thing the webbrowser module can do. Even so, the open() function does make some interesting things possible. For example, it’s tedious to copy a street address to the clipboard and bring up a map of it on Google Maps. You could take a few steps out of this task by writing a simple script to automatically launch the map in your browser using the contents of your clipboard. This way, you only have to copy the address to a clipboard and run the script, and the map will be loaded for you.

This is what your program does:

Gets a street address from the command line arguments or clipboard.

Opens the web browser to the Google Maps page for the address.

This means your code will need to do the following:

Read the command line arguments from sys.argv.

Read the clipboard contents.

Call the webbrowser.open() function to open the web browser.

Open a new file editor window and save it as mapIt.py.

# Step 1: Figure Out the URL
Based on the instructions in Appendix B, set up mapIt.py so that when you run it from the command line, like so...


C:\> mapit 870 Valencia St, San Francisco, CA 94110
... the script will use the command line arguments instead of the clipboard. If there are no command line arguments, then the program will know to use the contents of the clipboard.

First you need to figure out what URL to use for a given street address. When you load http://maps.google.com/ in the browser and search for an address, the URL in the address bar looks something like this: https://www.google.com/maps/place/870+Valencia+St/@37.7590311,-122.4215096,17z/data=!3m1!4b1!4m2!3m1!1s0x808f7e3dadc07a37:0xc86b0b2bb93b73d8.

The address is in the URL, but there’s a lot of additional text there as well. Websites often add extra data to URLs to help track visitors or customize sites. But if you try just going to https://www.google.com/maps/place/870+Valencia+St+San+Francisco+CA/, you’ll find that it still brings up the correct page. So your program can be set to open a web browser to 'https://www.google.com/maps/place/your_address_string' (where your_address_string is the address you want to map).

# Step 2: Handle the Command Line Arguments
Make your code look like this:


	#! python3
	# mapIt.py - Launches a map in the browser using an address from the
	# command line or clipboard.
```python
import webbrowser, sys
if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
```

# TODO: Get address from clipboard.
After the program’s #! shebang line, you need to import the webbrowser module for launching the browser and import the sys module for reading the potential command line arguments. The sys.argv variable stores a list of the program’s filename and command line arguments. If this list has more than just the filename in it, then len(sys.argv) evaluates to an integer greater than 1, meaning that command line arguments have indeed been provided.

Command line arguments are usually separated by spaces, but in this case, you want to interpret all of the arguments as a single string. Since sys.argv is a list of strings, you can pass it to the join() method, which returns a single string value. You don’t want the program name in this string, so instead of sys.argv, you should pass sys.argv[1:] to chop off the first element of the array. The final string that this expression evaluates to is stored in the address variable.

If you run the program by entering this into the command line...


mapit 870 Valencia St, San Francisco, CA 94110
... the sys.argv variable will contain this list value:


['mapIt.py', '870', 'Valencia', 'St, ', 'San', 'Francisco, ', 'CA', '94110']
The address variable will contain the string '870 Valencia St, San Francisco, CA 94110'.

# Step 3: Handle the Clipboard Content and Launch the Browser
Make your code look like the following:


#! python3
# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard.

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
```python
else:
    # Get address from clipboard.
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
```
If there are no command line arguments, the program will assume the address is stored on the clipboard. You can get the clipboard content with pyperclip.paste() and store it in a variable named address. Finally, to launch a web browser with the Google Maps URL, call webbrowser.open().

While some of the programs you write will perform huge tasks that save you hours, it can be just as satisfying to use a program that conveniently saves you a few seconds each time you perform a common task, such as getting a map of an address. Table 11-1 compares the steps needed to display a map with and without mapIt.py.

Table 11-1. Getting a Map with and Without mapIt.py

Manually getting a map

Using mapIt.py

Highlight the address.

Highlight the address.

Copy the address.

Copy the address.

Open the web browser.

Run mapIt.py.

Go to <span><a href="http://maps.google.com/.">http://maps.google.com/.</a></span>

 
Click the address text field.

 
Paste the address.

 
Press ENTER.

 
See how mapIt.py makes this task less tedious?

