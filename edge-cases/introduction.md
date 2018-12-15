## EdgeCases


## EdgeCases kya hota hai
Agar aapka program sahi chal raha hai most of the inputs ke liye, but kisi ek ya do input ke liye sahi nahi chal raha, to us input ko edgecase kehte hai.

Humara objective hai ki hum edgecases ke liye bhi humara program sahi input de


### Example: Division of 2 numbers.


```python
# a,b naam ke 2 variables mai input lenge.
a = input()
b = input()

# ab hum a,b ko integer mai typecase karenge
a = int(a)
b = int(b)

# hum a, b ka division print karenge
print (a/b) 
```

agar hum ye program chalate hai, and `a` mai input 6 dete hai and `b` mai input 2 dete hai, to kya print hoga

## Finding edgecases

ab hume is program mai aisa input dhundna hai, jispe ye program sahi output nahi dega ya fir error de dega
agar hum `a` mai kuch bhi input de dete hai but `b` mai 0 input dete hai, to kya hoga?

Agar aap is program ko run karenge apne laptop mai to aapko error dikega, ye error kyuun aaya?

## Finding reason of edgecases

ab hume ye dekhna hai ki ye edgecase kyyun aaya.
well agar hum kisi bhi number ko zero se divide nahi kar sakte and aisa karne pe `ZeroDivisionError` exception aata hai

## Handling edgecases

ab hum is program mai edge case kaise handle kar sakte hai, hum agar `b` 0 hai to bol sakte hai ki division of any number by `0` possible nahi hai

```python
# a,b naam ke 2 variables mai input lenge.
a = input()
b = input()

# ab hum a,b ko integer mai typecase karenge
a = int(a)
b = int(b)

# hum a, b ka division print karenge
if (b != 0):
	print (a/b)
else:
	print ("Number cannot be divided by zero")
```


