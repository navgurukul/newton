project-multithreaded-xkcd-downloader_key1
project-multithreaded-xkcd-downloader_key2


project-multithreaded-xkcd-downloader_key3


project-multithreaded-xkcd-downloader_key4
project-multithreaded-xkcd-downloader_key5


project-multithreaded-xkcd-downloader_key6


project-multithreaded-xkcd-downloader_key7



project-multithreaded-xkcd-downloader_key8
project-multithreaded-xkcd-downloader_key9
project-multithreaded-xkcd-downloader_key10


project-multithreaded-xkcd-downloader_key11
[project-multithreaded-xkcd-downloader_key12](http://xkcd.com/%s...&#39;)
project-multithreaded-xkcd-downloader_key13
[project-multithreaded-xkcd-downloader_key14](http://xkcd.com/%s&#39;)
project-multithreaded-xkcd-downloader_key15


project-multithreaded-xkcd-downloader_key16


           # Find the URL of the comic image.
project-multithreaded-xkcd-downloader_key17


               # Save the image to ./xkcd.
               imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
               for chunk in res.iter_content(100000):
                   imageFile.write(chunk)
               imageFile.close()

project-multithreaded-xkcd-downloader_key18
project-multithreaded-xkcd-downloader_key19
project-multithreaded-xkcd-downloader_key20


project-multithreaded-xkcd-downloader_key21
project-multithreaded-xkcd-downloader_key22



project-multithreaded-xkcd-downloader_key23
project-multithreaded-xkcd-downloader_key24
project-multithreaded-xkcd-downloader_key25
```python
# Create and start the Thread objects.
downloadThreads = []             # a list of all the Thread objects
for i in range(0, 1400, 100):    # loops 14 times, creates 14 threads
    downloadThread = threading.Thread(target=downloadXkcd, args=(i, i + 99))
    downloadThreads.append(downloadThread)
    downloadThread.start()
```
project-multithreaded-xkcd-downloader_key26


project-multithreaded-xkcd-downloader_key27


project-multithreaded-xkcd-downloader_key28
project-multithreaded-xkcd-downloader_key29



project-multithreaded-xkcd-downloader_key30
project-multithreaded-xkcd-downloader_key31
project-multithreaded-xkcd-downloader_key32
```python
# Wait for all threads to end.
for downloadThread in downloadThreads:
    downloadThread.join()
print('Done.')
```
project-multithreaded-xkcd-downloader_key33
