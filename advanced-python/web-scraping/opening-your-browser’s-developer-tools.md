```ngMeta
name: opening-your-browser’s-developer-tools
```
# Opening Your Browser’s Developer Tools
In addition to viewing a web page’s source, you can look through a page’s HTML using your browser’s developer tools. In Chrome and Internet Explorer for Windows, the developer tools are already installed, and you can press F12 to make them appear (see Figure 11-4). Pressing F12 again will make the developer tools disappear. In Chrome, you can also bring up the developer tools by selecting View▸Developer▸Developer Tools. In OS X, pressing -OPTION-I will open Chrome’s Developer Tools.

<!-- ![image](assets/000095.jpg)
 -->
The Developer Tools window in the Chrome browser

In Firefox, you can bring up the Web Developer Tools Inspector by pressing CTRL-SHIFT-C on Windows and Linux or by pressing ⌘-OPTION-C on OS X. The layout is almost identical to Chrome’s developer tools.

In Safari, open the Preferences window, and on the Advanced pane check the Show Develop menu in the menu bar option. After it has been enabled, you can bring up the developer tools by pressing -OPTION-I.

After enabling or installing the developer tools in your browser, you can right-click any part of the web page and select Inspect Element from the context menu to bring up the HTML responsible for that part of the page. This will be helpful when you begin to parse HTML for your web scraping programs.

Don’t Use Regular Expressions to Parse HTML

Locating a specific piece of HTML in a string seems like a perfect case for regular expressions. However, I advise you against it. There are many different ways that HTML can be formatted and still be considered valid HTML, but trying to capture all these possible variations in a regular expression can be tedious and error prone. A module developed specifically for parsing HTML, such as Beautiful Soup, will be less likely to result in bugs.

You can find an extended argument for why you shouldn’t to parse HTML with regular expressions at <span><a href="http://stackoverflow.com/a/1732454/1893164/.">http://stackoverflow.com/a/1732454/1893164/</a></span>
