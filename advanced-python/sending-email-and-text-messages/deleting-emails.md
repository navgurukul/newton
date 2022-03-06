```ngMeta
name:  deleting-emails
```
# Deleting Emails
To delete emails, pass a list of message UIDs to the IMAPClient object’s delete_messages() method. This marks the emails with the \Deleted flag. Calling the expunge() method will permanently delete all emails with the \Deleted flag in the currently selected folder. Consider the following interactive shell example:

```python
❶ >>> imapObj.select_folder('INBOX', readonly=False)
❷ >>> UIDs = imapObj.search(['ON 09-Jul-2015'])
   >>> UIDs
```
   [40066]
```python
   >>> imapObj.delete_messages(UIDs)
```
❸ {40066: ('\\Seen', '\\Deleted')}
```python
   >>> imapObj.expunge()
```
   ('Success', [(5452, 'EXISTS')])
Here we select the inbox by calling select_folder() on the IMAPClient object and passing 'INBOX' as the first argument; we also pass the keyword argument readonly=False so that we can delete emails ❶. We search the inbox for messages received on a specific date and store the returned message IDs in UIDs ❷. Calling delete_message() and passing it UIDs returns a dictionary; each key-value pair is a message ID and a tuple of the message’s flags, which should now include \Deleted ❸. Calling expunge() then permanently deletes messages with the \Deleted flag and returns a success message if there were no problems expunging the emails. Note that some email providers, such as Gmail, automatically expunge emails deleted with delete_messages() instead of waiting for an expunge command from the IMAP client.