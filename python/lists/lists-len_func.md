```ngMeta
name: Iterating on Two Lists Togetherw
completionMethod: manual
```

# How to iterate on two lists together?

Let's say aapke paas do lists jo same lenght ki hai. Aap unn do lists pe ek saath kaise iterate karoge?

```python
students = ['Rishabh', 'Madhurima', 'Rahul', 'Abhishek', 'Faizal', 'Muskaan']
marks = [10, 20, 56, 45, 36, 20]

print len(students)
print len(marks)
```

Dekho ki dono lists li length `6` hai. Inpe iterate karne ka code aise likhenge:

```python
length = len(students) # kyunki dono ki same length hai toh jiski bhi length le sakte ho
counter = 0
while counter < length:
	print students[counter] + str(marks[counter])
```

Yahan dekho dono lists mein jo bhi element hain woh print ho jayenge.

Iss lesson mein bass itna hi hai :D