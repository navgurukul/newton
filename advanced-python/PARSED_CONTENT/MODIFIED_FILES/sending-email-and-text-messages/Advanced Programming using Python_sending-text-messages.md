```ngMeta
sending-text-messages_key1
```

sending-text-messages_key2
sending-text-messages_key3


sending-text-messages_key4


```python
❶ >>> from twilio.rest import TwilioRestClient
   >>> accountSID = 'ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
   >>> authToken = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
❷ >>> twilioCli = TwilioRestClient(accountSID, authToken)
   >>> myTwilioNumber = '+14955551234'
   >>> myCellPhone = '+14955558888'
❸ >>> message = twilioCli.messages.create(body='Mr. Watson - Come here - I want to see you.', from_=myTwilioNumber, to=myCellPhone)
```
sending-text-messages_key5


sending-text-messages_key6


sending-text-messages_key7


```python
>>> message.to
```
sending-text-messages_key8
```python
>>> message.from_
```
sending-text-messages_key9
```python
>>> message.body
```
sending-text-messages_key10


```python
>>> message.status
```
sending-text-messages_key11
```python
>>> message.date_created
```
sending-text-messages_key12
```python
>>> message.date_sent == None
```
sending-text-messages_key13


```python
   >>> message.sid
```
sending-text-messages_key14
```python
❶ >>> updatedMessage = twilioCli.messages.get(message.sid)
   >>> updatedMessage.status
```
sending-text-messages_key15
```python
   >>> updatedMessage.date_sent
```
sending-text-messages_key16


sending-text-messages_key17


sending-text-messages_key18
