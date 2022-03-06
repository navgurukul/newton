```ngMeta
name: logging-in-to-the-smtp-server
```
# Logging in to the SMTP Server
Once your encrypted connection to the SMTP server is set up, you can log in with your username (usually your email address) and email password by calling the login() method.

```python
>>> smtpObj.login(' my_email_address@gmail.com ', ' MY_SECRET_PASSWORD ')
```
(235, b'2.7.0 Accepted')
Gmail’s Application-Specific Passwords

Gmail has an additional security feature for Google accounts called application-specific passwords. If you receive an Application-specific password required error message when your program tries to log in, you will have to set up one of these passwords for your Python script. Check out the resources at <span><a href="http://nostarch.com/automatestuff/">http://nostarch.com/automatestuff/</a></span> for detailed directions on how to set up an application-specific password for your Google account.

Pass a string of your email address as the first argument and a string of your password as the second argument. The 235 in the return value means authentication was successful. Python will raise an smtplib.SMTPAuthenticationError exception for incorrect passwords.

# Warning
Be careful about putting passwords in your source code. If anyone ever copies your program, they’ll have access to your email account! It’s a good idea to call input() and have the user type in the password. It may be inconvenient to have to enter a password each time you run your program, but this approach will prevent you from leaving your password in an unencrypted file on your computer where a hacker or laptop thief could easily get it.