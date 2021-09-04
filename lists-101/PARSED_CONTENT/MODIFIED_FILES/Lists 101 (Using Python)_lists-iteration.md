lists-iteration_key1
lists-iteration_key2


lists-iteration_key3


lists-iteration_key4


lists-iteration_key5
- lists-iteration_key6
- lists-iteration_key7
lists-iteration_key8
- lists-iteration_key9
- lists-iteration_key10
- lists-iteration_key11
lists-iteration_key12
- lists-iteration_key13
- lists-iteration_key14
- lists-iteration_key15
lists-iteration_key16



```python
students_list = ["robin", "anamika", "faisal", "valmiki", "waseem", "amara"]
```

lists-iteration_key17


* lists-iteration_key18
* lists-iteration_key19
* lists-iteration_key20
* lists-iteration_key21
* lists-iteration_key22
* lists-iteration_key23
lists-iteration_key24
```python
students_list = ["robin", "anamika", "faisal", "valmiki", "waseem", "amara"]
list_length = len(students_list)
index = 0
while index < list_length:
    print students_list[index]
    index = index + 1
```lists-iteration_key25



lists-iteration_key26
lists-iteration_key27
```python
student_marks = [23, 45, 89, 90, 56, 80] 
length = len(student_marks)
index = 0
total_marks = 0
while index < len(student_marks):
    total_marks = student_marks[index] + total_marks
    index = index + 1
print "Total Marks: " + str(total_marks)
```lists-iteration_key28



lists-iteration_key29
lists-iteration_key30



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
print "Marks more than 50: " + str(more_than50)
print "Marks less than 50: " + str(less_than50)
```

lists-iteration_key31
lists-iteration_key32
