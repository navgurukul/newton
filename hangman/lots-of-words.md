```ngMeta
submission_type:url
```
## Lots of Words
Abhi sirf teen-chaar words mei se ek word user ko de diya jaata hai. (Check `words.py`)
Aapko `words.txt` file ko code mei read kar kar, `words.py` file ko modify karna hai. 
Jisse ki `words.txt` mei se koi random word computer use kare user se guess karane ke liye.

## Hint
- `words.txt` ko read kar kar, ek `array/list` bana kar `load_words` se return kar sakte ho
- file padhne ke liye, `readline()` function use kar sakte ho 

## Solution

@[youtube](https://www.youtube.com/watch?v=6LiPNTmkNeY)

## Possible Solution
```python
def load_words():
    """
    Ye function kaafi jayada words ko load karne mai help karega
    """

    WORDLIST_FILENAME = "words.txt"
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    line = inFile.readline()
    word_list = string.split(line)
    print "  ", len(word_list), "words loaded.\n"

    return word_list
```
