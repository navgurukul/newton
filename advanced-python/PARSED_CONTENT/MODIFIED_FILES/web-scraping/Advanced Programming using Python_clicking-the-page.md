clicking-the-page_key1
clicking-the-page_key2


```python
>>> from selenium import webdriver
>>> browser = webdriver.Firefox()
>>> browser.get('http://inventwithpython.com')
>>> linkElem = browser.find_element_by_link_text('Read It Online')
>>> type(linkElem)
```
clicking-the-page_key3
```python
>>> linkElem.click() # follows the "Read It Online" link
```
clicking-the-page_key4
