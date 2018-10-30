```ngMeta
name: html
completionMethod: manual
```
#HTML
Before you pick apart web pages, you’ll learn some HTML basics. You’ll also see how to access your web browser’s powerful developer tools, which will make scraping information from the Web much easier.

#Resources for Learning HTML
Hypertext Markup Language (HTML) is the format that web pages are written in. This chapter assumes you have some basic experience with HTML, but if you need a beginner tutorial, I suggest one of the following sites:

<span><a href="http://htmldog.com/guides/html/beginner/">http://htmldog.com/guides/html/beginner/</a></span>

<span><a href="http://www.codecademy.com/tracks/web/">http://www.codecademy.com/tracks/web/</a></span>

<span><a href="https://developer.mozilla.org/en-US/learn/html/">https://developer.mozilla.org/en-US/learn/html/</a></span>

#A Quick Refresher
In case it’s been a while since you’ve looked at any HTML, here’s a quick overview of the basics. An HTML file is a plaintext file with the .html file extension. The text in these files is surrounded by tags, which are words enclosed in angle brackets. The tags tell the browser how to format the web page. A starting tag and closing tag can enclose some text to form an element. The text (or inner HTML) is the content between the starting and closing tags. For example, the following HTML will display Hello world! in the browser, with Hello in bold:


<strong>Hello</strong> world!
This HTML will look like Figure 11-1 in a browser.

<!-- ![](assets/000005.jpg)
 -->
Hello world! rendered in the browser

The opening <strong> tag says that the enclosed text will appear in bold. The closing </strong> tags tells the browser where the end of the bold text is.

There are many different tags in HTML. Some of these tags have extra properties in the form of attributes within the angle brackets. For example, the <a> tag encloses text that should be a link. The URL that the text links to is determined by the href attribute. Here’s an example:


Al's free <a href="http://inventwithpython.com">Python books</a>.
This HTML will look like Figure 11-2 in a browser.

<!-- ![](assets/000007.jpg)
 -->
The link rendered in the browser

Some elements have an id attribute that is used to uniquely identify the element in the page. You will often instruct your programs to seek out an element by its id attribute, so figuring out an element’s id attribute using the browser’s developer tools is a common task in writing web scraping programs.
#Viewing the Source HTML of a Web Page
You’ll need to look at the HTML source of the web pages that your programs will work with. To do this, right-click (or CTRL-click on OS X) any web page in your web browser, and select View Source or View page source to see the HTML text of the page (see Figure 11-3). This is the text your browser actually receives. The browser knows how to display, or render, the web page from this HTML.

<!-- ![](assets/000009.jpg)
 -->
Viewing the source of a web page

I highly recommend viewing the source HTML of some of your favorite sites. It’s fine if you don’t fully understand what you are seeing when you look at the source. You won’t need HTML mastery to write simple web scraping programs—after all, you won’t be writing your own websites. You just need enough knowledge to pick out data from an existing site.