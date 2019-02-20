```ngMeta
name: Kaun Banega Codepati (KBC) - Setup
```

**Lists ke baare mein seekhne ke liye hum Kaun Banega Crorepati jaise ek game banayenge python ka use kar ke.**

Yeh code dekh kar samjhe - ki kaise humne KBC game banane ke liye, kuch important cheezein define ki hai - jaise - questions, options aur unke solutions.

```python
question_list = [
	"How many continents are there?",  			# pehla question
	"What is the capital of India?",			# doosra question
	"NG mei kaun se course padhaya jaata hai?"	# teesra question
]

options_list = [
	#pehle question ke liye options
	["Four", "Nine", "Seven", "Eight"],
	#second question ke liye options
	["Chandigarh", "Bhopal", "Chennai", "Delhi"],
	#third question ke liye options
	["Software Engineering", "Counseling", "Tourism", "Agriculture"]
]

# har ek question ke liye, uski solution key (yeh index nahi hai)
solution_list = [3, 4, 1]
```