```ngMeta
files-intro_key1
```
# files-intro_key2
files-intro_key3

files-intro_key4

files-intro_key5`people1.txt`files-intro_key6

files-intro_key7

files-intro_key8

```python
my_file = open("people1.txt")
file_data = my_file.read()
print (file_data)
my_file.close()
```
files-intro_key9`open`files-intro_key10`open`files-intro_key11`open`files-intro_key12

files-intro_key13`my_file`files-intro_key14`my_file`files-intro_key15`read`files-intro_key16`read`files-intro_key17`string`files-intro_key18

files-intro_key19`people1.txt`files-intro_key20

files-intro_key21

# files-intro_key22
files-intro_key23

```python
my_file2 = open("people2.txt", "w")
my_file2.write("Abhishek - Gurgaon")
my_file2.write("Ranveer - Delhi")
my_file2.close()
```
files-intro_key24`open`files-intro_key25`open`files-intro_key26`write`files-intro_key27

files-intro_key28`write`files-intro_key29`"Abishek - Gurgaon"`files-intro_key30`"Ranveer - Delhi"`files-intro_key31

files-intro_key32`my_file2.close`files-intro_key33

1. files-intro_key34
2. files-intro_key35
files-intro_key36`people2.txt`files-intro_key37

files-intro_key38


files-intro_key39

files-intro_key40


```python
print ("AbhishekRanveer")
print ("---------------------------------")
print ("Abhishek\nRanveer")
print ("---------------------------------")
print ("Abhishek\n\nRanveer")
print ("---------------------------------")
```
files-intro_key41

1. files-intro_key42
2. files-intro_key43
3. files-intro_key44
files-intro_key45`"Abhishek - Gurgaon"`files-intro_key46`"Ranveer - Delhi"`files-intro_key47`write`files-intro_key48

```python
my_file3 = open("people3.txt", "w")
my_file3.write("Abhishek - Gurgaon\n")
my_file3.write("Ranveer - Delhi")
my_file3.close()
```
files-intro_key49

files-intro_key50`write`files-intro_key51`write`files-intro_key52

```python
my_file3.write("Abhishek - Gurgaon\nRanveer - Delhi")
```
files-intro_key53

files-intro_key54

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
files-intro_key55

files-intro_key56\<files-intro_key57\>files-intro_key58`batch1_students`files-intro_key59`li`files-intro_key60

files-intro_key61`close`files-intro_key62

```python
my_file3 = open("test_file.txt", "w")
my_file3.write("Yahan main kuch likha")
my_file3.write("\nYaha maine kuch aur bhi likha.")
```
files-intro_key63`test_file.txt`files-intro_key64

```python
my_file3.close()
```
files-intro_key65`write`files-intro_key66

```python
my_file3.write("Kuch aur likhte hain")
```
files-intro_key67