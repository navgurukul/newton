```ngMeta
invalid-input_key1
```

invalid-input_key2
invalid-input_key3


- invalid-input_key4
- invalid-input_key5
- invalid-input_key5
invalid-input_key6
- invalid-input_key7
- invalid-input_key8
- invalid-input_key9
- invalid-input_key10
invalid-input_key11
@[`youtube`](https://www.`youtube`.com/watch?v=-3aK5qikWBs)


invalid-input_key12
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
invalid-input_key13
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
invalid-input_key14
