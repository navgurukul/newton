debugging-question3_key1


debugging-question3_key2


debugging-question3_key3


```
plain_message = "navgurukul"
iska encrypted text aisa hoga => pcxiwtwmwn
```
```python
chars =         ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
shifted_chars = ['c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b']
```

```
chars[13] = 'n'
shifted_chars[13] = 'p'
isliye navgurukul ka n ==> p mein change ho gaya.
chars[0] = 'a'
shifted_chars[0] = 'c'
isliye navgurukul ka a ==> c mein change ho gaya.    
decryption theek iska ulta hota hai.
```
debugging-question3_key4


* debugging-question3_key5
* debugging-question3_key6
* debugging-question3_key7
* debugging-question3_key8
debugging-question3_key9


```python
# Cipher wheel with a function for finding an element in a list

# find_in_list function defined here but not called
def find_in_list(query, mainlist):
# this function is used to find the position of the "query" in the "mainlist". If "query" is in the list then it returns its position, otherwise it returns None
    mainlist_len = len(query)
    range_for_loop = range(mainlist_len)
    index = None
    for i in range_for_loop:
        element = mainlist[i]
        if element = query:
            index = i
    return i
# this should return the position of the "query" in the "mainlist"


chars =         ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
shifted_chars = ['c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b']

# encrypt_message function defined here but not called
def encrypt_message(plain_msg):
# this fucnction takes "plain_msg" as an argument and print/return the encrypted message. The "plain_msg" is tranfered into "encrypted_msg" using "shifted_chars" list. Example, if plain_msg = "ng" then n => p, g => i  and hence encrypted_msg = "pi"
    encrypted_msg = ""
    for character in encrypted_msg:
      # for character in msg
        if character in chars:
            char_index = find_in_list(character, chars)
            new_char = shifted_chars[char_index]
            encrypted_msg = encrypted_msg + new_char
        else:
            encrypted_msg = encrypted_msg + character

# decrypt_message function defined here but not called
def decrypt_message(encrypted_msg):
# this fucnction takes "encrypted_msg" as an argument and print/return the encrypted message. The "encrypted_msg" is tranfered into "decrypted_msg" using "shifted_chars" list. Example, if encrypted_msg = "pi" then p => n, i => g  and hence decrypted_msg = "ng"
    decrypted_msg = ""
    for character in decrypted_msg:
        if character in shifted_chars
            char_index = find_in_list(character, shifted_chars)
            new_char = chars[char_index]
            decrypted_msg = decrypted_msg + new_char
        else:
            decrypted_msg = decrypted_msg + character


# methods should return or print the new messages.
############################################### Code starts from here ##################################################
flag = True
while flag == True
choice = input("What do you want to do? 1. Encrypt a message 2. Decrypt a message  Enter `e` or `d` respectively!")
debugging-question3_key10
