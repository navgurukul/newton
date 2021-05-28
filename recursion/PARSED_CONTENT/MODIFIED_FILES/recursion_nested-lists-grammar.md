## nested-lists-grammar_key1
**nested-lists-grammar_key2**

nested-lists-grammar_key3`Grammar`nested-lists-grammar_key4`compiler`nested-lists-grammar_key5`language`nested-lists-grammar_key6`compiler`nested-lists-grammar_key7`machine`nested-lists-grammar_key8`machine code`nested-lists-grammar_key9

nested-lists-grammar_key10

1. nested-lists-grammar_key11
2. nested-lists-grammar_key12
3. nested-lists-grammar_key13
4. nested-lists-grammar_key14
nested-lists-grammar_key15`grammar rules`nested-lists-grammar_key16`nested list`nested-lists-grammar_key17

nested-lists-grammar_key18

`[5]`nested-lists-grammar_key19`nested list`nested-lists-grammar_key20`[[5], 2]`nested-lists-grammar_key21`nested list`nested-lists-grammar_key22`[3, [[5], 2]]`nested-lists-grammar_key23`nested list`nested-lists-grammar_key24`[5, 6, 7]`nested-lists-grammar_key25`nested list`nested-lists-grammar_key26`[5]`nested-lists-grammar_key27`[6]`nested-lists-grammar_key28`[7]`nested-lists-grammar_key29

nested-lists-grammar_key30

```python
[1, 2, [3, 4, [5, 6, [7, 8]], 9, 10], 11, 12] => [1] + [2, [3, 4, [5, 6, [7, 8]], 9, 10], 11, 12]] # Rule 4 and Rule 1 (for [1])
[2,     [3, 4, [5, 6, [7, 8]], 9, 10], 11, 12]] # Rule 3
[3, 4, [5, 6, [7, 8]], 9, 10], 11, 12] => [3] + [4, [5, 6, [7, 8]], 9, 10], 11, 12]] # Rule 4
[4,             [5, 6, [7, 8]], 9, 10], 11, 12]] # Rule 3
and so on ...
```
nested-lists-grammar_key31`nested list`nested-lists-grammar_key32

## nested-lists-grammar_key33
- nested-lists-grammar_key34
- nested-lists-grammar_key35
- nested-lists-grammar_key36
- nested-lists-grammar_key37
## nested-lists-grammar_key38
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
## nested-lists-grammar_key39
nested-lists-grammar_key40

## nested-lists-grammar_key41
nested-lists-grammar_key42

nested-lists-grammar_key43[nested-lists-grammar_key44](https://github.com/navgurukul/shakuntala-devi)
nested-lists-grammar_key45