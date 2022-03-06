```ngMeta
name: fetching-an-email-and-marking-it-as-read
```
# Fetching an Email and Marking It As Read
Once you have a list of UIDs, you can call the IMAPClient object’s fetch() method to get the actual email content.

The list of UIDs will be fetch()’s first argument. The second argument should be the list ['BODY[]'], which tells fetch() to download all the body content for the emails specified in your UID list.

Let’s continue our interactive shell example.

```python
>>> rawMessages = imapObj.fetch(UIDs, ['BODY[]'])
>>> import pprint
>>> pprint.pprint(rawMessages)
```
{40040: {'BODY[]': 'Delivered-To: my_email_address@gmail.com\r\n'
                   'Received: by 10.76.71.167 with SMTP id '
--snip--
                   '\r\n'
                   '------=_Part_6000970_707736290.1404819487066--\r\n',
         'SEQ': 5430}}
Import pprint and pass the return value from fetch(), stored in the variable rawMessages, to pprint.pprint() to “pretty print” it, and you’ll see that this return value is a nested dictionary of messages with UIDs as the keys. Each message is stored as a dictionary with two keys: 'BODY[]' and 'SEQ'. The 'BODY[]' key maps to the actual body of the email. The 'SEQ' key is for a sequence number, which has a similar role to the UID. You can safely ignore it.
As you can see, the message content in the 'BODY[]' key is pretty unintelligible. It’s in a format called RFC 822, which is designed for IMAP servers to read. But you don’t need to understand the RFC 822 format; later in this chapter, the pyzmail module will make sense of it for you.
When you selected a folder to search through, you called select_folder() with the readonly=True keyword argument. Doing this will prevent you from accidentally deleting an email—but it also means that emails will not get marked as read if you fetch them with the fetch() method. If you do want emails to be marked as read when you fetch them, you will need to pass readonly=False to select_folder(). If the selected folder is already in readonly mode, you can reselect the current folder with another call to select_folder(), this time with the readonly=False keyword argument:
```python
>>> imapObj.select_folder('INBOX', readonly=False)
```