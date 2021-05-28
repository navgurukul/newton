```ngMeta
project-multithreaded-xkcd-downloader_key1
```
# project-multithreaded-xkcd-downloader_key2
project-multithreaded-xkcd-downloader_key3

project-multithreaded-xkcd-downloader_key4project-multithreaded-xkcd-downloader_key5

# project-multithreaded-xkcd-downloader_key6
project-multithreaded-xkcd-downloader_key7

project-multithreaded-xkcd-downloader_key8project-multithreaded-xkcd-downloader_key9project-multithreaded-xkcd-downloader_key10project-multithreaded-xkcd-downloader_key11project-multithreaded-xkcd-downloader_key12project-multithreaded-xkcd-downloader_key13project-multithreaded-xkcd-downloader_key14project-multithreaded-xkcd-downloader_key15project-multithreaded-xkcd-downloader_key16

project-multithreaded-xkcd-downloader_key17


project-multithreaded-xkcd-downloader_key18 project-multithreaded-xkcd-downloader_key19
project-multithreaded-xkcd-downloader_key20

project-multithreaded-xkcd-downloader_key21[project-multithreaded-xkcd-downloader_key22](http://xkcd.com/%s...&#39;)
project-multithreaded-xkcd-downloader_key23[project-multithreaded-xkcd-downloader_key24](http://xkcd.com/%s&#39;)
project-multithreaded-xkcd-downloader_key25

project-multithreaded-xkcd-downloader_key26

project-multithreaded-xkcd-downloader_key27

 project-multithreaded-xkcd-downloader_key28
 project-multithreaded-xkcd-downloader_key29
project-multithreaded-xkcd-downloader_key30

# project-multithreaded-xkcd-downloader_key31
project-multithreaded-xkcd-downloader_key32


# project-multithreaded-xkcd-downloader_key33
# project-multithreaded-xkcd-downloader_key34
project-multithreaded-xkcd-downloader_key35```python
# Create and start the Thread objects.
downloadThreads = []             # a list of all the Thread objects
for i in range(0, 1400, 100):    # loops 14 times, creates 14 threads
    downloadThread = threading.Thread(target=downloadXkcd, args=(i, i + 99))
    downloadThreads.append(downloadThread)
    downloadThread.start()
```
project-multithreaded-xkcd-downloader_key36

project-multithreaded-xkcd-downloader_key37

# project-multithreaded-xkcd-downloader_key38
project-multithreaded-xkcd-downloader_key39


# project-multithreaded-xkcd-downloader_key40
# project-multithreaded-xkcd-downloader_key41
project-multithreaded-xkcd-downloader_key42```python
# Wait for all threads to end.
for downloadThread in downloadThreads:
    downloadThread.join()
print('Done.')
```
project-multithreaded-xkcd-downloader_key43

