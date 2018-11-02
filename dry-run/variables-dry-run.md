```ngMeta
name: Dry Run of Variables
completionMethod: manual
```

## Humein inn programs ka dry run karna hai:
### Kaise Use Karein
Aap sab ko yeh questions pen and paper use kar kar karne hai. Saari exercises aap apni notebooks mei solve kar kar, ek doosre ke solution ko check karayein.

Variables ka dry run samajhne ke liye aap [iss video](https://www.youtube.com/watch?v=9PnmC9NAvzU&feature=youtu.be) ko dekhein.

```python
a = 3
b = 4
c = a * b
a = b * c
b = a + c
c = a + b + c
```

Jab aap ko confidence ho ki aap ka solution theek hai, tab aap kisi senior se solution verify kara kar aage badh sakte hai.

Yeh bahut important hai ki yeh course aap bahut dhyaan se karein, kyuki programming ke basics iss course mei develop ho jayenge.

<!-- TODO : Dry run kaise karte hai iske liye yeh video dekho. -->

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
Iska solution verify ya samajhne k liye aap yeh [video](https://www.youtube.com/watch?v=fny5w_YKSc8) ya yeh [video](https://www.youtube.com/watch?v=RsmMloOHrRQ) ya yeh [video](https://www.youtube.com/watch?v=pyFetzD0b38) dekh sakte ho. Kaunsi video aap ko jyada clear lagi?

<!-- TODO: MODULUS KA KHUD KA EK MINI COURSE CURATE KARNA HOGA -->
```python
seconds = 96768
seconds_to_report = (seconds/ 1) % (60)
minutes = (seconds/60) % 60 
hours = (seconds/(60*60)) % 24
days = seconds/(60*60*24)
print days, hours, minutes, seconds_to_report
```


```python
seconds = 96768

seconds_to_report = seconds % 60
minutes = seconds / 60

minutes_to_report = minutes % 60
hours = minutes / 60

hours_to_report = hours % 24
days = hours / 24

print days, hours_to_report, minutes_to_report, seconds_to_report
```

Kya yeh dono program same behave karte hai? If yes, toh aisa kyu?


```python
amount = 8712
note2000 = amount/2000
amount = amount%2000

note500 = amount/500
amount = amount%500

note100= amount/100
amount = amount%100

note50 = amount/50
amount = amount%50

note10 = amount/10
amount = amount%10

note5 = amount/5
amount = amount%5

note2 = amount/2
amount = amount%2

note1 = amount/1
amount = amount%1

print note2000, note500, note100, note50, note10, note5, note2, note1

new_amount = note2000*2000 + note500*500 + note100*100 + note50*50 + note10*10 + note5*5 + note2*2 + note1*1
print new_amount

```
new_amount aur amount kya same hai ya alag? Aisa kyu hona chahiye


Iss program mai humne int or float dono daale hai, isko dhyaan se kijeyega. Dhyaan rakhein, floats aur integer division alag alag hota hai.

```python
x = 5
y = 4
z = y*1.0

if x/y == x/z:
	print "same hai"
else:
	print "same nahi hai"	


print x/y
print x/z
```
<!-- TODO: division of floats and integers: EXPLAIN: NEED A NEW CHAPTER IN ITSELF -->
