```ngMeta
name: disconnecting-from-the-imap-server
completionMethod: manual
```
# Disconnecting from the IMAP Server
When your program has finished retrieving or deleting emails, simply call the IMAPClient’s logout() method to disconnect from the IMAP server.

```python
>>> imapObj.logout()
```
If your program runs for several minutes or more, the IMAP server may time out, or automatically disconnect. In this case, the next method call your program makes on the IMAPClient object will raise an exception like the following:


imaplib.abort: socket error: [WinError 10054] An existing connection was
forcibly closed by the remote host
In this event, your program will have to call imapclient.IMAPClient() to connect again.

Whew! That’s it. There were a lot of hoops to jump through, but you now have a way to get your Python programs to log in to an email account and fetch emails. You can always consult the overview in Retrieving and Deleting Emails with IMAP whenever you need to remember all of the steps.

