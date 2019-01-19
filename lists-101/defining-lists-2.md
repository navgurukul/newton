
## MIXED Lists

Aisa nahi hai ki lists mein ek hi type ke data types hone chaiye. Inme kisi bhi type ke data types ho sakte hain. Jaise:

```python
mixed_list = ["rahul", 12, 9.0, "kaavay", "shivam", 1]
print type(mixed_list)
```

## LISTS ki LIST

```python
student1_list = ["rahul", "maths"]
print type(student1_list)
student2_list = ["shivam", "science"]
student3_list = ["kavay", "english"]

# student1_list, student2_list, student3_list mei naam and favorite subject hai
# ab hum ek LIST banayenge jiske ITEMS khud ek LIST hai

students_list = [student1_list, student2_list, student3_list]
print type(students_list)
```

Yahan humne ek list ke andar ek aur list daal di hai.

Yeh observe karein ki har LIST mei kisi bhi tarah ke ITEMS rakhe ja sakte hai. LIST ek generic structure hai jismei aap jo chahe unko rakh sakte hai. LIST hai ya nahi dekhne ke liye [ ] (square brackets) ko dhundhe.

@[youtube](9rLdQP3g4fw)

**Aapne observe kiya hoga, sab ka type 'list' hi hai.**
