```ngMeta
name: clicking-the-page
completionMethod: manual
```
# Clicking the Page
WebElement objects returned from the find_element_* and find_elements_* methods have a click() method that simulates a mouse click on that element. This method can be used to follow a link, make a selection on a radio button, click a Submit button, or trigger whatever else might happen when the element is clicked by the mouse. For example, enter the following into the interactive shell:

```python
>>> from selenium import webdriver
>>> browser = webdriver.Firefox()
>>> browser.get('http://inventwithpython.com')
>>> linkElem = browser.find_element_by_link_text('Read It Online')
>>> type(linkElem)
```
<class 'selenium.webdriver.remote.webelement.WebElement'>
```python
>>> linkElem.click() # follows the "Read It Online" link
```
This opens Firefox to <span><a href="http://inventwithpython.com/">http://inventwithpython.com/</a></span>, gets the WebElement object for the <a> element with the text Read It Online, and then simulates clicking that <a> element. It’s just like if you clicked the link yourself; the browser then follows that link.

