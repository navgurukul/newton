```ngMeta
submissionType:url
```

# Invalid Inputs

Aapko yeh check karna hai ki user no jo input daala hai, woh valid hai ya nahi. Iske liye aapko yeh dekhna hai ki jo user ne input daala hai,

- usmei agar ek se jyada `letters` hai toh, woh input invalid hai
- usmei a to z ke alawa koi bhi `character` hai toh woh input invalid hai
    - Yeh check karne ke liye aap .isalpha function use kar sakte ho
    ```python
    'a'.isalpha()
    True

    '1'.isalpha()
    False

    'ab'.isalpha()
    True

    'a1'.isalpha()
    False
    ```

## Hint
- Aapko user se input receive karne ke baad check karna hai ki input valid hai ya nahi
- Check karne ke liye aap user ke input ki length check kar sakte hai
- Agar input valid hai toh sab accha hai
- Par agar input invalid hai toh aap loop ko wapis se continue karo aur dobara user input lo


## Solution

```python
def ifValid(user_input):
    if len(user_input) != 1:
        return False

    if not user_input.isalpha():
        return False

    # True humne tab hi return kiya hai jab
    # user_input ki length 1 hai aur woh character hai
    return True
```

..................... in the hangman function ............................
...
...
...
```python
    while (True):
        available_letters = get_available_letters(letters_guessed)
        print "Available letters: " + available_letters

        guess = raw_input("Please guess a letter: ")
        letter = guess.lower()

        if (not ifValid(letter))
            continue

        if letter in secret_word:
            letters_guessed.append(letter)
```
...
...
...
