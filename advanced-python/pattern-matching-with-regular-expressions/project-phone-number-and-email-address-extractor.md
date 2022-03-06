```ngMeta
name: project-phone-number-and-email-address-extractor
```
# Project: Phone Number and Email Address Extractor
Say you have the boring task of finding every phone number and email address in a long web page or document. If you manually scroll through the page, you might end up searching for a long time. But if you had a program that could search the text in your clipboard for phone numbers and email addresses, you could simply press CTRL-A to select all the text, press CTRL-C to copy it to the clipboard, and then run your program. It could replace the text on the clipboard with just the phone numbers and email addresses it finds.

Whenever you’re tackling a new project, it can be tempting to dive right into writing code. But more often than not, it’s best to take a step back and consider the bigger picture. I recommend first drawing up a high-level plan for what your program needs to do. Don’t think about the actual code yet—you can worry about that later. Right now, stick to broad strokes.

For example, your phone and email address extractor will need to do the following:

Get the text off the clipboard.

Find all phone numbers and email addresses in the text.

Paste them onto the clipboard.

Now you can start thinking about how this might work in code. The code will need to do the following:

Use the pyperclip module to copy and paste strings.

Create two regexes, one for matching phone numbers and the other for matching email addresses.

Find all matches, not just the first match, of both regexes.

Neatly format the matched strings into a single string to paste.

Display some kind of message if no matches were found in the text.

This list is like a road map for the project. As you write the code, you can focus on each of these steps separately. Each step is fairly manageable and expressed in terms of things you already know how to do in Python.

# Step 1: Create a Regex for Phone Numbers
First, you have to create a regular expression to search for phone numbers. Create a new file, enter the following, and save it as phoneAndEmail.py:


#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)

# TODO: Create email regex.

# TODO: Find matches in clipboard text.

# TODO: Copy results to the clipboard.
The TODO comments are just a skeleton for the program. They’ll be replaced as you write the actual code.

The phone number begins with an optional area code, so the area code group is followed with a question mark. Since the area code can be just three digits (that is, \d{3}) or three digits within parentheses (that is, \(\d{3}\)), you should have a pipe joining those parts. You can add the regex comment # Area code to this part of the multiline string to help you remember what (\d{3}|\(\d{3}\))? is supposed to match.

The phone number separator character can be a space (\s), hyphen (-), or period (.), so these parts should also be joined by pipes. The next few parts of the regular expression are straightforward: three digits, followed by another separator, followed by four digits. The last part is an optional extension made up of any number of spaces followed by ext, x, or ext., followed by two to five digits.

# Step 2: Create a Regex for Email Addresses
You will also need a regular expression that can match email addresses. Make your program look like the following:
```python

   #! python3
   # phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.
   import pyperclip, re

   phoneRegex = re.compile(r'''(
   --snip--

   # Create email regex.
   emailRegex = re.compile(r'''(
❶     [a-zA-Z0-9._%+-]+      # username
❷     @                      # @ symbol
❸     [a-zA-Z0-9.-]+         # domain name
       (\.[a-zA-Z]{2,4})      # dot-something
       )''', re.VERBOSE)
```
   # TODO: Find matches in clipboard text.

   # TODO: Copy results to the clipboard.
The username part of the email address ❶ is one or more characters that can be any of the following: lowercase and uppercase letters, numbers, a dot, an underscore, a percent sign, a plus sign, or a hyphen. You can put all of these into a character class: [a-zA-Z0-9._%+-].
The domain and username are separated by an @ symbol ❷. The domain name ❸ has a slightly less permissive character class with only letters, numbers, periods, and hyphens: [a-zA-Z0-9.-]. And last will be the “dot-com” part (technically known as the top-level domain), which can really be dot-anything. This is between two and four characters.
The format for email addresses has a lot of weird rules. This regular expression won’t match every possible valid email address, but it’ll match almost any typical email address you’ll encounter.
#Step 3: Find All Matches in the Clipboard Text
Now that you have specified the regular expressions for phone numbers and email addresses, you can let Python’s re module do the hard work of finding all the matches on the clipboard. The pyperclip.paste() function will get a string value of the text on the clipboard, and the findall() regex method will return a list of tuples.
Make your program look like the following:
```python
   #! python3
   # phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

   import pyperclip, re

   phoneRegex = re.compile(r'''(
   --snip--

   # Find matches in clipboard text.
   text = str(pyperclip.paste())
❶ matches = []
❷ for groups in phoneRegex.findall(text):
       phoneNum = '-'.join([groups[1], groups[3], groups[5]])
       if groups[8] != '':
           phoneNum += ' x' + groups[8]
       matches.append(phoneNum)
❸ for groups in emailRegex.findall(text):
       matches.append(groups[0])
```
   # TODO: Copy results to the clipboard.
There is one tuple for each match, and each tuple contains strings for each group in the regular expression. Remember that group 0 matches the entire regular expression, so the group at index 0 of the tuple is the one you are interested in.
As you can see at ❶, you’ll store the matches in a list variable named matches. It starts off as an empty list, and a couple for loops. For the email addresses, you append group 0 of each match ❸. For the matched phone numbers, you don’t want to just append group 0. While the program detects phone numbers in several formats, you want the phone number appended to be in a single, standard format. The phoneNum variable contains a string built from groups 1, 3, 5, and 8 of the matched text ❷. (These groups are the area code, first three digits, last four digits, and extension.)

# Step 4: Join the Matches into a String for the Clipboard
Now that you have the email addresses and phone numbers as a list of strings in matches, you want to put them on the clipboard. The pyperclip.copy() function takes only a single string value, not a list of strings, so you call the join() method on matches.
To make it easier to see that the program is working, let’s print any matches you find to the terminal. And if no phone numbers or email addresses were found, the program should tell the user this.
Make your program look like the following:
```python
#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

--snip--
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
```