```ngMeta
name: saving-downloaded-files-to-the-hard-drive
```
# Saving Downloaded Files to the Hard Drive
From here, you can save the web page to a file on your hard drive with the standard open() function and write() method. There are some slight differences, though. First, you must open the file in write binary mode by passing the string 'wb' as the second argument to open(). Even if the page is in plaintext (such as the Romeo and Juliet text you downloaded earlier), you need to write binary data instead of text data in order to maintain the Unicode encoding of the text.

Unicode Encodings

Unicode encodings are beyond the scope of this book, but you can learn more about them from these web pages:

Joel on Software: The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets (No Excuses!): <span><a href=" http://www.joelonsoftware.com/articles/Unicode.html"> http://www.joelonsoftware.com/articles/Unicode.html</a></span>

Pragmatic Unicode: <span><a href="http://nedbatchelder.com/text/unipain.html">http://nedbatchelder.com/text/unipain.html</a></span>

To write the web page to a file, you can use a for loop with the Response object’s iter_content() method.

```python
>>> import requests
>>> res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
>>> res.raise_for_status()
>>> playFile = open('RomeoAndJuliet.txt', 'wb')
>>> for chunk in res.iter_content(100000):
        playFile.write(chunk)
```

100000
78981
```python
>>> playFile.close()
```
The iter_content() method returns “chunks” of the content on each iteration through the loop. Each chunk is of the bytes data type, and you get to specify how many bytes each chunk will contain. One hundred thousand bytes is generally a good size, so pass 100000 as the argument to iter_content().

The file RomeoAndJuliet.txt will now exist in the current working directory. Note that while the filename on the website was rj.txt, the file on your hard drive has a different filename. The requests module simply handles downloading the contents of web pages. Once the page is downloaded, it is simply data in your program. Even if you were to lose your Internet connection after downloading the web page, all the page data would still be on your computer.

The write() method returns the number of bytes written to the file. In the previous example, there were 100,000 bytes in the first chunk, and the remaining part of the file needed only 78,981 bytes.

To review, here’s the complete process for downloading and saving a file:

Call requests.get() to download the file.

Call open() with 'wb' to create a new file in write binary mode.

Loop over the Response object’s iter_content() method.

Call write() on each iteration to write the content to the file.

Call close() to close the file.

That’s all there is to the requests module! The for loop and iter_content() stuff may seem complicated compared to the open()/write()/close() workflow you’ve been using to write text files, but it’s to ensure that the requests module doesn’t eat up too much memory even if you download massive files. You can learn about the requests module’s other features from <span><a href="http://requests.readthedocs.org/.">http://requests.readthedocs.org/.</a></span>