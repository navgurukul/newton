```ngMeta
name: finding-patterns-of-text-with-regular-expressions
completionMethod: manual
```
# Finding Patterns of Text with Regular Expressions
The previous phone number–finding program works, but it uses a lot of code to do something limited: The isPhoneNumber() function is 17 lines but can find only one pattern of phone numbers. What about a phone number formatted like 415.555.4242 or (415) 555-4242? What if the phone number had an extension, like 415-555-4242 x99? The isPhoneNumber() function would fail to validate them. You could add yet more code for these additional patterns, but there is an easier way.

Regular expressions, called regexes for short, are descriptions for a pattern of text. For example, a \d in a regex stands for a digit character—that is, any single numeral 0 to 9. The regex \d\d\d-\d\d\d-\d\d\d\d is used by Python to match the same text the previous isPhoneNumber() function did: a string of three numbers, a hyphen, three more numbers, another hyphen, and four numbers. Any other string would not match the \d\d\d-\d\d\d-\d\d \d\d regex.

But regular expressions can be much more sophisticated. For example, adding a 3 in curly brackets ({3}) after a pattern is like saying, “Match this pattern three times.” So the slightly shorter regex \d{3}-\d{3}-\d{4} also matches the correct phone number format.

# Creating Regex Objects
All the regex functions in Python are in the re module. Enter the following into the interactive shell to import this module:

```python
>>> import re
```
Note
Most of the examples that follow in this chapter will require the re module, so remember to import it at the beginning of any script you write or any time you restart IDLE. Otherwise, you’ll get a NameError: name 're' is not defined error message.

Passing a string value representing your regular expression to re.compile() returns a Regex pattern object (or simply, a Regex object).

To create a Regex object that matches the phone number pattern, enter the following into the interactive shell. (Remember that \d means “a digit character” and \d\d\d-\d\d\d-\d\d\d\d is the regular expression for the correct phone number pattern.)

```python
>>> phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
```
Now the phoneNumRegex variable contains a Regex object.

Passing Raw Strings to re.compile( )

Remember that escape characters in Python use the backslash (\). The string value '\n' represents a single newline character, not a backslash followed by a lowercase n. You need to enter the escape character \\ to print a single backslash. So '\\n' is the string that represents a backslash followed by a lowercase n. However, by putting an r before the first quote of the string value, you can mark the string as a raw string, which does not escape characters.

Since regular expressions frequently use backslashes in them, it is convenient to pass raw strings to the re.compile() function instead of typing extra backslashes. Typing r'\d\d\d-\d\d\d-\d\d\d\d' is much easier than typing '\\d\\d\\d-\\d\\d\\d-\\d\\d\\d\\d'.

# Matching Regex Objects
A Regex object’s search() method searches the string it is passed for any matches to the regex. The search() method will return None if the regex pattern is not found in the string. If the pattern is found, the search() method returns a Match object. Match objects have a group() method that will return the actual matched text from the searched string. (I’ll explain groups shortly.) For example, enter the following into the interactive shell:

```python
>>> phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
>>> mo = phoneNumRegex.search('My number is 415-555-4242.')
>>> print('Phone number found: ' + mo.group())
```
Phone number found: 415-555-4242
The mo variable name is just a generic name to use for Match objects. This example might seem complicated at first, but it is much shorter than the earlier isPhoneNumber.py program and does the same thing.

Here, we pass our desired pattern to re.compile() and store the resulting Regex object in phoneNumRegex. Then we call search() on phoneNumRegex and pass search() the string we want to search for a match. The result of the search gets stored in the variable mo. In this example, we know that our pattern will be found in the string, so we know that a Match object will be returned. Knowing that mo contains a Match object and not the null value None, we can call group() on mo to return the match. Writing mo.group() inside our print statement displays the whole match, 415-555-4242.

# Review of Regular Expression Matching
While there are several steps to using regular expressions in Python, each step is fairly simple.

Import the regex module with import re.

Create a Regex object with the re.compile() function. (Remember to use a raw string.)

Pass the string you want to search into the Regex object’s search() method. This returns a Match object.

Call the Match object’s group() method to return a string of the actual matched text.

# Note
While I encourage you to enter the example code into the interactive shell, you should also make use of web-based regular expression testers, which can show you exactly how a regex matches a piece of text that you enter. I recommend the tester at <span><a href="http://regexpal.com/.">regexpal.com</a></span>