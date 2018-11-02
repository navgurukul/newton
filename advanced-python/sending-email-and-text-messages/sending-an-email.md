```ngMeta
name: sending-an-email
completionMethod: manual
```
# Sending an Email
Once you are logged in to your email provider’s SMTP server, you can call the sendmail() method to actually send the email. The sendmail() method call looks like this:

```python
>>> smtpObj.sendmail(' my_email_address@gmail.com ', ' recipient@example.com ','Subject: So long.\nDear Alice,so long and thanks for all the fish. Sincerely,Bob')
```
{}
The sendmail() method requires three arguments.

Your email address as a string (for the email’s “from” address)

The recipient’s email address as a string or a list of strings for multiple recipients (for the “to” address)

The email body as a string

The start of the email body string must begin with 'Subject: \n' for the subject line of the email. The '\n' newline character separates the subject line from the main body of the email.

The return value from sendmail() is a dictionary. There will be one key-value pair in the dictionary for each recipient for whom email delivery failed. An empty dictionary means all recipients were successfully sent the email.
# Disconnecting from the SMTP Server
Be sure to call the quit() method when you are done sending emails. This will disconnect your program from the SMTP server.

```python
>>> smtpObj.quit()
```
(221, b'2.0.0 closing connection ko10sm23097611pbd.52 - gsmtp')
The 221 in the return value means the session is ending.

To review all the steps for connecting and logging in to the server, sending email, and disconnection, see Sending Email.