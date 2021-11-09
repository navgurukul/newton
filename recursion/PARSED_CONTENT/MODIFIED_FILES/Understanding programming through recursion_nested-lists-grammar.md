nested-lists-grammar_key1
nested-lists-grammar_key2


nested-lists-grammar_key3


nested-lists-grammar_key4


1. nested-lists-grammar_key5
2. nested-lists-grammar_key6
3. nested-lists-grammar_key7
4. nested-lists-grammar_key8
nested-lists-grammar_key9


nested-lists-grammar_key10


nested-lists-grammar_key11


nested-lists-grammar_key12


```python
[1, 2, [3, 4, [5, 6, [7, 8]], 9, 10], 11, 12] => [1] + [2, [3, 4, [5, 6, [7, 8]], 9, 10], 11, 12]] # Rule 4 and Rule 1 (for [1])
[2,     [3, 4, [5, 6, [7, 8]], 9, 10], 11, 12]] # Rule 3
[3, 4, [5, 6, [7, 8]], 9, 10], 11, 12] => [3] + [4, [5, 6, [7, 8]], 9, 10], 11, 12]] # Rule 4
[4,             [5, 6, [7, 8]], 9, 10], 11, 12]] # Rule 3
and so on ...
```

nested-lists-grammar_key13


nested-lists-grammar_key14
- nested-lists-grammar_key15
- nested-lists-grammar_key16
- nested-lists-grammar_key17
- nested-lists-grammar_key18
nested-lists-grammar_key19
```python
import random

rules = [ "[INTEGER]", "[NESTED_LIST, INTEGER]", "[INTEGER, NESTED_LIST]", "NESTED_LIST + NESTED_LIST"]

def generateRandomNumber():
    return random.randrange(1, 20)

def generateRandomNestedList():
    random_rule = random.randrange(4)
    if random_rule == 0:
        return [generateRandomNumber()]

    elif random_rule == 1:
        return [generateRandomNestedList(), generateRandomNumber()]

    elif random_rule == 2:
        return [generateRandomNumber(), generateRandomNestedList()]

    elif random_rule == 3:
        return generateRandomNestedList() + generateRandomNestedList()

print generateRandomNestedList()
```

nested-lists-grammar_key20
nested-lists-grammar_key21


nested-lists-grammar_key22
nested-lists-grammar_key23


nested-lists-grammar_key24[nested-lists-grammar_key25](https://github.com/navgurukul/shakuntala-devi)
nested-lists-grammar_key26