```ngMeta
name: Lists
completionMethod: manual
```

# What are Lists?

List ek aisa variable hai, jisme hum bahut saare values rakh sakte hai. List kaafi useful hoti hai kyuki hum bahut saari values apni sahuliyat se list mei pack kar sakte hai. Jaise:

1. Schools mei baccho ke naam ki list
2. Banks ke naam ki list
3. Ravi ke boards mei marks ki list
4. Rahul ke phone numbers ki list
5. Mohd Rafi ke gaano ki list

Aur bhi aise bahot saare examples ho sakte hain.

# Kuch Examples

Iss example mein hum kuch bachon ki naam ki list store kar rahe hain.

```python
names_list = ["rahul", "shivam", "kavay", "ashish", "rohit"]
print names_list
print type(names_list)
```

Aakhri line mein humne `type` ka use kiya hai. `type` function se hum dekhenge python mein iska type kya hai.

Yeh ek strings ki list hai kyunki iski saari values mein string hain.

**Note kariye, ki LIST ko start karne ke liye `[` use hota hai and band karne ke liye `]` use hota hai. `[ ]` ki shape square jaise dekhti hai, isliye inhe SQUARE BRACKEtS kaha jata hai**

Lists ke andar hum koi bhi object daal sakte hain. Yeh string, integer ya kisi bhi aur data type ka ho sakta hai.

## STRINGS ki LIST

```python
banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
print banks_list
print type(banks_list)
```

Lekin hum jab bhi ek list variable pe `type` function ka use karenge, toh humesha uska type list dikhayega. Lekin list ke andar kuch bhi type ho sakte hain.

## INTEGERS ki LIST

Yeh ek student ke boards ki marks ki list hai.

```python
ravi_marks_list = [70, 80, 75, 65, 68]
print ravi_marks_list   
print type(ravi_marks_list)
```

## FLOATS ki LIST

Yeh pichle saat dinon mein tapman (temperature) ki list hai.

```python
temperature_list = [21.1, 24.3, 19, 25, 17, 18, 23]
print temperature_list
```

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

**Aapne observe kiya hoga, sab ka type 'list' hi hai.**