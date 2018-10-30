```ngMeta
name: ideas-for-similar-programs_2
completionMethod: manual
```
# Ideas for Similar Programs
The benefit of tabbed browsing is that you can easily open links in new tabs to peruse later. A program that automatically opens several links at once can be a nice shortcut to do the following:

Open all the product pages after searching a shopping site such as Amazon

Open all the links to reviews for a single product

Open the result links to photos after performing a search on a photo site such as Flickr or Imgur

# Project: Downloading All XKCD Comics
Blogs and other regularly updating websites usually have a front page with the most recent post as well as a Previous button on the page that takes you to the previous post. Then that post will also have a Previous button, and so on, creating a trail from the most recent page to the first post on the site. If you wanted a copy of the site’s content to read when you’re not online, you could manually navigate over every page and save each one. But this is pretty boring work, so let’s write a program to do it instead.

XKCD is a popular geek webcomic with a website that fits this structure (see Figure 11-6). The front page at <span><a href="http://xkcd.com/">http://xkcd.com/</a></span> has a Prev button that guides the user back through prior comics. Downloading each comic by hand would take forever, but you can write a script to do this in a couple of minutes.

Here’s what your program does:

Loads the XKCD home page.

Saves the comic image on that page.

Follows the Previous Comic link.

Repeats until it reaches the first comic.

<!-- ![image](asseta/000016.jpg)
 -->
 “a webcomic of romance, sarcasm, math, and language”

This means your code will need to do the following:

Download pages with the requests module.

Find the URL of the comic image for a page using Beautiful Soup.

Download and save the comic image to the hard drive with iter_content().

Find the URL of the Previous Comic link, and repeat.

Open a new file editor window and save it as downloadXkcd.py.
# Step 1: Design the Program
If you open the browser’s developer tools and inspect the elements on the page, you’ll find the following:

The URL of the comic’s image file is given by the href attribute of an <img> element.

The <img> element is inside a <div id="comic"> element.

The Prev button has a rel HTML attribute with the value prev.

The first comic’s Prev button links to the <span><a href="http://xkcd.com/#">http://xkcd.com/#</a></span> URL, indicating that there are no more previous pages.

Make your code look like the following:


#! python3
# downloadXkcd.py - Downloads every single XKCD comic.

import requests, os, bs4

url = <span><a href="'http://xkcd.com'">'http://xkcd.com'</a></span>            
  # starting url
os.makedirs('xkcd', exist_ok=True)   # store comics in ./xkcd
while not url.endswith('#'):
    # TODO: Download the page.

    # TODO: Find the URL of the comic image.

    # TODO: Download the image.

    # TODO: Save the image to ./xkcd.

    # TODO: Get the Prev button's url.

print('Done.')
You’ll have a url variable that starts with the value 'http://xkcd.com' and repeatedly update it (in a for loop) with the URL of the current page’s Prev link. At every step in the loop, you’ll download the comic at url. You’ll know to end the loop when url ends with '#'.

You will download the image files to a folder in the current working directory named xkcd. The call os.makedirs() ensures that this folder exists, and the exist_ok=True keyword argument prevents the function from throwing an exception if this folder already exists. The rest of the code is just comments that outline the rest of your program.

# Step 2: Download the Web Page
Let’s implement the code for downloading the page. Make your code look like the following:


#! python3
# downloadXkcd.py - Downloads every single XKCD comic.

import requests, os, bs4

url = <span><a href="'http://xkcd.com'">'http://xkcd.com'</a></span>              
	# starting url
os.makedirs('xkcd', exist_ok=True)   # store comics in ./xkcd
while not url.endswith('#'):
```python
    # Download the page.
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)
```
    # TODO: Find the URL of the comic image.

    # TODO: Download the image.

    # TODO: Save the image to ./xkcd.

    # TODO: Get the Prev button's url.

print('Done.')
First, print url so that the user knows which URL the program is about to download; then use the requests module’s request.get() function to download it. As always, you immediately call the Response object’s raise_for_status() method to throw an exception and end the program if something went wrong with the download. Otherwise, you create a BeautifulSoup object from the text of the downloaded page.

# Step 3: Find and Download the Comic Image
Make your code look like the following:


#! python3
# downloadXkcd.py - Downloads every single XKCD comic.

import requests, os, bs4

--snip--
```python
    # Find the URL of the comic image.
    comicElem = soup.select('#comic img')
    if comicElem == []:
         print('Could not find comic image.')
    else:
         try:
             comicUrl = 'http:' + comicElem[0].get('src')
             # Download the image.
             print('Downloading image %s...' % (comicUrl))
             res = requests.get(comicUrl)
             res.raise_for_status()
         except requests.exceptions.MissingSchema:
             # skip this comic
             prevLink = soup.select('a[rel="prev"]')[0]
             url = 'http://xkcd.com' + prevLink.get('href')
             continue
```

    # TODO: Save the image to ./xkcd.

    # TODO: Get the Prev button's url.

