```ngMeta
name: manipulating-strings
```
# Manipulating Strings
Text is one of the most common forms of data your programs will handle. You already know how to concatenate two string values together with the + operator, but you can do much more than that. You can extract partial strings from string values, add or remove spacing, convert letters to lowercase or uppercase, and check that strings are formatted correctly. You can even write Python code to access the clipboard for copying and pasting text.

In this chapter, you’ll learn all this and more. Then you’ll work through two different programming projects: a simple password manager and a program to automate the boring chore of formatting pieces of text.

# Working with Strings
Let’s look at some of the ways Python lets you write, print, and access strings in your code.

# String Literals
Typing string values in Python code is fairly straightforward: They begin and end with a single quote. But then how can you use a quote inside a string? Typing 'That is Alice's cat.' won’t work, because Python thinks the string ends after Alice, and the rest (s cat.') is invalid Python code. Fortunately, there are multiple ways to type strings.

# Double Quotes
Strings can begin and end with double quotes, just as they do with single quotes. One benefit of using double quotes is that the string can have a single quote character in it. Enter the following into the interactive shell:

```python
>>> spam = "That is Alice's cat."
```
Since the string begins with a double quote, Python knows that the single quote is part of the string and not marking the end of the string. However, if you need to use both single quotes and double quotes in the string, you’ll need to use escape characters.

# Escape Characters
An escape character lets you use characters that are otherwise impossible to put into a string. An escape character consists of a backslash (\) followed by the character you want to add to the string. (Despite consisting of two characters, it is commonly referred to as a singular escape character.) For example, the escape character for a single quote is \'. You can use this inside a string that begins and ends with single quotes. To see how escape characters work, enter the following into the interactive shell:

```python
>>> spam = 'Say hi to Bob\'s mother.'
```
Python knows that since the single quote in Bob\'s has a backslash, it is not a single quote meant to end the string value. The escape characters \' and \" let you put single quotes and double quotes inside your strings, respectively.

Table 6-1 lists the escape characters you can use.

Table 6-1. Escape Characters

Escape character

Prints as

\'

Single quote

\"

Double quote

\t

Tab

\n

Newline (line break)

\\

Backslash

Enter the following into the interactive shell:

```python
>>> print("Hello there!\nHow are you?\nI\'m doing fine.")
```
Hello there!
How are you?
I'm doing fine.
Raw Strings
You can place an r before the beginning quotation mark of a string to make it a raw string. A raw string completely ignores all escape characters and prints any backslash that appears in the string. For example, type the following into the interactive shell:

```python
>>> print(r'That is Carol\'s cat.')
```
That is Carol\'s cat.
Because this is a raw string, Python considers the backslash as part of the string and not as the start of an escape character. Raw strings are helpful if you are typing string values that contain many backslashes, such as the strings used for regular expressions described in the next chapter.