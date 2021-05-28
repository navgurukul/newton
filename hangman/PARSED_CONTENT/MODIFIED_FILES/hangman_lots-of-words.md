```ngMeta
lots-of-words_key1
```
## lots-of-words_key2
lots-of-words_key3`words.py`lots-of-words_key4`words.txt`lots-of-words_key5`words.py`lots-of-words_key6`words.txt`lots-of-words_key7

## lots-of-words_key8
- lots-of-words_key9
- lots-of-words_key10
## lots-of-words_key11
lots-of-words_key12[lots-of-words_key13](https://www.youtube.com/watch?v=6LiPNTmkNeY)


## lots-of-words_key14
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
