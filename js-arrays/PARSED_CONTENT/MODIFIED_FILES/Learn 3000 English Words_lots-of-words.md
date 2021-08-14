lots-of-words_key1
lots-of-words_key2


lots-of-words_key3
- lots-of-words_key4
- lots-of-words_key5
lots-of-words_key6
@[youtube](https://www.youtube.com/watch?v=6LiPNTmkNeY)

lots-of-words_key7
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