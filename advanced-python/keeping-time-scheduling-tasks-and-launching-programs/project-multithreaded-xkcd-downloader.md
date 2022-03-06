```ngMeta
name:  project-multithreaded-xkcd-downloader
```
# Project: Multithreaded XKCD Downloader
In Chapter 11, you wrote a program that downloaded all of the XKCD comic strips from the XKCD website. This was a single-threaded program: It downloaded one comic at a time. Much of the program’s running time was spent establishing the network connection to begin the download and writing the downloaded images to the hard drive. If you have a broadband Internet connection, your single-threaded program wasn’t fully utilizing the available bandwidth.

A multithreaded program that has some threads downloading comics while others are establishing connections and writing the comic image files to disk uses your Internet connection more efficiently and downloads the collection of comics more quickly. Open a new file editor window and save it as multidownloadXkcd.py. You will modify this program to add multithreading. The completely modified source code is available to download from <span><a href="http://nostarch.com/automatestuff/.">http://nostarch.com/automatestuff/.</a></span>

# Step 1: Modify the Program to Use a Function
This program will mostly be the same downloading code from Chapter 11, so I’ll skip the explanation for the Requests and BeautifulSoup code. The main changes you need to make are importing the threading module and making a downloadXkcd() function, which takes starting and ending comic numbers as parameters.

For example, calling downloadXkcd(140, 280) would loop over the downloading code to download the comics at <span><a href="http://xkcd.com/140">http://xkcd.com/140</a></span>, <span><a href="http://xkcd.com/141">http://xkcd.com/141</a></span>, <span><a href="http://xkcd.com/142">http://xkcd.com/142</a></span>, and so on, up to <span><a href="http://xkcd.com/279">http://xkcd.com/279</a></span>. Each thread that you create will call downloadXkcd() and pass a different range of comics to download.

Add the following code to your multidownloadXkcd.py program:


   #! python3
   # multidownloadXkcd.py - Downloads XKCD comics using multiple threads.

   import requests, os, bs4, threading
❶ os.makedirs('xkcd', exist_ok=True) # store comics in ./xkcd

❷ def downloadXkcd(startComic, endComic):
❸     for urlNumber in range(startComic, endComic + 1):
           # Download the page.
           print('Downloading page http://xkcd.com/%s...' % (urlNumber))
❹         res = requests.get('http://xkcd.com/%s' % (urlNumber))
           res.raise_for_status()

❺         soup = bs4.BeautifulSoup(res.text)

           # Find the URL of the comic image.
❻         comicElem = soup.select('#comic img')
           if comicElem == []:
               print('Could not find comic image.')
           else:
❼             comicUrl = comicElem[0].get('src')
               # Download the image.
               print('Downloading image %s...' % (comicUrl))
❽             res = requests.get(comicUrl)
               res.raise_for_status()

               # Save the image to ./xkcd.
               imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
               for chunk in res.iter_content(100000):
                   imageFile.write(chunk)
               imageFile.close()

   # TODO: Create and start the Thread objects.
   # TODO: Wait for all threads to end.
After importing the modules we need, we make a directory to store comics in ❶ and start defining downloadxkcd() ❷. We loop through all the numbers in the specified range ❸ and download each page ❹. We use Beautiful Soup to look through the HTML of each page ❺ and find the comic image ❻. If no comic image is found on a page, we print a message. Otherwise, we get the URL of the image ❼ and download the image ❽. Finally, we save the image to the directory we created.

# Step 2: Create and Start Threads
Now that we’ve defined downloadXkcd(), we’ll create the multiple threads that each call downloadXkcd() to download different ranges of comics from the XKCD website. Add the following code to multidownloadXkcd.py after the downloadXkcd() function definition:


# !python3
# multidownloadXkcd.py - Downloads XKCD comics using multiple threads.

--snip--
```python
# Create and start the Thread objects.
downloadThreads = []             # a list of all the Thread objects
for i in range(0, 1400, 100):    # loops 14 times, creates 14 threads
    downloadThread = threading.Thread(target=downloadXkcd, args=(i, i + 99))
    downloadThreads.append(downloadThread)
    downloadThread.start()
```
First we make an empy list downloadThreads; the list will help us keep track of the many Thread objects we’ll create. Then we start our for loop. Each time through the loop, we create a Thread object with threading.Thread(), append the Thread object to the list, and call start() to start running downloadXkcd() in the new thread. Since the for loop sets the i variable from 0 to 1400 at steps of 100, i will be set to 0 on the first iteration, 100 on the second iteration, 200 on the third, and so on. Since we pass args=(i, i + 99) to threading.Thread(), the two arguments passed to downloadXkcd() will be 0 and 99 on the first iteration, 100 and 199 on the second iteration, 200 and 299 on the third, and so on.

As the Thread object’s start() method is called and the new thread begins to run the code inside downloadXkcd(), the main thread will continue to the next iteration of the for loop and create the next thread.

# Step 3: Wait for All Threads to End
The main thread moves on as normal while the other threads we create download comics. But say there’s some code you don’t want to run in the main thread until all the threads have completed. Calling a Thread object’s join() method will block until that thread has finished. By using a for loop to iterate over all the Thread objects in the downloadThreads list, the main thread can call the join() method on each of the other threads. Add the following to the bottom of your program:


# !python3
# multidownloadXkcd.py - Downloads XKCD comics using multiple threads.

--snip--
```python
# Wait for all threads to end.
for downloadThread in downloadThreads:
    downloadThread.join()
print('Done.')
```
The 'Done.' string will not be printed until all of the join() calls have returned. If a Thread object has already completed when its join() method is called, then the method will simply return immediately. If you wanted to extend this program with code that runs only after all of the comics downloaded, you could replace the print('Done.') line with your new code.

