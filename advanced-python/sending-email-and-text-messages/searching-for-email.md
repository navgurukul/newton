```ngMeta
name: searching-for-email
```
# Searching for Email
Once you’re logged on, actually retrieving an email that you’re interested in is a two-step process. First, you must select a folder you want to search through. Then, you must call the IMAPClient object’s search() method, passing in a string of IMAP search keywords.

## Selecting a Folder
Almost every account has an INBOX folder by default, but you can also get a list of folders by calling the IMAPClient object’s list_folders() method. This returns a list of tuples. Each tuple contains information about a single folder. Continue the interactive shell example by entering the following:

```python
>>> import pprint
>>> pprint.pprint(imapObj.list_folders())
```
[(('\\HasNoChildren',), '/', 'Drafts'),
 (('\\HasNoChildren',), '/', 'Filler'),
 (('\\HasNoChildren',), '/', 'INBOX'),
 (('\\HasNoChildren',), '/', 'Sent'),
--snip-
 (('\\HasNoChildren', '\\Flagged'), '/', '[Gmail]/Starred'),
 (('\\HasNoChildren', '\\Trash'), '/', '[Gmail]/Trash')]
This is what your output might look like if you have a Gmail account. (Gmail calls its folders labels, but they work the same way as folders.) The three values in each of the tuples—for example, (('\\HasNoChildren',), '/', 'INBOX')—are as follows:

A tuple of the folder’s flags. (Exactly what these flags represent is beyond the scope of this book, and you can safely ignore this field.)

The delimiter used in the name string to separate parent folders and subfolders.

The full name of the folder.

To select a folder to search through, pass the folder’s name as a string into the IMAPClient object’s select_folder() method.

```python
>>> imapObj.select_folder('INBOX', readonly=True)
```
You can ignore select_folder()’s return value. If the selected folder does not exist, Python will raise an imaplib.error exception.

The readonly=True keyword argument prevents you from accidentally making changes or deletions to any of the emails in this folder during the subsequent method calls. Unless you want to delete emails, it’s a good idea to always set readonly to True.

## Performing the Search
With a folder selected, you can now search for emails with the IMAPClient object’s search() method. The argument to search() is a list of strings, each formatted to the IMAP’s search keys. Table 16-3 describes the various search keys.

Table 16-3. IMAP Search Keys

Search key

Meaning

'ALL'

Returns all messages in the folder. You may run in to imaplib size limits if you request all the messages in a large folder. See Size Limits.

'BEFORE date', 'ON date', 'SINCE date'

These three search keys return, respectively, messages that were received by the IMAP server before, on, or after the given date. The date must be formatted like 05-Jul-2015. Also, while 'SINCE 05-Jul-2015' will match messages on and after July 5, 'BEFORE 05-Jul-2015' will match only messages before July 5 but not on July 5 itself.

'SUBJECT string', 'BODY string', 'TEXT string'

Returns messages where string is found in the subject, body, or either, respectively. If string has spaces in it, then enclose it with double quotes: 'TEXT "search with spaces"'.

'FROM string', 'TO string', 'CC string', 'BCC string'

Returns all messages where string is found in the “from” emailaddress, “to” addresses, “cc” (carbon copy) addresses, or “bcc” (blind carbon copy) addresses, respectively. If there are multiple email addresses in string, then separate them with spaces and enclose them all with double quotes: 'CC "<span><a href="firstcc@example.com secondcc@example.com">firstcc@example.com secondcc@example.com</a></span>"'.

'SEEN', 'UNSEEN'

Returns all messages with and without the \Seen flag, respectively. An email obtains the \Seen flag if it has been accessed with a fetch() method call (described later) or if it is clicked when you’re checking your email in an email program or web browser. It’s more common to say the email has been “read” rather than “seen,” but they mean the same thing.

'ANSWERED', 'UNANSWERED'

Returns all messages with and without the \Answered flag, respectively. A message obtains the \Answered flag when it is replied to.

'DELETED', 'UNDELETED'

Returns all messages with and without the \Deleted flag, respectively. Email messages deleted with the delete_messages() method are given the \Deleted flag but are not permanently deleted until the expunge() method is called (see Deleting Emails). Note that some email providers, such as Gmail, automatically expunge emails.

'DRAFT', 'UNDRAFT'

Returns all messages with and without the \Draft flag, respectively. Draft messages are usually kept in a separate Drafts folder rather than in the INBOX folder.

'FLAGGED', 'UNFLAGGED'

Returns all messages with and without the \Flagged flag, respectively. This flag is usually used to mark email messages as “Important” or “Urgent.”

