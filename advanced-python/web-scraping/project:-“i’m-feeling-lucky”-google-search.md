```ngMeta
name: project:-“i’m-feeling-lucky”-google-search
completionMethod: manual
```
# Project: “I’m Feeling Lucky” Google Search
Whenever I search a topic on Google, I don’t look at just one search result at a time. By middle-clicking a search result link (or clicking while holding CTRL), I open the first several links in a bunch of new tabs to read later. I search Google often enough that this workflow—opening my browser, searching for a topic, and middle-clicking several links one by one—is tedious. It would be nice if I could simply type a search term on the command line and have my computer automatically open a browser with all the top search results in new tabs. Let’s write a script to do this.

This is what your program does:

Gets search keywords from the command line arguments.

Retrieves the search results page.

Opens a browser tab for each result.

This means your code will need to do the following:

Read the command line arguments from sys.argv.

Fetch the search result page with the requests module.

Find the links to each search result.

Call the webbrowser.open() function to open the web browser.

Open a new file editor window and save it as lucky.py.

# Step 1: Get the Command Line Arguments and Request the Search Page
Before coding anything, you first need to know the URL of the search result page. By looking at the browser’s address bar after doing a Google search, you can see that the result page has a URL like <span><a href="https://www.google.com/search?q=SEARCH_TERM_HERE">https://www.google.com/search?q=SEARCH_TERM_HERE</a></span>. The requests module can download this page and then you can use Beautiful Soup to find the search result links in the HTML. Finally, you’ll use the webbrowser module to open those links in browser tabs.

Make your code look like the following:


	#! python3
	# lucky.py - Opens several Google search results.

import requests, sys, webbrowser, bs4

print('Googling...') # display text while downloading the Google page
res = requests.get(<span><a href="'http://google.com/search?q=' ">'http://google.com/search?q=' </a></span>+ ' '.join(sys.argv[1:]))
res.raise_for_status()

	# TODO: Retrieve top search result links.

	# TODO: Open a browser tab for each result.
The user will specify the search terms using command line arguments when they launch the program. These arguments will be stored as strings in a list in sys.argv.

# Step 2: Find All the Results
Now you need to use Beautiful Soup to extract the top search result links from your downloaded HTML. But how do you figure out the right selector for the job? For example, you can’t just search for all <a> tags, because there are lots of links you don’t care about in the HTML. Instead, you must inspect the search result page with the browser’s developer tools to try to find a selector that will pick out only the links you want.

After doing a Google search for Beautiful Soup, you can open the browser’s developer tools and inspect some of the link elements on the page. They look incredibly complicated, something like this: <a href="/url?sa =t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8& amp;ved=0CCgQFjAA&url=http%3A%2F%2Fwww.crummy.com%2Fsoftware%2FBeautifulSoup %2F&ei=LHBVU_XDD9KVyAShmYDwCw&usg=AFQjCNHAxwplurFOBqg5cehWQEVKi-TuLQ&a mp;sig2=sdZu6WVlBlVSDrwhtworMA" onmousedown="return rwt(this,'','','','1','AFQ jCNHAxwplurFOBqg5cehWQEVKi-TuLQ','sdZu6WVlBlVSDrwhtworMA','0CCgQFjAA','','',ev ent)" data-href="http://www.crummy.com/software/BeautifulSoup/"><em>Beautiful Soup</em>: We called him Tortoise because he taught us.</a>.

It doesn’t matter that the element looks incredibly complicated. You just need to find the pattern that all the search result links have. But this <a> element doesn’t have anything that easily distinguishes it from the nonsearch result <a> elements on the page.

Make your code look like the following:


	#! python3
	# lucky.py - Opens several google search results.

import requests, sys, webbrowser, bs4

--snip--

	# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text)

	# Open a browser tab for each result.
linkElems = soup.select('.r a')
If you look up a little from the <a> element, though, there is an element like this: <h3 class="r">. Looking through the rest of the HTML source, it looks like the r class is used only for search result links. You don’t have to know what the CSS class r is or what it does. You’re just going to use it as a marker for the <a> element you are looking for. You can create a BeautifulSoup object from the downloaded page’s HTML text and then use the selector '.r a' to find all <a> elements that are within an element that has the r CSS class.

# Step 3: Open Web Browsers for Each Result
Finally, we’ll tell the program to open web browser tabs for our results. Add the following to the end of your program:


 #! python3
 # lucky.py - Opens several google search results.

import requests, sys, webbrowser, bs4

--snip--

# Open a browser tab for each result.
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open(<span><a href="'http://google.com' ">'http://google.com' </a></span>+ linkElems[i].get('href'))
By default, you open the first five search results in new tabs using the webbrowser module. However, the user may have searched for something that turned up fewer than five results. The soup.select() call returns a list of all the elements that matched your '.r a' selector, so the number of tabs you want to open is either 5 or the length of this list (whichever is smaller).

The built-in Python function min() returns the smallest of the integer or float arguments it is passed. (There is also a built-in max() function that returns the largest argument it is passed.) You can use min() to find out whether there are fewer than five links in the list and store the number of links to open in a variable named numOpen. Then you can run through a for loop by calling range(numOpen).

On each iteration of the loop, you use webbrowser.open() to open a new tab in the web browser. Note that the href attribute’s value in the returned <a> elements do not have the initial <span><a href="http://google.com">http://google.com</a></span> part, so you have to concatenate that to the href attribute’s string value.

Now you can instantly open the first five Google results for, say, Python programming tutorials by running lucky python programming tutorials on the command line! (See Appendix B for how to easily run programs on your operating system.)