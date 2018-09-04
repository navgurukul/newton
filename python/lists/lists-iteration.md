```ngMeta
name: Lists
completionMethod: manual
```

# Lists ko iterate karna

Class mei teacher ek ek naam bol kar attendance mark karti hai, list of students ki. Iss process ko iteration bolte hai. Ek ek karke list ke elements ke saath same action repeat karna. Iteration ke aise aur bahot saare examples ho sakte hain. Jaise:

1. Ek ek kar ke apne saare friends ko same SMS bhejna.
2. Ek ek kar ke report card dekh ke har bache ke marks calculate karna.
3. Ek ek kar ke apne doston ko chai dena.

Basically jab bhi hum ek kaam ko baar baar ek hi dhang se karte hain usko iteration kehte hain. Humne loops ka use kar ke pichle lessons mein iteration karna seekh liya hai. Lekin abhi hume lists pe iterate karna nahi aata. Ab yahan hum lists pe loop kaise chala sakte hain, woh dekhenge.

Iss example mei hum samjhenge ki LISTS ko kaise ITERATE karte hai. Humare paas yeh naam ki list hai:

```python
students_list = ["robin", "anamika", "faisal", "valmiki", "waseem", "amara"]
```

Iss list mein har element ka ek index hai.

* `"robin"` - 0
*  `"anamika"` - 1
*  `"faisal"` - 2
*  `"valmiki"` - 3
*  `"waseem"` - 4
*  `"amara"` - 5

Ab hum while loop ka use kar ek ek kar ke apna counter bada sakte hain aur iss list ka ek ek element access kar sakte hain. Jaise:

```python
students_list = ["robin", "anamika", "faisal", "valmiki", "waseem", "amara"]
list_length = len(students_list)
index = 0
while index < list_length:
	print students_list[index]
	index = index + 1
```

Yahan humne while mein yeh check kiya hai ki `index` ki value humesha `list_length` se kam rehni chaiye. Jaise hi index ki value `list_length` jitni ho jayegi yeh loop band ho jayega.

# Ek aur example

Ek student ke marks ki list se total marks calculate karne ke liye hum yeh code ka use karenge.

```python
student_marks = [23, 45, 89, 90, 56, 80] 
length = len(student_marks)
index = 0
total_marks = 0
while index < len(student_marks):
	total_marks = student_marks[index] + total_marks
	index = index + 1
print "Total Marks: " + str(total_marks)
```

Socho kya hona chahiye? and phir execute karke dekho kya hota hai? kuch samajh aaya?

# Ek final example

Maan lo humare paas ek list of marks hain aur humne yeh nikalna hai ki kitne bachon ke marks 50 se kam hai aur kitno ke zyada. Yeh karne ke liye hum yeh code likhenge.

```python
student_marks = [23, 45, 67, 89, 90, 54, 34, 21, 34, 23, 19, 28, 10, 45, 86, 87, 09]
list_length = len(student_marks)
index = 0
less_than50 = 0
more_than50 = 0
while index < list_length:
	marks = student_marks[index]
	if marks < 50:
		less_than50 = less_than50 + 1
	else:
		more_than50 = more_than50 + 1
	index = index + 1
print "Marks more than 50: " + str(more_than50)
print "Marks less than 50: " + str(less_than50)
```

Iss example ka output pehle paper pe soch ke likho aur fir execute kar ke dekho ki aapki understanding sahi hai ya galat. Agar galat hai toh apne peers se discuss karke ache se samjho :)