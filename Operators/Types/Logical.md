```ngMeta
name: Logical Operator 
submission_type: url
```
### Logical Operator(and ,or ,not ) :- 

Logical operators are used to combine conditional statements.
Logical operators are used in any programming language to make decision based on multiple conditions.in python ,we used logical operators to determine whether a condition is True or False by taking operand values as base.let's consider different logical operators that are used in python programming.

(logical operators ka use sabhi programmo me kayi condition me decision lene ke liye use kiya jata hai python me hum decision lene ke liye logical operator ka use karte hai ki kya humare operand me lagayi gayi condition True hai ya Fasle hai.)


`and :-`  and operator ka istemal hum tab karte hai jab dono condition ko check krwani ho agar dono condition true hogi to output true ayega agr dono me se koi ek bhi condition galat hui to false aayega . kyunki and me dono condition true hone par hi output True aata hai.


**Example :-**

```python
a = True 
b=False 
print(a and b and a)
 ```

`Output :-`

`False`

**Example :-**

```python
number = int(input("enter the number"))
print(number and 1)
 ```
`Iss example mai input mai 1 deti hu toh output 1 hoga kuki dono values True hoga`

`Iss example mai input mai 0 deti hu toh output 0 hoga kuki ek  value False hoga`



`or :-`  or operator me koi bhi ek condition true hoti hai to output true milta hai isme jaruri nahi hai ki dono conditon sahi ho, isme agar dono condition false ho tabhi output False aati hai.

**Example :-**

```python
a = 4 > 5
a = 899 < 887
print(a or a or 7 < 8) 
 ``` 
`Output :-`

`True`

**Example :-**
```python
x = "apple"
y = "mango"
print(x or y )
 ```

`Output :-`

`apple`


`not :-` not operator ka jab use karte hai tb wo condition ke opposite output dega ,agar condition true hogi to output false ayega or agr false hogi to output true deta hai.



**Example :-**

```python
a = 19
b = 34
c = 56
print(not c>b)
 ```


`Output :-`

`False`

**Example :-**

```python
var1 =True
print(not var1)
a =True
b= False
print( a and b or a or not b)
 ```


`Output :-`

`True`