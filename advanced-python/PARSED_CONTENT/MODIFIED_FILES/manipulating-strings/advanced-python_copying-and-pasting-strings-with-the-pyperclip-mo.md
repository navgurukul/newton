```ngMeta
copying-and-pasting-strings-with-the-pyperclip-mo_key1
```
# copying-and-pasting-strings-with-the-pyperclip-mo_key2
copying-and-pasting-strings-with-the-pyperclip-mo_key3

copying-and-pasting-strings-with-the-pyperclip-mo_key4

```python
>>> import pyperclip
>>> pyperclip.copy('Hello world!')
>>> pyperclip.paste()
'Hello world!'
```
copying-and-pasting-strings-with-the-pyperclip-mo_key5

```python
>>> pyperclip.paste()
```
copying-and-pasting-strings-with-the-pyperclip-mo_key6

copying-and-pasting-strings-with-the-pyperclip-mo_key7

# copying-and-pasting-strings-with-the-pyperclip-mo_key8
copying-and-pasting-strings-with-the-pyperclip-mo_key9

copying-and-pasting-strings-with-the-pyperclip-mo_key10

# copying-and-pasting-strings-with-the-pyperclip-mo_key11
copying-and-pasting-strings-with-the-pyperclip-mo_key12

# copying-and-pasting-strings-with-the-pyperclip-mo_key13
copying-and-pasting-strings-with-the-pyperclip-mo_key14

copying-and-pasting-strings-with-the-pyperclip-mo_key15


copying-and-pasting-strings-with-the-pyperclip-mo_key16# copying-and-pasting-strings-with-the-pyperclip-mo_key17
```python
PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}
```
# copying-and-pasting-strings-with-the-pyperclip-mo_key18
copying-and-pasting-strings-with-the-pyperclip-mo_key19


copying-and-pasting-strings-with-the-pyperclip-mo_key20# copying-and-pasting-strings-with-the-pyperclip-mo_key21
copying-and-pasting-strings-with-the-pyperclip-mo_key22```python
import sys
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]      # first command line arg is the account name
```
# copying-and-pasting-strings-with-the-pyperclip-mo_key23
copying-and-pasting-strings-with-the-pyperclip-mo_key24

copying-and-pasting-strings-with-the-pyperclip-mo_key25


copying-and-pasting-strings-with-the-pyperclip-mo_key26# copying-and-pasting-strings-with-the-pyperclip-mo_key27
copying-and-pasting-strings-with-the-pyperclip-mo_key28```python
import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: py pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]   # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
```
copying-and-pasting-strings-with-the-pyperclip-mo_key29

copying-and-pasting-strings-with-the-pyperclip-mo_key30

copying-and-pasting-strings-with-the-pyperclip-mo_key31

copying-and-pasting-strings-with-the-pyperclip-mo_key32


copying-and-pasting-strings-with-the-pyperclip-mo_key33copying-and-pasting-strings-with-the-pyperclip-mo_key34

