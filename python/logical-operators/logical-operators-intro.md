```ngMeta
name: Logical Operators - Introduction
```

# What are boolean operators?

Abhi tak humne booleans data type ke baare mein bahot samjha hai. Booleans special type ke constants hote hai (humne abhi tak Strings, Integers aur Floats ke baarein mei padha tha). Do hi boolean values hoti hai:

1. True
2. False

Jaise integers ko add, subtract, divide, multiply, etc. kiya ja sakta hai (isko operation kehte hai - jaise integers par add operation). Aise hi Booleans par bhi kuch special operations kiye ja sakte hai. Iske liye, yeh example and yeh exercise karo. Inn operators ko **logical operators** kehte hain.

Jab hum addition subtraction karte hain toh `+`,`-` ko operators kehte hain. Aise hi boolean operators hote hain. Jaise integers ko `+` karke result bhi integer aata hai, waise hi booleans pe boolean operators ka use kar ke result bhi boolean mein hi aata hai.

3 logical operators hote hain:

1. `and`
2. `or`
3. `not`

Yeh kuch examples hain.

```python
print True and True
print True or False
print not True
```

Dhyaan se iska output dekho aur fir samajhne ki koshish karo ki yeh operators kya karte hain. Neeche humne aur depth mein inki explaination di hui hai.

| Operator | Kya Matlab Hai?                                                                                | Kuch Examples                                                                                                                                                                                           |
|----------|------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `and`    | `True` agar dono side ki values `True` hai                                                         | `True and True` iska javab True hoga kyunki dono True hain <br> `True and False `iska javab False hoga kyunki inme se ek False hai                                                                      |
| `or`     | `True` agar dono side ki values mein se ek bhi `True` hai. Nahi toh `False`                                      | `True or False `iska javab True hoga kyunki inme se ek True hai <br> `True or True `iska javab True hoga kyunki dono hi True hain <br> `False or False `iska javab False hoga kyunki dono hi False hain |
| `not`    | Yeh ek value leta hai aur usko `ulta` kar deta hai. True ko False kar deta hai aur False ko True | `not False` iska javab True hoga kyunki False ki ulti value true hogi                                                                                                                                   |


## AND Examples

```python
print (True and True)
print (True and False)
print (False and True)
print (False and False)
```

Inn saaron ko python shell mein chala ke dekho aur results ko upar waale table ke hisaab se samjho.

## OR Examples

```python
print (True or True)
print (True or False)
print (False or True)
print (False or False)
```

Inn example ko bhi chala ke samjho.

## NOT Examples

```python
print (not True)
print (not False)
```

Terminal par yeh examples chala kar dekho, yeh samajhne ke liye ki booleans kaise kaam karte hai.