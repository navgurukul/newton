pattern-matching-with-regular-expressions_key1
pattern-matching-with-regular-expressions_key2


pattern-matching-with-regular-expressions_key3


pattern-matching-with-regular-expressions_key4


pattern-matching-with-regular-expressions_key5


pattern-matching-with-regular-expressions_key6
pattern-matching-with-regular-expressions_key7


pattern-matching-with-regular-expressions_key8


```python
   def isPhoneNumber(text):
❶     if len(text) != 12:
           return False
       for i in range(0, 3):
❷         if not text[i].isdecimal():
               return False
❸     if text[3] != '-':
           return False
       for i in range(4, 7):
❹         if not text[i].isdecimal():
               return False
❺     if text[7] != '-':
           return False
       for i in range(8, 12):
❻         if not text[i].isdecimal():
               return False
❼     return True

   print('415-555-4242 is a phone number:')
   print(isPhoneNumber('415-555-4242'))
   print('Moshi moshi is a phone number:')
   print(isPhoneNumber('Moshi moshi'))
```
pattern-matching-with-regular-expressions_key9


```python
415-555-4242 is a phone number:
True
Moshi moshi is a phone number:
False
```
pattern-matching-with-regular-expressions_key10


pattern-matching-with-regular-expressions_key11


pattern-matching-with-regular-expressions_key12


```python
   message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
   for i in range(len(message)):
❶     chunk = message[i:i+12]
❷     if isPhoneNumber(chunk):
         print('Phone number found: ' + chunk)
   print('Done')
```
pattern-matching-with-regular-expressions_key13



pattern-matching-with-regular-expressions_key14


pattern-matching-with-regular-expressions_key15


pattern-matching-with-regular-expressions_key16


pattern-matching-with-regular-expressions_key17
