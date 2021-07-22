```ngMeta
functions-args_key1
```

functions-args_key2
functions-args_key3


```python
numbers_list = [1, 2, 3, 4, 5, 6, 7, 10, -2]
print (max(numbers_list))
```
functions-args_key4


functions-args_key5


functions-args_key6


functions-args_key7


functions-args_key8


functions-args_key9


```python

a=[1,2,3,4,5,6]
print(len(a))
```
functions-args_key10


functions-args_key11


```python
def say_hello(name):
    print ("Hello ", name)
    print ("Aap kaise ho?")
say_hello("Aatif")
```
functions-args_key12


```
Hello , Aatif
Aap kaise ho?
```
functions-args_key13


functions-args_key14


* functions-args_key15
* functions-args_key16
* functions-args_key17
* functions-args_key18
functions-args_key19


functions-args_key20
functions-args_key21


```python
def add_numbers(number1, number2):
    print ("Main do numbers ko add karunga.")
    print (number1 + number2)
add_numbers(120, 50)
num_x = 134
name = "Rinki"
add_numbers(num_x, name)
```
functions-args_key22


```
Main do numbers ko add karunga.
170
Main do numbers ko add karunga.

TypeError: unsupported operand type(s) for +: 'int' and 'str'
```
functions-args_key23


* functions-args_key24
* functions-args_key25
* functions-args_key26
* functions-args_key27
functions-args_key28



functions-args_key29



```
def say_hello_language(name, language):
    if language == "hindi":
        print ("Namaste ", name)
        print ("Aap kaise ho?")
    elif language == "punjabi":
        print ("Sat sri akaal ", name)
        print ("Tuhada ki haal hai?")
    else:
        print ("Hello ", name)
        print ("How are you?")
say_hello_language("Rishabh", "punjabi")
say_hello_language("Armaan", "english")
say_hello_language("Abhishek", "french")
say_hello_language("Kavay", "hindi")
```
functions-args_key30


```
Sat sri akaal  Rishabh
Tuhada ki haal hai?
Hello  Armaan
How are you?
Hello  Abhishek
How are you?
Namaste  Kavay
Aap kaise ho?
```
functions-args_key31


* functions-args_key32
* functions-args_key33
* functions-args_key34
functions-args_key35


* functions-args_key36
* functions-args_key37
* functions-args_key38
functions-args_key39
functions-args_key40


```python
def say_hello_people(name_x, name_y, name_z, name_a):
    print ("Namaste ", name_x) # hindi mein
    print ("Alah hafiz ", name_y) # urdu mein
    print ("Bonjour ", name_z) # french mein
    print ("Hello ", name_a) # english mein
say_hello_people("Imitiyaz", "Rishabh", "Rahul", "Vidya")
say_hello_people("Steve", "Saswata", "Shakrundin", "Rajeev")
```
functions-args_key41


```
Namaste  Imitiyaz
Alah hafiz  Rishabh
Bonjour  Rahul
Hello  Vidya
Namaste  Steve
Alah hafiz  Saswata
Bonjour  Shakrundin
Hello  Rajeev
```
functions-args_key42


functions-args_key43


* functions-args_key44
* functions-args_key45
* functions-args_key46
* functions-args_key47
functions-args_key48
functions-args_key49


functions-args_key50


```python
def icecream(*flavours):
 for flavour in flavours:
  print("i love"+flavour)

icecream("chocolate", "butterscotch","vanilla","strawberry")
```
functions-args_key51


```
i love chocolate
i love butterscotch
i love vanilla
i love strawberry 
```
functions-args_key52
functions-args_key53


functions-args_key54


```python
def attendance(name,status="absent"):
    print(name,"is",status," today")

attendance("kartik","present")
attendance("sonu")
attendance("vishal","present")
attendance("umesh")
```
functions-args_key55
```
kartik is present today
sonu is absent today
vishal is present today
Umesh is absent today
```
