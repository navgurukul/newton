using-the-developer-tools-to-find-html-elements_key1
using-the-developer-tools-to-find-html-elements_key2


using-the-developer-tools-to-find-html-elements_key3


using-the-developer-tools-to-find-html-elements_key4


![](assets/000014.jpg)
 -->
Inspecting the element that holds the temperature text with the developer tools

From the developer tools, you can see that the HTML responsible for the temperature part of the web page is <p class="myforecast-current -lrg">59°F</p>. This is exactly what you were looking for! It seems that the temperature information is contained inside a <p> element with the myforecast-current-lrg class. Now that you know what you’re looking for, the BeautifulSoup module will help you find it in the string.

# Parsing HTML with the BeautifulSoup Module
Beautiful Soup is a module for extracting information from an HTML page (and is much better for this purpose than regular expressions). The BeautifulSoup module’s name is bs4 (for Beautiful Soup, version 4). To install it, you will need to run pip install beautifulsoup4 from the command line. (Check out Appendix A for instructions on installing third-party modules.) While beautifulsoup4 is the name used for installation, to import Beautiful Soup you run import bs4.

For this chapter, the Beautiful Soup examples will parse (that is, analyze and identify the parts of)using-the-developer-tools-to-find-html-elements_key5



