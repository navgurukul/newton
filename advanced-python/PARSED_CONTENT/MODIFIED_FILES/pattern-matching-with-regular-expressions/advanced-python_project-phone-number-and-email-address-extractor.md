```ngMeta
project-phone-number-and-email-address-extractor_key1
```
# project-phone-number-and-email-address-extractor_key2
project-phone-number-and-email-address-extractor_key3

project-phone-number-and-email-address-extractor_key4

project-phone-number-and-email-address-extractor_key5

project-phone-number-and-email-address-extractor_key6

project-phone-number-and-email-address-extractor_key7

project-phone-number-and-email-address-extractor_key8

project-phone-number-and-email-address-extractor_key9

project-phone-number-and-email-address-extractor_key10

project-phone-number-and-email-address-extractor_key11

project-phone-number-and-email-address-extractor_key12

project-phone-number-and-email-address-extractor_key13

project-phone-number-and-email-address-extractor_key14

project-phone-number-and-email-address-extractor_key15

# project-phone-number-and-email-address-extractor_key16
project-phone-number-and-email-address-extractor_key17


project-phone-number-and-email-address-extractor_key18# project-phone-number-and-email-address-extractor_key19
project-phone-number-and-email-address-extractor_key20

project-phone-number-and-email-address-extractor_key21\(project-phone-number-and-email-address-extractor_key22\)project-phone-number-and-email-address-extractor_key23\.project-phone-number-and-email-address-extractor_key24\.project-phone-number-and-email-address-extractor_key25

# project-phone-number-and-email-address-extractor_key26
# project-phone-number-and-email-address-extractor_key27
# project-phone-number-and-email-address-extractor_key28
project-phone-number-and-email-address-extractor_key29

project-phone-number-and-email-address-extractor_key30\(project-phone-number-and-email-address-extractor_key31\)project-phone-number-and-email-address-extractor_key32\(project-phone-number-and-email-address-extractor_key33\)project-phone-number-and-email-address-extractor_key34

project-phone-number-and-email-address-extractor_key35

# project-phone-number-and-email-address-extractor_key36
project-phone-number-and-email-address-extractor_key37```python

   #! python3
   # phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.
   import pyperclip, re

   phoneRegex = re.compile(r'''(
   --snip--

   # Create email regex.
   emailRegex = re.compile(r'''(
❶     [a-zA-Z0-9._%+-]+      # username
❷     @                      # @ symbol
❸     [a-zA-Z0-9.-]+         # domain name
       (\.[a-zA-Z]{2,4})      # dot-something
       )''', re.VERBOSE)
```
 project-phone-number-and-email-address-extractor_key38
 project-phone-number-and-email-address-extractor_key39
project-phone-number-and-email-address-extractor_key40```python
   #! python3
   # phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

   import pyperclip, re

   phoneRegex = re.compile(r'''(
   --snip--

   # Find matches in clipboard text.
   text = str(pyperclip.paste())
❶ matches = []
❷ for groups in phoneRegex.findall(text):
       phoneNum = '-'.join([groups[1], groups[3], groups[5]])
       if groups[8] != '':
           phoneNum += ' x' + groups[8]
       matches.append(phoneNum)
❸ for groups in emailRegex.findall(text):
       matches.append(groups[0])
```
 project-phone-number-and-email-address-extractor_key41
project-phone-number-and-email-address-extractor_key42

# project-phone-number-and-email-address-extractor_key43
project-phone-number-and-email-address-extractor_key44```python
#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

--snip--
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
```
