```ngMeta
files-intro_key1
```

files-intro_key2
files-intro_key3


files-intro_key4


files-intro_key5


```
priyanka - shimla
neela - delhi
sashi - jaipur
sarika - delhi
deepti - shimla
harshad - delhi
trishna - delhi
pradeep - jaipur
sekhar - delhi
nand - delhi
anoop - delhi
balwinder - jaipur
```
files-intro_key6


files-intro_key7


```python
my_file = open("people1.txt")
file_data = my_file.read()
print (file_data)
my_file.close()
```
files-intro_key8


files-intro_key9


files-intro_key10


files-intro_key11


files-intro_key12
files-intro_key13


```python
my_file2 = open("people2.txt", "w")
my_file2.write("Abhishek - Gurgaon")
my_file2.write("Ranveer - Delhi")
my_file2.close()
```
files-intro_key14


files-intro_key15


files-intro_key16


1. files-intro_key17
2. files-intro_key18
files-intro_key19


files-intro_key20



```
Abhishek - GurgaonRanveer - Delhi
```
files-intro_key21


files-intro_key22



```python
print ("AbhishekRanveer")
print ("---------------------------------")
print ("Abhishek\nRanveer")
print ("---------------------------------")
print ("Abhishek\n\nRanveer")
print ("---------------------------------")
```
files-intro_key23


1. files-intro_key24
2. files-intro_key25
3. files-intro_key26
files-intro_key27


```python
my_file3 = open("people3.txt", "w")
my_file3.write("Abhishek - Gurgaon\n")
my_file3.write("Ranveer - Delhi")
my_file3.close()
```
files-intro_key28


```
Abhishek - Gurgaon
Ranveer - Delhi
```
files-intro_key29


```python
my_file3.write("Abhishek - Gurgaon\nRanveer - Delhi")
```
files-intro_key30


files-intro_key31


```python
batch1_students = ["Shivam", "Rahul", "Kavay", "Dhannu", "Deepanshu", "Nitin", "Manoj", "Shakrudin", "Tara", "Suraj", "Krishna"]
students_file = open("navgurukul_students.html", "w")
students_file.write("<html>\n")
students_file.write("<head>\n")
students_file.write("<title>NavGurukul Students</title>\n")
students_file.write("</head>\n")
students_file.write("<body>\n")
students_file.write("<ul>")
for student in batch1_students:
    students_file.write("<li>" + student + "</li>\n")
students_file.write("</ul>\n")
students_file.write("</body>\n")
students_file.write("</html>\n")
students_file.close()
```
files-intro_key32


files-intro_key33


files-intro_key34


```python
my_file3 = open("test_file.txt", "w")
my_file3.write("Yahan main kuch likha")
my_file3.write("\nYaha maine kuch aur bhi likha.")
```
files-intro_key35


```python
my_file3.close()
```
files-intro_key36


```python
my_file3.write("Kuch aur likhte hain")
```
files-intro_key37
