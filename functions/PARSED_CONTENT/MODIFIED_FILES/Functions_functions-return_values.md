functions-return_values_key1
functions-return_values_key2


functions-return_values_key3


```python
def add_numbers(number_x, number_y):
    number_sum = number_x + number_y
    return number_sum

sum1 = add_numbers(20, 40)
print(sum1)
sum2 = add_numbers(560, 23)
a = 1234
b = 12
sum3 = add_numbers(a, b)
print(sum2)
print(sum3)
number_a = add_numbers(20, 40) / add_numbers(5, 1)
print(number_a)
```
functions-return_values_key4


functions-return_values_key5


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
print(sum4)
print(type(sum4))
```
functions-return_values_key13


functions-return_values_key14


functions-return_values_key15


functions-return_values_key16


functions-return_values_key17


```python
number_b = add_numbers_print(5, 4) / add_numbers_print(2, 1)
```
functions-return_values_key18


functions-return_values_key19



functions-return_values_key20



functions-return_values_key21


functions-return_values_key22


functions-return_values_key23
functions-return_values_key24


```python
def add_numbers_more(number_x, number_y):
    number_sum = number_x + number_y
    print("Hello from NavGurukul ;)")
    return number_sum
    number_sum = number_x + number_x
    print("Will i reach here?")
    return number_sum

sum6 = add_numbers_more(100, 20)
```
functions-return_values_key25


functions-return_values_key26




* functions-return_values_key27
* functions-return_values_key28
* functions-return_values_key29
functions-return_values_key30


```python
def menu(day):
    if day == "monday":
        return "Butter Chicken"
    elif day == "tuesday":
        return "Mutton Chaap"
    else:
        return "Chole Bhature"

    print("Will I be able to print? :-(")

mon_menu = menu("monday")
print(mon_menu)
tues_menu = menu("tuesday")
print(tues_menu)
fri_menu = menu("friday")
print(fri_menu)
```
functions-return_values_key31



functions-return_values_key32



* functions-return_values_key33
* functions-return_values_key34
* functions-return_values_key35
* functions-return_values_key36
* functions-return_values_key37
functions-return_values_key38


```python
def menu(day):
    if day == "monday":
        food = "Butter Chicken"
    elif day == "tuesday":
        food = "Mutton Chaap"
    else:
        food = "Chole Bhature"
    print("Will I be able to print? :-(")
    return food
    print("But I'm not sure will print? :'(")
print(menu("monday"))
```
functions-return_values_key39


functions-return_values_key40



functions-return_values_key41
