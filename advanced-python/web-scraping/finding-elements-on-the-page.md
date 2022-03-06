```ngMeta
name: finding-elements-on-the-page
```
# Finding Elements on the Page
WebDriver objects have quite a few methods for finding elements on a page. They are divided into the find_element_* and find_elements_* methods. The find_element_* methods return a single WebElement object, representing the first element on the page that matches your query. The find_elements_* methods return a list of WebElement_* objects for every matching element on the page.

Table 11-3 shows several examples of find_element_* and find_elements_* methods being called on a WebDriver object that’s stored in the variable browser.

Table 11-3. Selenium’s WebDriver Methods for Finding Elements

Method name

WebElement object/list returned

 browser.find_element_by_class_name(name)
browser.find_elements_by_class_name(name)
Elements that use the CSS class name

 browser.find_element_by_css_selector(selector)
browser.find_elements_by_css_selector(selector)
Elements that match the CSS selector

 browser.find_element_by_id(id)
browser.find_elements_by_id(id)
Elements with a matching id attribute value

 browser.find_element_by_link_text(text)
browser.find_elements_by_link_text(text)
<a> elements that completely match the text provided

 browser.find_element_by_partial_link_text(text)
browser.find_elements_by_partial_link_text(text)
<a> elements that contain the text provided

 browser.find_element_by_name(name)
browser.find_elements_by_name(name)
Elements with a matching name attribute value

 browser.find_element_by_tag_name(name)
browser.find_elements_by_tag_name(name)
Elements with a matching tag name (case insensitive; an <a> element is matched by 'a' and 'A')

Except for the *_by_tag_name() methods, the arguments to all the methods are case sensitive. If no elements exist on the page that match what the method is looking for, the selenium module raises a NoSuchElement exception. If you do not want this exception to crash your program, add try and except statements to your code.
Once you have the WebElement object, you can find out more about it by reading the attributes or calling the methods in Table 11-4.
Table 11-4. WebElement Attributes and Methods
Attribute or method 								Description
tag_name 											The tag name, such as 'a' for an <a> element
get_attribute(name) 								The value for the element’s name attribute
text 												The text within the element, such as 'hello' in <span>hello</span>
clear()												For text field or text area elements, clears the text typed into it
is_displayed() 										Returns True if the element is visible; otherwise returns False
is_enabled() 										For input elements, returns True if the element is enabled; otherwise returns False
is_selected()										For checkbox or radio button elements, returns True if the element is selected; otherwise returns False
location											A dictionary with keys 'x' and 'y' for the position of the element in the page
For example, open a new file editor and enter the following program:
from selenium import webdriver
browser = webdriver.Firefox()
browser.get('<span><a href="http://inventwithpython.com'">http://inventwithpython.com'</a></span>)
try:
    elem = browser.find_element_by_class_name('bookcover')
    print('Found <%s> element with that class name!' % (elem.tag_name))
except:
    print('Was not able to find an element with that name.')
Here we open Firefox and direct it to a URL. On this page, we try to find elements with the class name 'bookcover', and if such an element is found, we print its tag name using the tag_name attribute. If no such element was found, we print a different message.
This program will output the following:
Found <img> element with that class name!
We found an element with the class name 'bookcover' and the tag name 'img'.
