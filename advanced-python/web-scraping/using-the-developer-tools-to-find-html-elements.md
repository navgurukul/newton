```ngMeta
name: using-the-developer-tools-to-find-html-elements
```
# Using the Developer Tools to Find HTML Elements
Once your program has downloaded a web page using the requests module, you will have the page’s HTML content as a single string value. Now you need to figure out which part of the HTML corresponds to the information on the web page you’re interested in.

This is where the browser’s developer tools can help. Say you want to write a program to pull weather forecast data from <span><a href="http://weather.gov/.">http://weather.gov/.</a></span> Before writing any code, do a little research. If you visit the site and search for the 94105 ZIP code, the site will take you to a page showing the forecast for that area.

What if you’re interested in scraping the temperature information for that ZIP code? Right-click where it is on the page (or CONTROL-click on OS X) and select Inspect Element from the context menu that appears. This will bring up the Developer Tools window, which shows you the HTML that produces this particular part of the web page. Figure 11-5 shows the developer tools open to the HTML of the temperature.

<!-- ![](assets/000014.jpg)
 -->
Inspecting the element that holds the temperature text with the developer tools

From the developer tools, you can see that the HTML responsible for the temperature part of the web page is <p class="myforecast-current -lrg">59°F</p>. This is exactly what you were looking for! It seems that the temperature information is contained inside a <p> element with the myforecast-current-lrg class. Now that you know what you’re looking for, the BeautifulSoup module will help you find it in the string.

# Parsing HTML with the BeautifulSoup Module
Beautiful Soup is a module for extracting information from an HTML page (and is much better for this purpose than regular expressions). The BeautifulSoup module’s name is bs4 (for Beautiful Soup, version 4). To install it, you will need to run pip install beautifulsoup4 from the command line. (Check out Appendix A for instructions on installing third-party modules.) While beautifulsoup4 is the name used for installation, to import Beautiful Soup you run import bs4.

For this chapter, the Beautiful Soup examples will parse (that is, analyze and identify the parts of) an HTML file on the hard drive. Open a new file editor window in IDLE, enter the following, and save it as example.html. Alternatively, download it from http://nostarch.com/automatestuff/.


<!-- This is the example.html example file. -->

<html><head><title>The Website Title</title></head>
<body>
<p>Download my <strong>Python</strong> book from <a href="http://
inventwithpython.com">my website</a>.</p>
<p class="slogan">Learn Python the easy way!</p>
<p>By <span id="author">Al Sweigart</span></p>
</body></html>
As you can see, even a simple HTML file involves many different tags and attributes, and matters quickly get confusing with complex websites. Thankfully, Beautiful Soup makes working with HTML much easier.

