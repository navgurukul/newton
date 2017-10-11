```ngMeta
name: Cipher 1.0
completionMethod: peer
```

Apne simple se message ko aise change karna jisse koi dusra insaan usse samajh na paye usse encryption bolte hai. Encryption karne ke bhot sare ways hote hai. Hum cipher wheel use karenge. Cipher wheel mei hum her character ko kissi number se aage shift kar dete hai. Jaise:
 
Hum iss cihper wheel mein her character ki value ko 2 se increase kar denge. Aisa karne ke liye hum chars aur shifted_chars array ka use karenge.

Example:

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

Topics covered

* function returning the wrong value
* argument passed to the function but never used.
* for loop itterates over wrong string
* semantic/syntactic problems in if/else

Neeche yeh program diya hua hai, isko sahi kar ke ek nayi file mein submit karo.

```python
# Cipher wheel with a function for finding an element in a list
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

flag = True
while flag == True
choice = raw_input("What do you want to do? 1. Encrypt a message 2. Decrypt a message  Enter `e` or `d` respectively!")
if choice = 'e':
    plain_message = raw_input("Enter message to encrypt??")
    encrypt_message(plain_message)
else choice = 'd':
    encrypted_msg = raw_input("Enter message to decrypt?")
    decrypt_message(encrypted_msg)
else
    play_again = raw_input("Do you want to try agian or Do you want to exit? (Y/N)")
    if play_again == 'Y'
        continue
    elif play_again == 'N':
        break
```