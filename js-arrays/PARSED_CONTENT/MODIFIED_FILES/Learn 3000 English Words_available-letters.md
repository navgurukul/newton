available-letters_key1
available-letters_key2


available-letters_key3


available-letters_key4
- available-letters_key5
- available-letters_key6
available-letters_key7
@[youtube](https://www.youtube.com/watch?v=qks4QueruIM)

available-letters_key8
```python
def get_available_letters(letters_guessed)available-letters_key9


    import string
    all_letters = string.ascii_lowercase
    letters_left = ""

    for letter in all_letters:
        if letter not in letters_guessed:
            letters_left += letter
    
    return letters_left
available-letters_key10


available-letters_key11
