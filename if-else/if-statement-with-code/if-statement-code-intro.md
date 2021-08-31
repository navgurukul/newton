```ngMeta
name: Writing Code for If Statements
```

## Introduction

We have learned how to create `flowcharts` for `if conditions`. But we cannot use these `flowcharts` unless we learn how to write a code by looking at a `flowchart`.

```python
day = raw_input("Din enter karo\n")
if day == "monday": # Agar din Monday hai toh
	print "Rajma Chawal"
elif day == "tuesday": # Agar uppar wali conditions galat hai (Yaani day Monday nahi hai) aur day Tuesday hai toh
	print "Pao Bhaji"
elif day == "wednesday": # Agar uppar wali conditions galat hai (Yaani day Monday aur Tuesday nahi hai) aur day Wednesday hai toh
	print "Chole Bhature"
elif day == "thursday": # Agar uppar wali conditions galat hai (Yaani day Monday, Tuesday aur Wednesday nahi hai) aur day Thursday hai toh
	print "Dosa"
elif day == "friday": # Agar uppar wali conditions galat hai (Yaani day Monday, Tuesday, Wednesday aur Thursday nahi hai) aur day Friday hai toh
	print "Litti Chokha"
elif day == "saturday": # Agar uppar wali conditions galat hai (Yaani day Monday, Tuesday, Wednesday, Thursday aur Friday nahi hai) aur day Saturday hai toh
	print "Thukpa"
else: # Agar uppar wali conditions galat hai (Yaani day Monday, Tuesday, Wednesday, Thursday, Friday aur Saturday nahi hai)
	print "Poha"
```

In the above example, we take the day as input from the user. According to the day entered, we print the food item for that particular day. Read the comments carefully to understand how the code is executed at every step.

### Note:
 While entering the input for the day, you'll have to enter it exactly as it is used in the if conditions. Since Python is case-sensitive, it will treat `Monday` and `monday` differently.

### More examples

We have only used `==` comparison operator in the if statements. In the booleans exercise, we had seen other comparison operators as well. For example: 
1. `>`: Greater than
2. `<`: Less than 
3. `>=`: Greater than equal to 
4. `<=`: Less than equal to 
5. `!=`: Not equal to 

The following examples use these above mentioned comparison operators.

#### Example 1 :-
In this program, you have set the value of the variable. The user will have to guess the string.

```python
value = "delhi"
guess = raw_input("Sheher ka naam guess karo> ")
if guess != value:
	print "Aapka guess galat hai"
else:
	print "Aapka guess sahi hai"
```


#### Example 2 :-
Let's assume a rule that if the speed of our vehicle is less than or equal to 60, it will not be considered as overspeeding. Otherwise, it will be considered as overspeeding. We can write the program for it as shown below:

```python
speed = raw_input("Gaadi ki kya speed thi?")
speed = int(speed)
if speed <= 60:
	print "Gaadi speed limit ke andar thi."
else:
	print "Gaadi speed limit ke bahar thi."
```

### Note: 
Notice we have converted the value in the `speed` variable to an `int` before using in if condition. This is because the output of the `input` function is always a `string` and we cannot compare a string with a number correctly using `<=` operator.

### `Nested If Condition`
We can easily use an if statement inside another if statement.

Consider the example where we want to display the food menu based on the day and time. For example on monday, "Poha" in breakfast, "Rajma Chawal" for lunch and "Roti Sabzi" for dinner. Similary on tuesday, "Poori Sabzi" for breakfast, "Thukpa" for lunch and "Chicken Chawal" for dinner. We can write a program for this question as shown below:-

`TODO: We need to add a flowchart here somehow. #studentsShouldIgnore`

```python
day = raw_input("Din enter karo> ")
meal = raw_input("Meal enter karo, jaise breakfast lunch aur dinner mein se ek> ")
if day == "monday"
	# code yahan andar tab hi aayega jab day ki value "monday" hogi, nahi andar aayega hi nahi
	if meal == "breafast":
		print "Poha"
	elif meal == "lunch":
		print "Rajma Chawal"
	else:
		print "Roti Sabzi"
elif day == "tuesday":
	if meal == "breakfast":
		print "Poori Sabzi"
	elif meal == "lunch":
		print "Thukpa"
	else:
		print "Chicken Chawal"
else:
	print "Aur kisi bhi din hum daal roti sabzi khaynege."
```

Observe how we have used if statement inside another if statement. The if statement inside will only be checked if the outer `if condition` is `True`.