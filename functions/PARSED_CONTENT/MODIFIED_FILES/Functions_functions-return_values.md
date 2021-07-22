```ngMeta
functions-return_values_key1
```

functions-return_values_key2
functions-return_values_key3


functions-return_values_key4


```python
def add_numbers(number_x, number_y):
    number_sum = number_x + number_y
    return number_sum

sum1 = add_numbers(20, 40)
print (sum1)
sum2 = add_numbers(560, 23)
a = 1234
b = 12
sum3 = add_numbers(a, b)
print (sum2)
print (sum3)
number_a = add_numbers(20, 40) / add_numbers(5, 1)
print (number_a)
```
functions-return_values_key5
```python
60
583
1246
10.0
```
* functions-return_values_key6
* functions-return_values_key7
* functions-return_values_key8
* functions-return_values_key9
* functions-return_values_key10
* functions-return_values_key11
functions-return_values_key12


```python
def add_numbers_print(number_x, number_y):
    number_sum = number_x + number_y
    print (number_sum)
sum4 = add_numbers_print(4, 5)
print (sum4)
print (type(sum4))
```
functions-return_values_key13
```python
9
None
<class 'NoneType'>
```
functions-return_values_key14


functions-return_values_key15



functions-return_values_key16


```python
number_b = add_numbers_print(5, 4) / add_numbers_print(2, 1)
```
functions-return_values_key17


```python
TypeError: unsupported operand type(s) for /: 'NoneType' and 'NoneType'
```
functions-return_values_key18


functions-return_values_key19


functions-return_values_key20


functions-return_values_key21
functions-return_values_key22


```python
def add_numbers_more(number_x, number_y):
    number_sum = number_x + number_y
    print ("Hello from NavGurukul ;)")
    return number_sum
    number_sum = number_x + number_x
    print ("Kya main yahan tak pahunchunga?")
    return number_sum

sum6 = add_numbers_more(100, 20)
```
functions-return_values_key23
```python
Hello from NavGurukul ;)
```
* functions-return_values_key24
* functions-return_values_key25
* functions-return_values_key26
functions-return_values_key27


```python
def menu(day):
    if day == "monday":
        return "Butter Chicken"
    elif day == "tuesday":
        return "Mutton Chaap"
    else:
        return "Chole Bhature"

    print ("Kya main print ho payungi? :-(")

mon_menu = menu("monday")
print (mon_menu)
tues_menu = menu("tuesday")
print (tues_menu)
fri_menu = menu("friday")
print (fri_menu)
```
functions-return_values_key28


```python
Butter Chicken
Mutton Chaap
Chole Bhature
```
functions-return_values_key29


* functions-return_values_key30
* functions-return_values_key31
* functions-return_values_key32
* functions-return_values_key33
functions-return_values_key34


```python
def menu(day):
    if day == "monday":
        food = "Butter Chicken"
    elif day == "tuesday":
        food = "Mutton Chaap"
    else:
        food = "Chole Bhature"
    print ("Kya main print ho payungi? :-(")
    return food
    print ("Lekin main toh pakka nahi print hounga :'(")
print(menu("monday"))
```
functions-return_values_key35
```python
Kya main print ho payungi? :-(
Butter Chicken
```
functions-return_values_key36
