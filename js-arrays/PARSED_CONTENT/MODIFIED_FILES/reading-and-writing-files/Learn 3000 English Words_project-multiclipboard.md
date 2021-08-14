project-multiclipboard_key1
project-multiclipboard_key2


project-multiclipboard_key3


project-multiclipboard_key4


project-multiclipboard_key5


project-multiclipboard_key6


project-multiclipboard_key7


project-multiclipboard_key8


project-multiclipboard_key9


project-multiclipboard_key10


project-multiclipboard_key11


project-multiclipboard_key12


project-multiclipboard_key13


project-multiclipboard_key14



project-multiclipboard_key15
project-multiclipboard_key16
project-multiclipboard_key17



project-multiclipboard_key18
project-multiclipboard_key19
project-multiclipboard_key20
project-multiclipboard_key21
project-multiclipboard_key22
project-multiclipboard_key23


project-multiclipboard_key24


project-multiclipboard_key25
project-multiclipboard_key26
```python
   mcbShelf.close()
```
project-multiclipboard_key27


project-multiclipboard_key28
project-multiclipboard_key29



project-multiclipboard_key30
project-multiclipboard_key31
project-multiclipboard_key32
```python
   # Save clipboard content.

❶ if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
❷         mcbShelf[sys.argv[2]] = pyperclip.paste()
   elif len(sys.argv) == 2:
```
project-multiclipboard_key33


project-multiclipboard_key34


project-multiclipboard_key35


project-multiclipboard_key36
project-multiclipboard_key37



project-multiclipboard_key38
project-multiclipboard_key39
project-multiclipboard_key40


project-multiclipboard_key41
project-multiclipboard_key42
```python
       # List keywords and load content.
❶     if sys.argv[1].lower() == 'list':
❷         pyperclip.copy(str(list(mcbShelf.keys())))
       elif sys.argv[1] in mcbShelf:
❸         pyperclip.copy(mcbShelf[sys.argv[1]])
```
project-multiclipboard_key43


project-multiclipboard_key44


project-multiclipboard_key45


project-multiclipboard_key46


project-multiclipboard_key47
project-multiclipboard_key48


project-multiclipboard_key49


project-multiclipboard_key50


project-multiclipboard_key51
