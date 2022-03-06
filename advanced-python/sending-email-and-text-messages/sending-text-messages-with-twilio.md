```ngMeta
name: sending-text-messages-with-twilio
```
# Sending Text Messages with Twilio
Most people are more likely to be near their phones than their computers, so text messages can be a more immediate and reliable way of sending notifications than email. Also, the short length of text messages makes it more likely that a person will get around to reading them.

In this section, you’ll learn how to sign up for the free Twilio service and use its Python module to send text messages. Twilio is an SMS gateway service, which means it’s a service that allows you to send text messages from your programs. Although you will be limited in how many texts you can send per month and the texts will be prefixed with the words Sent from a Twilio trial account, this trial service is probably adequate for your personal programs. The free trial is indefinite; you won’t have to upgrade to a paid plan later.

Twilio isn’t the only SMS gateway service. If you prefer not to use Twilio, you can find alternative services by searching online for free sms gateway, python sms api, or even twilio alternatives.

Before signing up for a Twilio account, install the twilio module. Appendix A has more details about installing third-party modules.

## Note
This section is specific to the United States. Twilio does offer SMS texting services for countries outside of the United States, but those specifics aren’t covered in this book. The twilio module and its functions, however, will work the same outside the United States. See <span><a href="http://twilio.com/">http://twilio.com/</a></span> for more information.