```ngMeta
available-letters_key1
```

available-letters_key2
available-letters_key3


available-letters_key4


available-letters_key5
- available-letters_key6
- available-letters_key7
available-letters_key8
@[`youtube`](https://www.`youtube`.com/watch?v=qks4QueruIM)

available-letters_key9
```python
def get_available_letters(letters_guessed):
    '''
    letters_guessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
    returns: string, hame ye return karna hai ki kaun kaun se letters aapne nahi guess kare abhi tak
    eg agar letters_guessed = ['e', 'a'] hai to humme baki charecters return karne hai
    jo ki bcdfghijklmnopqrstuvwxyz' ye hoga
    '''

    import string
    all_letters = string.ascii_lowercase
    letters_left = ""

    for letter in all_letters:
        if letter not in letters_guessed:
            letters_left += letter
    
    return letters_left
```
available-letters_key10
