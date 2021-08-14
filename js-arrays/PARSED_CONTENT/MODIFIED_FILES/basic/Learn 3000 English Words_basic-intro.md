basic-intro_key1
basic-intro_key2


basic-intro_key3


basic-intro_key4
basic-intro_key5


basic-intro_key6
```python
>>> 2 + 2
```
basic-intro_key7



basic-intro_key8
```python
Type "copyright", "credits" or "license()" for more information.
>>> 2 + 2
```
basic-intro_key9
```python
>>>
```
basic-intro_key10


basic-intro_key11


```python
>>> 2
```
basic-intro_key12


basic-intro_key13


basic-intro_key14


basic-intro_key15


basic-intro_key16


|basic-intro_key17|basic-intro_key18|basic-intro_key19|
|-----------|-----------|-----------|
|basic-intro_key20|basic-intro_key21|basic-intro_key22|
|basic-intro_key23|basic-intro_key24|basic-intro_key25|
|basic-intro_key26|basic-intro_key27|basic-intro_key28|
|basic-intro_key29|basic-intro_key30|basic-intro_key31|
|basic-intro_key32|basic-intro_key33|basic-intro_key34|
|basic-intro_key35|basic-intro_key36|basic-intro_key37|

basic-intro_key38



```python
>>> 2 + 3 * 6
```
basic-intro_key39
```python
>>> (2 + 3) * 6
```
basic-intro_key40
```python
>>> 48565878 * 578453
```
basic-intro_key41
```python
>>> 2 ** 8
```
basic-intro_key42
```python
>>> 23 / 7
```
basic-intro_key43
```python
>>> 23 // 7
```
basic-intro_key44
```python
>>> 23 % 7
```
basic-intro_key45
```python
>>> 2     +            2
```
basic-intro_key46
```python
>>> (5 - 1) * ((7 + 1) / (3 - 1))
```
basic-intro_key47




basic-intro_key48


![](assets/000056.png)
 -->
Figure 1-1. Evaluating an expression reduces it to a single value.

These rules for putting operators and values together to form expressions are a fundamental part of Python as a programming language, just like the grammar rules that help us communicate. Here’s an example:

1. This is a grammatically correct English sentence.

2. This grammatically is sentence not English correct a.

The second line is difficult to parse because it doesn’t follow the rules of English. Similarly, if you type in a bad Python instruction, Python won’t be able to understand it and will display a SyntaxError error message, as shown here:

```basic-intro_key49
>>> basic-intro_key50
```
You can always test to see whether an instruction works by typing it into the interactive shell. Don’t worry about breaking the computer: The worst thing that could happen is that Python responds with an error message. Professional software developers get error messages while writing code all the time.

# The Integer, Floating-Point, and String Data Types

Remember that expressions are just values combined with operators, and they always evaluate down to a single value. A data type is a category for values, and every value belongs to exactly one data type. The most common data types in Python are listed in Table 1-2. The values -2 and 30, for example, are said to be integer values. The integer (or int) data type indicates values that are whole numbers. Numbers with a decimal point, such as 3.14, are called floating-point numbers (or floats). Note that even though the value 42 is an integer, the value 42.0 would be a floating-point number.

Table 1-2. Common Data Types

| Data type | Examples |
|-----------|----------|
| Integers  | -2, -1, 0, 1, 2, 3, 4, 5|
| Floating-point numbers| -1.25, -1.0, --0.5, 0.0, 0.5, 1.0, 1.25|
| Strings   | 'a', 'aa', 'aaa', 'Hello!', '11 cats'|

