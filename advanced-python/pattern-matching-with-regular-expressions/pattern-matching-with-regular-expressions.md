```ngMeta
name: pattern-matching-with-regular-expressions
```

# Pattern Matching with Regular Expressions
You may be familiar with searching for text by pressing CTRL-F and typing in the words you’re looking for. Regular expressions go one step further: They allow you to specify a pattern of text to search for. You may not know a business’s exact phone number, but if you live in the United States or Canada, you know it will be three digits, followed by a hyphen, and then four more digits (and optionally, a three-digit area code at the start). This is how you, as a human, know a phone number when you see it: 415-555-1234 is a phone number, but 4,155,551,234 is not.

Regular expressions are helpful, but not many non-programmers know about them even though most modern text editors and word processors, such as Microsoft Word or OpenOffice, have find and find-and-replace features that can search based on regular expressions. Regular expressions are huge time-savers, not just for software users but also for programmers. In fact, tech writer Cory Doctorow argues that even before teaching programming, we should be teaching regular expressions:

“Knowing [regular expressions] can mean the difference between solving a problem in 3 steps and solving it in 3,000 steps. When you’re a nerd, you forget that the problems you solve with a couple keystrokes can take other people days of tedious, error-prone work to slog through.”[1]

In this chapter, you’ll start by writing a program to find text patterns without using regular expressions and then see how to use regular expressions to make the code much less bloated. I’ll show you basic matching with regular expressions and then move on to some more powerful features, such as string substitution and creating your own character classes. Finally, at the end of the chapter, you’ll write a program that can automatically extract phone numbers and email addresses from a block of text.

# Finding Patterns of Text Without Regular Expressions
Say you want to find a phone number in a string. You know the pattern: three numbers, a hyphen, three numbers, a hyphen, and four numbers. Here’s an example: 415-555-4242.

Let’s use a function named isPhoneNumber() to check whether a string matches this pattern, returning either True or False. Open a new file editor window and enter the following code; then save the file as isPhoneNumber.py:

```python
   def isPhoneNumber(text):
❶     if len(text) != 12:
           return False
       for i in range(0, 3):
❷         if not text[i].isdecimal():
               return False
❸     if text[3] != '-':
           return False
       for i in range(4, 7):
❹         if not text[i].isdecimal():
               return False
❺     if text[7] != '-':
           return False
       for i in range(8, 12):
❻         if not text[i].isdecimal():
               return False
❼     return True

   print('415-555-4242 is a phone number:')
   print(isPhoneNumber('415-555-4242'))
   print('Moshi moshi is a phone number:')
   print(isPhoneNumber('Moshi moshi'))
```
When this program is run, the output looks like this:

```python
415-555-4242 is a phone number:
True
Moshi moshi is a phone number:
False
```
The isPhoneNumber() function has code that does several checks to see whether the string in text is a valid phone number. If any of these checks fail, the function returns False. First the code checks that the string is exactly 12 characters ❶. Then it checks that the area code (that is, the first three characters in text) consists of only numeric characters ❷. The rest of the function checks that the string follows the pattern of a phone number: The number must have the first hyphen after the area code ❸, three more numeric characters ❹, then another hyphen ❺, and finally four more numbers ❻. If the program execution manages to get past all the checks, it returns True ❼.

Calling isPhoneNumber() with the argument '415-555-4242' will return True. Calling isPhoneNumber() with 'Moshi moshi' will return False; the first test fails because 'Moshi moshi' is not 12 characters long.

You would have to add even more code to find this pattern of text in a larger string. Replace the last four print() function calls in isPhoneNumber.py with the following:

```python
   message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
   for i in range(len(message)):
❶     chunk = message[i:i+12]
❷     if isPhoneNumber(chunk):
         print('Phone number found: ' + chunk)
   print('Done')
```
When this program is run, the output will look like this:


Phone number found: 415-555-1011
Phone number found: 415-555-9999
Done
On each iteration of the for loop, a new chunk of 12 characters from message is assigned to the variable chunk ❶. For example, on the first iteration, i is 0, and chunk is assigned message[0:12] (that is, the string 'Call me at 4'). On the next iteration, i is 1, and chunk is assigned message[1:13] (the string 'all me at 41').

You pass chunk to isPhoneNumber() to see whether it matches the phone number pattern ❷, and if so, you print the chunk.

Continue to loop through message, and eventually the 12 characters in chunk will be a phone number. The loop goes through the entire string, testing each 12-character piece and printing any chunk it finds that satisfies isPhoneNumber(). Once we’re done going through message, we print Done.

While the string in message is short in this example, it could be millions of characters long and the program would still run in less than a second. A similar program that finds phone numbers using regular expressions would also run in less than a second, but regular expressions make it quicker to write these programs.