'LARGER N', 'SMALLER N'

Returns all messages larger or smaller than N bytes, respectively.

'NOT search-key'

Returns the messages that search-key would not have returned.

'OR search-key1 search-key2'

Returns the messages that match either the first or second search-key.

Note that some IMAP servers may have slightly different implementations for how they handle their flags and search keys. It may require some experimentation in the interactive shell to see exactly how they behave.

You can pass multiple IMAP search key strings in the list argument to the search() method. The messages returned are the ones that match all the search keys. If you want to match any of the search keys, use the OR search key. For the NOT and OR search keys, one and two complete search keys follow the NOT and OR, respectively.

Here are some example search() method calls along with their meanings:

imapObj.search(['ALL']). Returns every message in the currently selected folder.

imapObj.search(['ON 05-Jul-2015']). Returns every message sent on July 5, 2015.

imapObj.search(['SINCE 01-Jan-2015', 'BEFORE 01-Feb-2015', 'UNSEEN']). Returns every message sent in January 2015 that is unread. (Note that this means on and after January 1 and up to but not including February 1.)

imapObj.search(['SINCE 01-Jan-2015', 'FROM <span><a href="alice@example.com">alice@example.com</a></span>']). Returns every message from<span><a href=" alice@example.com"> alice@example.com</a></span> sent since the start of 2015.

imapObj.search(['SINCE 01-Jan-2015', 'NOT FROM <span><a href="alice@example.com">alice@example.com</a></span>']). Returns every message sent from everyone except <span><a href="alice@example.com">alice@example.com</a></span> since the start of 2015.

imapObj.search(['OR FROM <span><a href="alice@example.com">alice@example.com</a></span> FROM <span><a href="bob@example.com">bob@example.com</a></span>']). Returns every message ever sent from <span><a href="alice@example.com ">alice@example.com </a></span> or bob@example.com.

imapObj.search(['FROM <span><a href="alice@example.com">alice@example.com</a></span>', 'FROM <span><a href="bob@example.com">bob@example.com</a></span>']). Trick example! This search will never return any messages, because messages must match all search keywords. Since there can be only one “from” address, it is impossible for a message to be from both <span><a href="alice@example.com">alice@example.com</a></span> and <span><a href=" bob@example.com"> bob@example.com</a></span>.

The search() method doesn’t return the emails themselves but rather unique IDs (UIDs) for the emails, as integer values. You can then pass these UIDs to the fetch() method to obtain the email content.

Continue the interactive shell example by entering the following:

```python
>>> UIDs = imapObj.search(['SINCE 05-Jul-2015'])
>>> UIDs
```
[40032, 40033, 40034, 40035, 40036, 40037, 40038, 40039, 40040, 40041]
Here, the list of message IDs (for messages received July 5 onward) returned by search() is stored in UIDs. The list of UIDs returned on your computer will be different from the ones shown here; they are unique to a particular email account. When you later pass UIDs to other function calls, use the UID values you received, not the ones printed in this book’s examples.

## Size Limits
If your search matches a large number of email messages, Python might raise an exception that says imaplib.error: got more than 10000 bytes. When this happens, you will have to disconnect and reconnect to the IMAP server and try again.

This limit is in place to prevent your Python programs from eating up too much memory. Unfortunately, the default size limit is often too small. You can change this limit from 10,000 bytes to 10,000,000 bytes by running this code:

```python
>>> import imaplib
>>> imaplib._MAXLINE = 10000000
```
This should prevent this error message from coming up again. You may want to make these two lines part of every IMAP program you write.

Using Imapclient’s Gmail_Search( ) Method

If you are logging in to the imap.gmail.com server to access a Gmail account, the IMAPClient object provides an extra search function that mimics the search bar at the top of the Gmail web page, as highlighted in Figure 16-1.

<!-- ![image](assets/000087.jpg)
 -->
Figure 16-1. The search bar at the top of the Gmail web page

Instead of searching with IMAP search keys, you can use Gmail’s more sophisticated search engine. Gmail does a good job of matching closely related words (for example, a search for driving will also match drive and drove) and sorting the search results by most significant matches. You can also use Gmail’s advanced search operators (see <span><a href="http://nostarch.com/automatestuff/">http://nostarch.com/automatestuff/</a></span> for more information). If you are logging in to a Gmail account, pass the search terms to the gmail_search() method instead of the search() method, like in the following interactive shell example:

```python
>>> UIDs = imapObj.gmail_search('meaning of life')
>>> UIDs
```
[42]
Ah, yes—there’s that email with the meaning of life! I was looking for that.

