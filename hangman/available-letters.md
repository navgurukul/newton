```ngMeta

```


## Available Letters
Ab aapko ek feature implement karna hai, jisse ki user ko hum dikha sake ki kaun kaun se letters abhi tak user ne use nahi kiye hai. Aise letters ko hum `Available Letters` ke naam se refer karenge.

Aap `available_letters` ka use apni tarah se program ko interesting banane mei kar sakte hai.

## Hint
- `available_letters` ke liye get_available_letters function use hota hai. Isliye aapko iss function mei changes karne hai
- `get_available_letters` mei further hints hai, isko karne ke liye

## Solution

@[youtube](https://www.youtube.com/watch?v=qks4QueruIM)

## Possible Solution
```python
def get_available_letters(letters_guessed):
    '''
    letters_guessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
    returns: string, hame ye return karna hai ki kaun kaun se letters aapne nahi guess kare abhi tak
    eg agar letters_guessed = ['e', 'a'] hai to humme baki charecters return karne hai
    jo ki `bcdfghijklmnopqrstuvwxyz' ye hoga
    '''

    import string
    all_letters = string.ascii_lowercase
    letters_left = ""

    for letter in all_letters:
        if letter not in letters_guessed:
            letters_left += letter
    
    return letters_left
```

Aap yeh kaam alag tarah se bhi kar sakte hai, yeh sirf ek possible solution hai.
