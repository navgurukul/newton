```ngMeta
name:  signing-up-for-a-twilio-account
```
# Signing Up for a Twilio Account
Go to <span><a href="http://twilio.com/">http://twilio.com/</a></span> and fill out the sign-up form. Once you’ve signed up for a new account, you’ll need to verify a mobile phone number that you want to send texts to. (This verification is necessary to prevent people from using the service to spam random phone numbers with text messages.)

After receiving the text with the verification number, enter it into the Twilio website to prove that you own the mobile phone you are verifying. You will now be able to send texts to this phone number using the twilio module.

Twilio provides your trial account with a phone number to use as the sender of text messages. You will need two more pieces of information: your account SID and the auth (authentication) token. You can find this information on the Dashboard page when you are logged in to your Twilio account. These values act as your Twilio username and password when logging in from a Python program.

