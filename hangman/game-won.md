```ngMeta
submissionType:url
```


## Game Won?
Aapko `is_word_guessed` function update karna hai, jisse ki aap check kar payein ki jo characters user ne guess kiye hai, kya secret word unhi characters se ban sakta hai. Agar haa, toh aap `True` return karoge, nahi toh `False` return karoge.

## Hint
- Yeh karne ke liye aap `get_guessed_word` function use kar sakte hai

## Solution

@[youtube](https://www.youtube.com/watch?v=tBLsbWy1oSw)

## Possible Solution
```python
def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: ek string word jo ki user ko guess karna hai
    letters_guessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
    returns: return True kare agar saare letters jo ki user ne guess kiye hai wo secret_word mai hai, warna no
      False otherwise
    '''

    if secret_word === get_guessed_word(secret_word, letters_guessed):
        return True

    return False
```

Aap yeh kaam alag tarah se bhi kar sakte hai, yeh sirf ek possible solution hai.
