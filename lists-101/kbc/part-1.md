```ngMeta
name: Kaun Banega Codepati (KBC) - Setup
```

**To understand more about list, we will make a game similar to Kaun Banega Crorepati using python.** 

Please look at the code and try to understand that in order to understand KBC game, we have defined some inportant things like
- questions, options and their  solutions.

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