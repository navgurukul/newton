```ngMeta
name: Variables
```

## Variables kya hote hain?

**VARIABLE** ak memory/location hai jisme hamara data store hota hai, Jiski value badal sakta hai use VARIABLE kehte hai. **VARIABLE** ka aap kuch bhi naam rakh sakte hai, and usmei kuch bhi store kar sakte hai.

1. jaise hum `123` ko `variable_x` naam ke VARIABLE mei rakh sakte hai
2. aise hi hum `9999` ko `a` naam ke VARIABLE mei rakh sakte hai

Aapko shayad yaad hoga 123 aur 9999 INTEGERS hai

```python
variable_x=123
a=9999
```

`variable_x` and `a` print karke dekhte hai ki kya hota hai

```python
print (variable_x, a)
```

`variable_x` ko hum dobara ek value de sakte hai, isse `variable_x` update ho jayega. Jaise neeche humne variable_x ko ab 9.9 value de di hai.

```python
variable_x=9.9
```

Ab print karke dekhiye variable_x ki kya value hai

```python
print (variable_x)
```

Aapko yaad hoga ki `9.9` float hai. Iska matlab hum ek variable alag alag tarah ki values de sakte hai. `a` ki value change nahi hui hai, kyuki humne usko update nahi kiya hai. Aise hi hum `a` ko ab update kar dete hai, and ek naya variable banate hai `b`

```python
a='hello world'
b='navgurukul'
```

Abb inko aise print karke output dekho.

```python
print (variable_x, a, b)
```

### Dry Run 

Aap sab ko yeh questions pen and paper use kar kar karne hai. Saari exercises aap apni notebooks mei solve kar kar, ek doosre ke solution ko check karayein.

Variables ka dry run samajhne ke liye aap iss video ko dekhein aur samjhe.
@[youtube](https://www.youtube.com/watch?v=9PnmC9NAvzU)


```python
a = 3
b = 4
c = a * b
a = b * c
b = a + c
c = a + b + c
```

```python
a = 1
b = 2
b = a
```

```python
a = 7
b = 8 * 4
b = a
```

```python
a = 1
b = 2
c = b
b = a 
a = c
```

```python
a = 1
b = a*2
c = b*2
a = c*2
```

```python
 a = 100
 a = a + 50
 a = a / 3
 a = a * 2
```

```python
 a = 10
 b = 10
 c = a * b
 a = c - b
 b = c + a
 c = a * c
```

Iska solution verify ya samajhne k liye aap yeh videos dekh sakte ho.

@[youtube](https://www.youtube.com/watch?v=fny5w_YKSc8)

@[youtube](https://www.youtube.com/watch?v=RsmMloOHrRQ)

@[youtube](https://www.youtube.com/watch?v=pyFetzD0b38)
