```ngMeta
debugging-question1_key1
```
debugging-question1_key2

`v`debugging-question1_key3`118`debugging-question1_key4`3`debugging-question1_key5`121`debugging-question1_key6

```python
ascii_value = ord(v) # 118
string_value = chr(ascii_value) # v
```
debugging-question1_key7

debugging-question1_key8

* debugging-question1_key9
* debugging-question1_key10
```python
def encrypt():
  message = input("Enter the message you want to encrypt")
  ascii_message = [ord(char)+3 for char in message]
  encrypt_message = [ chr(char) for char in ascii_message]  
  print (''.join(encrypt_message))


def decrypt():
  message = input("Enter the message you want to decrypt")
  ascii_message = [ord(char) for char in message]
  decrypt_message = [ chr(char) for char in ascii_message]  
  print (''.join(decrypt_message))

flag = True
while flag == False
choice = input("What do you want to do? \n1. Encrypt a message 2. Decrypt a message \nEnter E or D respectively!")
if choice = 'e':
encrypt()
els choice = 'd':
  decrypt()    
else
    play_again = input("Do you want to try agian or Do you want to exit? (Y/N)")
    if play_again == 'Y'
        continue
    elif play_again == 'N':
        break
```