print('Done.')
From inspecting the XKCD home page with your developer tools, you know that the <img> element for the comic image is inside a <div> element with the id attribute set to comic, so the selector '#comic img' will get you the correct <img> element from the BeautifulSoup object.

A few XKCD pages have special content that isn’t a simple image file. That’s fine; you’ll just skip those. If your selector doesn’t find any elements, then soup.select('#comic img') will return a blank list. When that happens, the program can just print an error message and move on without downloading the image.

Otherwise, the selector will return a list containing one <img> element. You can get the src attribute from this <img> element and pass it to requests.get() to download the comic’s image file.

# Step 4: Save the Image and Find the Previous Comic
Make your code look like the following:


    #! python3
    # downloadXkcd.py - Downloads every single XKCD comic.

import requests, os, bs4

--snip--
```python
        # Save the image to ./xkcd.
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    # Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')
```
print('Done.')
At this point, the image file of the comic is stored in the res variable. You need to write this image data to a file on the hard drive.

You’ll need a filename for the local image file to pass to open(). The comicUrl will have a value like <span><a href="'http://imgs.xkcd.com/comics/heartbleed_explanation.png'—which ">'http://imgs.xkcd.com/comics/heartbleed_explanation.png'—which </a></span> you might have noticed looks a lot like a file path. And in fact, you can call os.path.basename() with comicUrl, and it will return just the last part of the URL, 'heartbleed_explanation.png'. You can use this as the filename when saving the image to your hard drive. You join this name with the name of your xkcd folder using os.path.join() so that your program uses backslashes (\) on Windows and forward slashes (/) on OS X and Linux. Now that you finally have the filename, you can call open() to open a new file in 'wb' “write binary” mode.

Remember from earlier in this chapter that to save files you’ve downloaded using Requests, you need to loop over the return value of the iter_content() method. The code in the for loop writes out chunks of the image data (at most 100,000 bytes each) to the file and then you close the file. The image is now saved to your hard drive.

Afterward, the selector 'a[rel="prev"]' identifies the <a> element with the rel attribute set to prev, and you can use this <a> element’s href attribute to get the previous comic’s URL, which gets stored in url. Then the while loop begins the entire download process again for this comic.

The output of this program will look like this:


Downloading page <span><a href="http://xkcd.com...">http://xkcd.com...</a></span>
Downloading image <span><a href="http://imgs.xkcd.com/comics/phone_alarm.png...">http://imgs.xkcd.com/comics/phone_alarm.png...</a></span>
Downloading page <span><a href="http://xkcd.com/1358/...">http://xkcd.com/1358/...</a></span>
Downloading image <span><a href="http://imgs.xkcd.com/comics/nro.png...">http://imgs.xkcd.com/comics/nro.png...</a></span>
Downloading page <span><a href=" http://xkcd.com/1357/..."> http://xkcd.com/1357/...</a></span>
Downloading image <span><a href="http://imgs.xkcd.com/comics/free_speech.png...">http://imgs.xkcd.com/comics/free_speech.png...</a></span>
Downloading page <span><a href=" http://xkcd.com/1356/..."> http://xkcd.com/1356/...</a></span>
Downloading image <span><a href="http://imgs.xkcd.com/comics/orbital_mechanics.png...">http://imgs.xkcd.com/comics/orbital_mechanics.png...</a></span>
Downloading page <span><a href=" http://xkcd.com/1355/..."> http://xkcd.com/1355/...</a></span>
Downloading image <span><a href="http://imgs.xkcd.com/comics/airplane_message.png...">http://imgs.xkcd.com/comics/airplane_message.png...</a></span>
Downloading page <span><a href=" http://xkcd.com/1354/..."> http://xkcd.com/1354/...</a></span>
Downloading image <span><a href="http://imgs.xkcd.com/comics/heartbleed_explanation.png...">http://imgs.xkcd.com/comics/heartbleed_explanation.png...</a></span>
--snip--
This project is a good example of a program that can automatically follow links in order to scrape large amounts of data from the Web. You can learn about Beautiful Soup’s other features from its documentation at <span><a href="http://www.crummy.com/software/BeautifulSoup/bs4/doc/.">http://www.crummy.com/software/BeautifulSoup/bs4/doc/.</a></span>

# Ideas for Similar Programs
Downloading pages and following links are the basis of many web crawling programs. Similar programs could also do the following:

Back up an entire site by following all of its links.

Copy all the messages off a web forum.

Duplicate the catalog of items for sale on an online store.

The requests and BeautifulSoup modules are great as long as you can figure out the URL you need to pass to requests.get(). However, sometimes this isn’t so easy to find. Or perhaps the website you want your program to navigate requires you to log in first. The selenium module will give your programs the power to perform such sophisticated tasks.