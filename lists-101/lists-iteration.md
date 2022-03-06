## To iterate over the list

In a class, the teacher marks attendance by calling out their names one by one, from a list of students. This process is called `Iteration`.

`ITERATE` is a very important word, which you should bring in your vocabulary.

Repeat the same action with each element means `iterate over the list`. There could be many examples of `Iteration` like:

1. Iterate on your own contact list
   - one by one to all your friends 
   - send SMS .
2. To iterate over the names of students list
   - See their report cards one by one 
   - calculate their marks one by one
   - assign grades to them.
3. Now iterate over the names of your friends list
   - Giving tea one by one to your friends
   - Out of them, the friend sitting nearest to you
     - you give them biscuit together with tea.

Basically, the work that we do repeatedly is called as `Iteration` . Using `loops`, we have learned how to do iteration. But , we don't know how to **iterate over a list**. Now we will learn how to run loop on any list.

In this example, we will understand that **how to iterate over the list.**
Please see the example given below:-

```python
students_list = ["robin", "anamika", "faisal", "valmiki", "waseem", "amara"]
```

In this list all the elements have specific `index`.
*  `"robin"` - 0
*  `"anamika"` - 1
*  `"faisal"` - 2
*  `"valmiki"` - 3
*  `"waseem"` - 4
*  `"amara"` - 5

Now, we will use while loop, increase the counter one by one and we can access the elements of the  list one by one.

#### Example :-
```python
students_list = ["robin", "anamika", "faisal", "valmiki", "waseem", "amara"]
list_length = len(students_list)
index = 0
while index < list_length:
    print(students_list[index])
    index = index + 1
```
Here we have to check in the while loop that the value of the index should be less than the `list_length`. The loop will stop working at the moment when the index value will become equal to the `list_length`.


## One More Example

To calculate the total marks of a student from the student's marks list we will use the following code.
```python
student_marks = [23, 45, 89, 90, 56, 80] 
length = len(student_marks)
index = 0
total_marks = 0
while index < len(student_marks):
    total_marks = student_marks[index] + total_marks
    index = index + 1
print("Total Marks: " + str(total_marks))
```
Think about what will happen and try to execute to see what will happen. Did you understand something?


# One Final Example

Suppose we have a list of marks and we have to find that how many students have marks less than 50. For doing this we write the code given below.


```python
student_marks = [23, 45, 67, 89, 90, 54, 34, 21, 34, 23, 19, 28, 10, 45, 86, 87, 9]
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
print("Marks more than 50: " + str(more_than50))
print("Marks less than 50: " + str(less_than50))
```

### Question

If we will add `less_than50` and `more_than50` then what is its relation with `list_length`? 

You will come to know whether your understanding level is good or not? If you are wrong then discuss it with your peers and understand it :).


*If you will clearly understand this example then your concepts will become more clear.*