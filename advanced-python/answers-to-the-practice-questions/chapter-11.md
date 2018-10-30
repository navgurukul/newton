```ngMeta
name: chapter-11
completionMethod: manual
```
# Chapter 11
The webbrowser module has an open() method that will launch a web browser to a specific URL, and that’s it. The requests module can download files and pages from the Web. The BeautifulSoup module parses HTML. Finally, the selenium module can launch and control a browser.

The requests.get() function returns a Response object, which has a text attribute that contains the downloaded content as a string.

The raise_for_status() method raises an exception if the download had problems and does nothing if the download succeeded.

The status_code attribute of the Response object contains the HTTP status code.

After opening the new file on your computer in 'wb' “write binary” mode, use a for loop that iterates over the Response object’s iter_content() method to write out chunks to the file. Here’s an example:


saveFile = open('filename.html', 'wb')
for chunk in res.iter_content(100000):
    saveFile.write(chunk)
F12 brings up the developer tools in Chrome. Pressing CTRL-SHIFT-C (on Windows and Linux) or ⌘-OPTION-C (on OS X) brings up the developer tools in Firefox.

Right-click the element in the page, and select Inspect Element from the menu.

'#main'

'.highlight'

'div div'

'button[value="favorite"]'

spam.getText()

linkElem.attrs

The selenium module is imported with from selenium import webdriver.

The find_element_* methods return the first matching element as a WebElement object. The find_elements_* methods return a list of all matching elements as WebElement objects.

The click() and send_keys() methods simulate mouse clicks and keyboard keys, respectively.

Calling the submit() method on any element within a form submits the form.

The forward(), back(), and refresh() WebDriver object methods simulate these browser buttons.