```ngMeta
name: controlling-the-browser-with-the-selenium-module
```
# Controlling the Browser with the selenium Module
The selenium module lets Python directly control the browser by programmatically clicking links and filling in login information, almost as though there is a human user interacting with the page. Selenium allows you to interact with web pages in a much more advanced way than Requests and Beautiful Soup; but because it launches a web browser, it is a bit slower and hard to run in the background if, say, you just need to download some files from the Web.

Appendix A has more detailed steps on installing third-party modules.

# Starting a Selenium-Controlled Browser
For these examples, you’ll need the Firefox web browser. This will be the browser that you control. If you don’t already have Firefox, you can download it for free from <span><a href=" http://getfirefox.com/."> http://getfirefox.com/.</a></span>

Importing the modules for Selenium is slightly tricky. Instead of import selenium, you need to run from selenium import webdriver. (The exact reason why the selenium module is set up this way is beyond the scope of this book.) After that, you can launch the Firefox browser with Selenium. Enter the following into the interactive shell:

```python
>>> from selenium import webdriver
>>> browser = webdriver.Firefox()
>>> type(browser)
```
<class 'selenium.webdriver.firefox.webdriver.WebDriver'>
```python
>>> browser.get('http://inventwithpython.com')
```
You’ll notice when webdriver.Firefox() is called, the Firefox web browser starts up. Calling type() on the value webdriver.Firefox() reveals it’s of the WebDriver data type. And calling browser.get(<span><a href="http://inventwithpython.com">http://inventwithpython.com</a></span>) directs the browser to <span><a href="http://inventwithpython.com/.">http://inventwithpython.com/.</a></span> Your browser should look something like Figure
```python
<<<<<<< HEAD
```

<!-- ![image](assets/000018.jpg)
 -->
```python
=======
```

<!-- ![image](assets/000018.jpg)
 -->
```python
>>>>>>> e7c92b8136151bdc6c9b42ea47eaf1dc7cfdbe70
```

After calling webdriver.Firefox() and get() in IDLE, the Firefox browser appears.

