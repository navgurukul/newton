```ngMeta
name: imap
completionMethod: manual
```
# IMAP
Just as SMTP is the protocol for sending email, the Internet Message Access Protocol (IMAP) specifies how to communicate with an email provider’s server to retrieve emails sent to your email address. Python comes with an imaplib module, but in fact the third-party imapclient module is easier to use. This chapter provides an introduction to using IMAPClient; the full documentation is at <span><a href="http://imapclient.readthedocs.org/.">http://imapclient.readthedocs.org/.</a></span>

The imapclient module downloads emails from an IMAP server in a rather complicated format. Most likely, you’ll want to convert them from this format into simple string values. The pyzmail module does the hard job of parsing these email messages for you. You can find the complete documentation for PyzMail at <span><a href="http://www.magiksys.net/pyzmail/.">http://www.magiksys.net/pyzmail/.</a></span>

Install imapclient and pyzmail from a Terminal window. Appendix A has steps on how to install third-party modules.