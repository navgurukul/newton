```ngMeta
submissionType:url
```

## Hangman Images
Aapko images.py se IMAGES import kar kar, woh images print karni hai. Jab bhi user koi galat input deta hai, toh aap corresponding image dikhayenge. 

## Hint
Toh agar user ne teesri baar galat answer diya, toh aap teesri wali image dikhayeing, `remaining_lives` ko graphically show karne ke liye.


## Possible Solution
```python
from images import IMAGES
```

..................... in the hangman function ............................
...
...
...
```python
    while (True):
        else:
            print "Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed)
            print IMAGES[8-remaining_lives]
            print "Remaining Lives : ", remaining_lives
            print ""
            letters_guessed.append(letter)
            remaining_lives -= 1
```
...
...
...
