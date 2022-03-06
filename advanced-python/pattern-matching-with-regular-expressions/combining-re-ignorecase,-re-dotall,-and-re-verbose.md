```ngMeta
name: combining-re-ignorecase,-re-dotall,-and-re-verbose
```
# Combining re.IGNORECASE, re.DOTALL, and re.VERBOSE
What if you want to use re.VERBOSE to write comments in your regular expression but also want to use re.IGNORECASE to ignore capitalization? Unfortunately, the re.compile() function takes only a single value as its second argument. You can get around this limitation by combining the re.IGNORECASE, re.DOTALL, and re.VERBOSE variables using the pipe character (|), which in this context is known as the bitwise or operator.

So if you want a regular expression that’s case-insensitive and includes newlines to match the dot character, you would form your re.compile() call like this:

```python
>>> someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL)
```
All three options for the second argument will look like this:

```python
>>> someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)
```
This syntax is a little old-fashioned and originates from early versions of Python. The details of the bitwise operators are beyond the scope of this book, but check out the resources at <span><a href="http://nostarch.com/automatestuff/">http://nostarch.com/automatestuff/</a></span> for more information. You can also pass other options for the second argument; they’re uncommon, but you can read more about them in the resources, too.