```ngMeta
name: ideas-for-similar-programs
completionMethod: manual
```
# Ideas for Similar Programs
As long as you have a URL, the webbrowser module lets users cut out the step of opening the browser and directing themselves to a website. Other programs could use this functionality to do the following:

Open all links on a page in separate browser tabs.

Open the browser to the URL for your local weather.

Open several social network sites that you regularly check.

# Downloading Files from the Web with the requests Module
The requests module lets you easily download files from the Web without having to worry about complicated issues such as network errors, connection problems, and data compression. The requests module doesn’t come with Python, so you’ll have to install it first. From the command line, run pip install requests. (Appendix A has additional details on how to install third-party modules.)

The requests module was written because Python’s urllib2 module is too complicated to use. In fact, take a permanent marker and black out this entire paragraph. Forget I ever mentioned urllib2. If you need to download things from the Web, just use the requests module.

Next, do a simple test to make sure the requests module installed itself correctly. Enter the following into the interactive shell:

```python
>>> import requests
```
If no error messages show up, then the requests module has been successfully installed.

# Downloading a Web Page with the requests.get() Function
The requests.get() function takes a string of a URL to download. By calling type() on requests.get()’s return value, you can see that it returns a Response object, which contains the response that the web server gave for your request. I’ll explain the Response object in more detail later, but for now, enter the following into the interactive shell while your computer is connected to the Internet:

```python
   >>> import requests
   >>> res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
   >>> type(res)
```
   <class 'requests.models.Response'>
```python
❶ >>> res.status_code == requests.codes.ok
```
   True
```python
   >>> len(res.text)
```
   178981
```python
   >>> print(res.text[:250])
```
   The Project Gutenberg EBook of Romeo and Juliet, by William Shakespeare

   This eBook is for the use of anyone anywhere at no cost and with
   almost no restrictions whatsoever. You may copy it, give it away or
   re-use it under the terms of the Proje
The URL goes to a text web page for the entire play of Romeo and Juliet. You can tell that the request for this web page succeeded by checking the status_code attribute of the Response object. If it is equal to the value of requests.codes.ok, then everything went fine ❶. (Incidentally, the status code for “OK” in the HTTP protocol is 200. You may already be familiar with the 404 status code for “Not Found.”)

If the request succeeded, the downloaded web page is stored as a string in the Response object’s text variable. This variable holds a large string of the entire play; the call to len(res.text) shows you that it is more than 178,000 characters long. Finally, calling print(res.text[:250]) displays only the first 250 characters.