Python programs can also have text values called strings, or strs (pronounced “stirs”). Always surround your string in single quote (') characters (as in 'Hello' or 'Goodbye cruel world!') so Python knows where the string begins and ends. You can even have a string with no characters in it, '', called a blank string. Strings are explained in greater detail in Chapter 4.

If you ever see the error message SyntaxError: EOL while scanning string literal, you probably forgot the final single quote character at the end of the string, such as in this example:

# String Concatenation and Replication

The meaning of an operator may change based on the data types of the values next to it. For example, + is the addition operator when it operates on two integers or floating-point values. However, when + is used on two string values, it joins the strings as the string concatenation operator. Enter the following into the interactive shell:

```
```python
>>> 'Alice' + 'Bob'
```
basic-intro_key51


```python
>>> 'Alice' + 42
```
basic-intro_key52


basic-intro_key53


```python
>>> 'Alice' * 5
```
basic-intro_key54


basic-intro_key55


```python
>>> 'Alice' * 'Bob'
```
basic-intro_key56
```python
>>> 'Alice' * 5.0
```
basic-intro_key57


>>> basic-intro_key58
basic-intro_key59


basic-intro_key60
|basic-intro_key61|basic-intro_key62|
|-----------|-----------|
|basic-intro_key63|basic-intro_key64|
|basic-intro_key65|basic-intro_key66|
|basic-intro_key67|basic-intro_key68|
|basic-intro_key69|basic-intro_key70|
|basic-intro_key71|basic-intro_key72|
|basic-intro_key73|basic-intro_key74|

basic-intro_key75


basic-intro_key76


basic-intro_key77


basic-intro_key78


basic-intro_key79


basic-intro_key80


1. basic-intro_key81
2. basic-intro_key82
basic-intro_key83


basic-intro_key84


basic-intro_key85


basic-intro_key86


basic-intro_key87



basic-intro_key88


basic-intro_key89
```python
>>> ================================ RESTART ================================
>>>
```
basic-intro_key90


basic-intro_key91


basic-intro_key92
basic-intro_key93



basic-intro_key94


basic-intro_key95


basic-intro_key96


basic-intro_key97



basic-intro_key98


basic-intro_key99


basic-intro_key100



basic-intro_key101


basic-intro_key102



basic-intro_key103


```python
>>> len('hello')
```
basic-intro_key104
```python
>>> len('My very energetic monster just scarfed nachos.')
```
basic-intro_key105
```python
>>> len('')
```
basic-intro_key106



>>> basic-intro_key107
```python
>>> 'I am ' + 29 + ' years old.'
```
basic-intro_key108


basic-intro_key109


```python
>>> str(29)
```
basic-intro_key110
```python
>>> print('I am ' + str(29) + ' years old.')
```
basic-intro_key111


basic-intro_key112


```python
>>> str(0)
```
basic-intro_key113
```python
>>> str(-3.14)
```
basic-intro_key114
```python
>>> int('42')
```
basic-intro_key115
```python
>>> int('-99')
```
basic-intro_key116
```python
>>> int(1.25)
```
basic-intro_key117
```python
>>> int(1.99)
```
basic-intro_key118
```python
>>> float('3.14')
```
basic-intro_key119
```python
>>> float(10)
```
basic-intro_key120


basic-intro_key121


```python
>>> spam = input()
```
basic-intro_key122
```python
>>> spam
```
basic-intro_key123


```python
>>> spam = int(spam)
>>> spam
```
basic-intro_key124


```python
>>> spam * 10 / 5
```
basic-intro_key125


```python
>>> int('99.99')
```
basic-intro_key126
```python
>>> int('twelve')
```
basic-intro_key127


```python
>>> int(7.7)
```
basic-intro_key128
```python
>>> int(7.7) + 1
```
basic-intro_key129



basic-intro_key130


basic-intro_key131


basic-intro_key132


basic-intro_key133


basic-intro_key134


```python
>>> 42 == '42'
```
basic-intro_key135
```python
>>> 42 == 42.0
```
basic-intro_key136
```python
>>> 42.0 == 0042.000
```
basic-intro_key137


basic-intro_key138
basic-intro_key139


1. basic-intro_key140
basic-intro_key141


2. basic-intro_key142
basic-intro_key143


3. basic-intro_key144
basic-intro_key145


4. basic-intro_key146
basic-intro_key147


5. basic-intro_key148
basic-intro_key149


6. basic-intro_key150
basic-intro_key151


7. basic-intro_key152
basic-intro_key153


8. basic-intro_key154
basic-intro_key155


9. basic-intro_key156
basic-intro_key157


10. basic-intro_key158
basic-intro_key159
```python
>>>
```
```python
>>> len('hello')
```
```python
>>> len('My very energetic monster just scarfed nachos.')
```
```python
>>> len('')
```
```python
>>> 'I am ' + 29 + ' years old.'
```
```python
>>> str(29)
```
```python
>>> print('I am ' + str(29) + ' years old.')
```
```python
>>> str(0)
```
```python
>>> str(-3.14)
```
```python
>>> int('42')
```
```python
>>> int('-99')
```
```python
>>> int(1.25)
```
```python
>>> int(1.99)
```
```python
>>> float('3.14')
```
```python
>>> float(10)
```
```python
>>> spam = input()
```
```python
>>> spam
```
```python
>>> spam = int(spam)
>>> spam
```
```python
>>> spam * 10 / 5
```
```python
>>> int('99.99')
```
```python
>>> int('twelve')
```
```python
>>> int(7.7)
```
```python
>>> int(7.7) + 1
```
```python
>>> 42 == '42'
```
```python
>>> 42 == 42.0
```
```python
>>> 42.0 == 0042.000
```
