```ngMeta
name: sending-text-messages
```
# Sending Text Messages
Once you’ve installed the twilio module, signed up for a Twilio account, verified your phone number, registered a Twilio phone number, and obtained your account SID and auth token, you will finally be ready to send yourself text messages from your Python scripts.

Compared to all the registration steps, the actual Python code is fairly simple. With your computer connected to the Internet, enter the following into the interactive shell, replacing the accountSID, authToken, myTwilioNumber, and myCellPhone variable values with your real information:

```python
❶ >>> from twilio.rest import TwilioRestClient
   >>> accountSID = 'ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
   >>> authToken = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
❷ >>> twilioCli = TwilioRestClient(accountSID, authToken)
   >>> myTwilioNumber = '+14955551234'
   >>> myCellPhone = '+14955558888'
❸ >>> message = twilioCli.messages.create(body='Mr. Watson - Come here - I want to see you.', from_=myTwilioNumber, to=myCellPhone)
```
A few moments after typing the last line, you should receive a text message that reads Sent from your Twilio trial account - Mr. Watson - Come here - I want to see you.

Because of the way the twilio module is set up, you need to import it using from twilio.rest import TwilioRestClient, not just import twilio ❶. Store your account SID in accountSID and your auth token in authToken and then call TwilioRestClient() and pass it accountSID and authToken. The call to TwilioRestClient() returns a TwilioRestClient object ❷. This object has a messages attribute, which in turn has a create() method you can use to send text messages. This is the method that will instruct Twilio’s servers to send your text message. After storing your Twilio number and cell phone number in myTwilioNumber and myCellPhone, respectively, call create() and pass it keyword arguments specifying the body of the text message, the sender’s number (myTwilioNumber), and the recipient’s number (myCellPhone) ❸.

The Message object returned from the create() method will have information about the text message that was sent. Continue the interactive shell example by entering the following:

```python
>>> message.to
```
'+14955558888'
```python
>>> message.from_
```
'+14955551234'
```python
>>> message.body
```
'Mr. Watson - Come here - I want to see you.'
The to, from_, and body attributes should hold your cell phone number, Twilio number, and message, respectively. Note that the sending phone number is in the from_ attribute—with an underscore at the end—not from. This is because from is a keyword in Python (you’ve seen it used in the from modulename import * form of import statement, for example), so it cannot be used as an attribute name. Continue the interactive shell example with the following:

```python
>>> message.status
```
'queued'
```python
>>> message.date_created
```
datetime.datetime(2015, 7, 8, 1, 36, 18)
```python
>>> message.date_sent == None
```
True
The status attribute should give you a string. The date_created and date_sent attributes should give you a datetime object if the message has been created and sent. It may seem odd that the status attribute is set to 'queued' and the date_sent attribute is set to None when you’ve already received the text message. This is because you captured the Message object in the message variable before the text was actually sent. You will need to refetch the Message object in order to see its most up-to-date status and date_sent. Every Twilio message has a unique string ID (SID) that can be used to fetch the latest update of the Message object. Continue the interactive shell example by entering the following:

```python
   >>> message.sid
```
   'SM09520de7639ba3af137c6fcb7c5f4b51'
```python
❶ >>> updatedMessage = twilioCli.messages.get(message.sid)
   >>> updatedMessage.status
```
   'delivered'
```python
   >>> updatedMessage.date_sent
```
   datetime.datetime(2015, 7, 8, 1, 36, 18)
Entering message.sid show you this message’s long SID. By passing this SID to the Twilio client’s get() method ❶, you can retrieve a new Message object with the most up-to-date information. In this new Message object, the status and date_sent attributes are correct.

The status attribute will be set to one of the following string values: 'queued', 'sending', 'sent', 'delivered', 'undelivered', or 'failed'. These statuses are self-explanatory, but for more precise details, take a look at the resources at <span><a href="http://nostarch.com/automatestuff/">http://nostarch.com/automatestuff/</a></span>.
Receiving Text Messages with Python

Unfortunately, receiving text messages with Twilio is a bit more complicated than sending them. Twilio requires that you have a website running its own web application. That’s beyond the scope of this book, but you can find more details in the resources for this book (<span><a href="http://nostarch.com/automatestuff/">http://nostarch.com/automatestuff/</a></span>).