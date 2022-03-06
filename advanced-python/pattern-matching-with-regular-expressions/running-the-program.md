```ngMeta
name: running-the-program
```
# Running the Program
For an example, open your web browser to the No Starch Press contact page at http://www.nostarch.com/contactus.htm, press CTRL-A to select all the text on the page, and press CTRL-C to copy it to the clipboard. When you run this program, the output will look something like this:


Copied to clipboard:
800-420-7240
415-863-9900
415-863-9950
info@nostarch.com
media@nostarch.com
academic@nostarch.com
help@nostarch.com
Ideas for Similar Programs
Identifying patterns of text (and possibly substituting them with the sub() method) has many different potential applications.

Find website URLs that begin with http:// or https://.

Clean up dates in different date formats (such as 3/14/2015, 03-14-2015, and 2015/3/14) by replacing them with dates in a single, standard format.

Remove sensitive information such as Social Security or credit card numbers.

Find common typos such as multiple spaces between words, accidentally accidentally repeated words, or multiple exclamation marks at the end of sentences. Those are annoying!!

# Summary
While a computer can search for text quickly, it must be told precisely what to look for. Regular expressions allow you to specify the precise patterns of characters you are looking for. In fact, some word processing and spreadsheet applications provide find-and-replace features that allow you to search using regular expressions.

The re module that comes with Python lets you compile Regex objects. These values have several methods: search() to find a single match, findall() to find all matching instances, and sub() to do a find-and-replace substitution of text.

There’s a bit more to regular expression syntax than is described in this chapter. You can find out more in the official Python documentation at <span><a href="http://docs.python.org/3/library/re.html.">http://docs.python.org/3/library/re.html.</a></span> The tutorial website <span><a href="http://www.regular-expressions.info/ ">http://www.regular-expressions.info/ </a></span> is also a useful resource.

Now that you have expertise manipulating and matching strings, it’s time to dive into how to read from and write to files on your computer’s hard drive.

