```ngMeta
name: creating-a-beautifulsoup-object-fromhtml
```
# Creating a BeautifulSoup Object from HTML
The bs4.BeautifulSoup() function needs to be called with a string containing the HTML it will parse. The bs4.BeautifulSoup() function returns is a BeautifulSoup object. Enter the following into the interactive shell while your computer is connected to the Internet:

```python
>>> import requests, bs4
>>> res = requests.get('http://nostarch.com')
>>> res.raise_for_status()
>>> noStarchSoup = bs4.BeautifulSoup(res.text)
>>> type(noStarchSoup)
```
<class 'bs4.BeautifulSoup'>
This code uses requests.get() to download the main page from the No Starch Press website and then passes the text attribute of the response to bs4.BeautifulSoup(). The BeautifulSoup object that it returns is stored in a variable named noStarchSoup.

You can also load an HTML file from your hard drive by passing a File object to bs4.BeautifulSoup(). Enter the following into the interactive shell (make sure the example.html file is in the working directory):

```python
>>> exampleFile = open('example.html')
>>> exampleSoup = bs4.BeautifulSoup(exampleFile)
>>> type(exampleSoup)
```
<class 'bs4.BeautifulSoup'>
Once you have a BeautifulSoup object, you can use its methods to locate specific parts of an HTML document.

# Finding an Element with the select() Method
You can retrieve a web page element from a BeautifulSoup object by calling the select()method and passing a string of a CSS selector for the element you are looking for. Selectors are like regular expressions: They specify a pattern to look for, in this case, in HTML pages instead of general text strings.

A full discussion of CSS selector syntax is beyond the scope of this book (there’s a good selector tutorial in the resources at <span><a href="http://nostarch.com/automatestuff/">http://nostarch.com/automatestuff/</a></span>), but here’s a short introduction to selectors. Table 11-2 shows examples of the most common CSS selector patterns.

Table 11-2. Examples of CSS Selectors

Selector passed to the select() method

Will match...

soup.select('div')							All elements named <div>

soup.select('#author')						The element with an id attribute of author

soup.select('.notice')						All elements that use a CSS class attribute named notice

soup.select('div span')						All elements named <span> that are within an element named <div>

soup.select('div > span')					All elements named <span> that are directly within an element named <div>, with no other element in between

soup.select('input[name]')					All elements named <input> that have a name attribute with any value

soup.select('input[type="button"]')			All elements named <input> that have an attribute named type with value button

The various selector patterns can be combined to make sophisticated matches. For example, soup.select('p #author') will match any element that has an id attribute of author, as long as it is also inside a <p> element.

The select() method will return a list of Tag objects, which is how Beautiful Soup represents an HTML element. The list will contain one Tag object for every match in the BeautifulSoup object’s HTML. Tag values can be passed to the str() function to show the HTML tags they represent. Tag values also have an attrs attribute that shows all the HTML attributes of the tag as a dictionary. Using the example.html file from earlier, enter the following into the interactive shell:

```python
>>> import bs4
>>> exampleFile = open('example.html')
>>> exampleSoup = bs4.BeautifulSoup(exampleFile.read())
>>> elems = exampleSoup.select('#author')
>>> type(elems)
```
<class 'list'>
```python
>>> len(elems)
```
1
```python
>>> type(elems[0])
```
<class 'bs4.element.Tag'>
```
>>> elems[0].getText()
```
'Al Sweigart'
```
>>> str(elems[0])
```
'<span id="author">Al Sweigart</span>'
```python
>>> elems[0].attrs
```
{'id': 'author'}
This code will pull the element with id="author" out of our example HTML. We use select('#author') to return a list of all the elements with id="author". We store this list of Tag objects in the variable elems, and len(elems) tells us there is one Tag object in the list; there was one match. Calling getText() on the element returns the element’s text, or inner HTML. The text of an element is the content between the opening and closing tags: in this case, 'Al Sweigart'.

Passing the element to str() returns a string with the starting and closing tags and the element’s text. Finally, attrs gives us a dictionary with the element’s attribute, 'id', and the value of the id attribute, 'author'.

You can also pull all the <p> elements from the BeautifulSoup object. Enter this into the interactive shell:

```python
>>> pElems = exampleSoup.select('p')
>>> str(pElems[0])
```
'<p>Download my <strong>Python</strong> book from <a href="http://
inventwithpython.com">my website</a>.</p>'
```python
>>> pElems[0].getText()
```
'Download my Python book from my website.'
```python
>>> str(pElems[1])
```
'<p class="slogan">Learn Python the easy way!</p>'
```python
>>> pElems[1].getText()
```
'Learn Python the easy way!'
```python
>>> str(pElems[2])
```
'<p>By <span id="author">Al Sweigart</span></p>'
```python
>>> pElems[2].getText()
```
'By Al Sweigart'
This time, select() gives us a list of three matches, which we store in pElems. Using str() on pElems[0], pElems[1], and pElems[2] shows you each element as a string, and using getText() on each element shows you its text.
# Getting Data from an Element’s Attributes
The get() method for Tag objects makes it simple to access attribute values from an element. The method is passed a string of an attribute name and returns that attribute’s value. Using example.html, enter the following into the interactive shell:

```python
>>> import bs4
>>> soup = bs4.BeautifulSoup(open('example.html'))
>>> spanElem = soup.select('span')[0]
>>> str(spanElem)
```
'<span id="author">Al Sweigart</span>'
```python
>>> spanElem.get('id')
```
'author'
```python
>>> spanElem.get('some_nonexistent_addr') == None
```
True
```python
>>> spanElem.attrs
```
{'id': 'author'}
Here we use select() to find any <span> elements and then store the first matched element in spanElem. Passing the attribute name 'id' to get() returns the attribute’s value, 'author'.