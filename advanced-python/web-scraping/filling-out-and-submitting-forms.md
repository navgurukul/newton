```ngMeta
name: filling-out-and-submitting-forms
completionMethod: manual
```
# Filling Out and Submitting Forms
Sending keystrokes to text fields on a web page is a matter of finding the <input> or <textarea> element for that text field and then calling the send_keys() method. For example, enter the following into the interactive shell:

```python
>>> from selenium import webdriver
>>> browser = webdriver.Firefox()
>>> browser.get('https://mail.yahoo.com')
>>> emailElem = browser.find_element_by_id('login-username')
>>> emailElem.send_keys('not_my_real_email')
>>> passwordElem = browser.find_element_by_id('login-passwd')
>>> passwordElem.send_keys('12345')
>>> passwordElem.submit()
```
As long as Gmail hasn’t changed the id of the Username and Password text fields since this book was published, the previous code will fill in those text fields with the provided text. (You can always use the browser’s inspector to verify the id.) Calling the submit() method on any element will have the same result as clicking the Submit button for the form that element is in. (You could have just as easily called emailElem.submit(), and the code would have done the same thing.)

# Sending Special Keys
Selenium has a module for keyboard keys that are impossible to type into a string value, which function much like escape characters. These values are stored in attributes in the selenium.webdriver.common.keys module. Since that is such a long module name, it’s much easier to run from selenium.webdriver.common.keys import Keys at the top of your program; if you do, then you can simply write Keys anywhere you’d normally have to write selenium.webdriver.common.keys. Table 11-5 lists the commonly used Keys variables.

Table 11-5. Commonly Used Variables in the selenium.webdriver.common.keys Module

Attributes 												Meanings

Keys.DOWN, Keys.UP, Keys.LEFT, Keys.RIGHT 				The keyboard arrow keys

Keys.ENTER, Keys.RETURN 								The ENTER and RETURN keys

Keys.HOME, Keys.END, Keys.PAGE_DOWN, Keys.PAGE_UP 		The home, end, pagedown, and pageup keys

Keys.ESCAPE, Keys.BACK_SPACE, Keys.DELETE                The ESC, BACKSPACE, and DELETE keys

Keys.F1, Keys.F2,..., Keys.F12                           The F1 to F12 keys at the top of the keyboard

Keys.TAB                                                 The TAB key

For example, if the cursor is not currently in a text field, pressing the HOME and END keys will scroll the browser to the top and bottom of the page, respectively. Enter the following into the interactive shell, and notice how the send_keys() calls scroll the page:

```python
>>> from selenium import webdriver
>>> from selenium.webdriver.common.keys import Keys
>>> browser = webdriver.Firefox()
>>> browser.get('http://nostarch.com')
>>> htmlElem = browser.find_element_by_tag_name('html')
>>> htmlElem.send_keys(Keys.END)     # scrolls to bottom
>>> htmlElem.send_keys(Keys.HOME)    # scrolls to top
```
The <html> tag is the base tag in HTML files: The full content of the HTML file is enclosed within the <html> and </html> tags. Calling browser.find_element_by_tag_name('html') is a good place to send keys to the general web page. This would be useful if, for example, new content is loaded once you’ve scrolled to the bottom of the page.

