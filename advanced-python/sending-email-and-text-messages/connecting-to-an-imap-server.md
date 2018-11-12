```ngMeta
name:  connecting-to-an-imap-server
completionMethod: manual
```
# Connecting to an IMAP Server
Just like you needed an SMTP object to connect to an SMTP server and send email, you need an IMAPClient object to connect to an IMAP server and receive email. First you’ll need the domain name of your email provider’s IMAP server. This will be different from the SMTP server’s domain name. Table 16-2 lists the IMAP servers for several popular email providers.

Table 16-2. Email Providers and Their IMAP Servers

Provider 								IMAP server domain name

Gmail 									imap.gmail.com

Outlook.com/Hotmail.com 				imap-mail.outlook.com

Yahoo Mail 								imap.mail.yahoo.com

AT&T 									imap.mail.att.net

Comcast									imap.comcast.net

Verizon									incoming.verizon.net

Once you have the domain name of the IMAP server, call the imapclient.IMAPClient() function to create an IMAPClient object. Most email providers require SSL encryption, so pass the ssl=True keyword argument. Enter the following into the interactive shell (using your provider’s domain name):

```python
>>> import imapclient
>>> imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
```
In all of the interactive shell examples in the following sections, the imapObj variable will contain an IMAPClient object returned from the imapclient.IMAPClient() function. In this context, a client is the object that connects to the server.

# Logging in to the IMAP Server
Once you have an IMAPClient object, call its login() method, passing in the username (this is usually your email address) and password as strings.

```python
>>> imapObj.login(' my_email_address@gmail.com ', ' MY_SECRET_PASSWORD ')
```
'<span><a href="my_email_address@gmail.com">my_email_address@gmail.com</a></span> Jane Doe authenticated (Success)'

## Warning
Remember, never write a password directly into your code! Instead, design your program to accept the password returned from input().

If the IMAP server rejects this username/password combination, Python will raise an imaplib.error exception. For Gmail accounts, you may need to use an application-specific password; for more details, see Gmail’s Application-Specific Passwords.
