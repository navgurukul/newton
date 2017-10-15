```ngMeta
name: Files in Python
completionMethod: manual
```

# How to Work with Files?

Hum python se apne computer jo bhi koi files hain, unko padh sakte hain aur saath hi saath nayi files bana ke unme data bhi daal sakte hain. Isse hum bahot interesting cheezein kar sakte hain. Jaise hum user se kuch python mein input leke, uss data se ek HTML file bana sakte hain. Aur bhi bahot saare interesting kaam kar sakte hain.

Inn examples se hum python se files ko padhna aur nayi files banana seekhenge. Abhi tak aap jo bhi programs bana rahe the, woh sirf kuch terminal pe print kar dete hain. Lekin python ka use kar ke hum apne computer pe files ke andar ke data ko padh sakte hain, aur nayi files bana ke unme data save bhi kar sakte hain. Iss example mein hum ek file khol ke uss file ka data nikalenge.

Iss ke liye ek `people1.txt` naam ki file mein neeche diye hue text ko save karo.

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

Iss file ko same folder mein save karo jisme aap apne python ka code likhne waali file ko save karoge.

Ab yeh code likh kar python file chalao:

```python
my_file = open("people1.txt")
file_data = my_file.read()
print file_data
my_file.close()
```

Yahan dekho kaise iss file ka sara data yahan print ho gaya. Python humein `open` function deta hai jis ka use kar ke, hum ek file khol sakte hain. Yahan humne `open` function ko file ka relative path diya hai. Yahan hum `open` ko file ka absolute path bhi de sakte hain.

Jaise hi hum file kholte hain, humein `my_file` variable mein ek file milti hai. `my_file` ka `read` function use kar ke hum iss file ke andar ka saara data read kar sakte hain. `read` function ka use kar ke humein file ke andar ka saara data `string` ke roop mein milta hai.

Agli line mein humne print ka use kar ke file ke saare andar ke saare contents ko print karva diya hai. Yeh woh same contents hain jo aapko `people1.txt` waali file ko khol ke dikhenge.

Hum jab bhi file kholte hain, humein uske baad my_file.close() ka use kar ke file band karni bhi zaroori hoti hai. Neeche hum iske baare mein aur baat karenge.

# Making new Files

Ab hum ek nayi file bana ke usme kuch data likhenge. Yeh karne ke liye hum neeche diye gaye code ko likhenge. Iss code se hum apni file mein kuch strings likhenge

```python
my_file2 = open("people2.txt", "w")
my_file2.write("Abhishek - Gurgaon")
my_file2.write("Ranveer - Delhi")
my_file2.close()
```

Yahan humein pehle `open` method ka use kar ek file kholi. Kyunki hum Yahan ek nayi file banana chahte hain, toh hum `open` function ek aur "w" wala argument bhi denge. Yahan "w" python ko batata hai ki hum file mein write/likhna chahte hain. Jab hum file mein `write` likhte hain toh agar uss naam ki file nahi hoti, toh python humare liye nayi file bana deti hai. Yeh file ussi directory mein banti hai, jis directory mein aap apne terminal mein ho. 

Fir humne `write` function ka use kar ke apni file mein pehle `"Abishek - Gurgaon"` likha aur fir `"Ranveer - Delhi"` likha.

Last mein humein `my_file2.close` call kiya. Jab hum file write kar rahe hote hain, toh close python ko do cheezein batata hai:

1. Humne `write` function ka use karke jo bhi likha hai, usko save kar do.
2. Ab iss file ko band kar do kyunki humein iski zaroorat nahi hai.

Ab aap jab apni nayi file `people2.txt` khol ke dekhoge, toh aapko uss file mein kuch content dikhega. Lekin aapko yeh saara content. Ek line mein dikha, na ki alag alag lines mein jaise aapne socha tha.

Iske baare mein hum agle section mein baat karenge. Humari file mein yeh aisa dikhega.


```
Abhishek - GurgaonRanveer - Delhi
```

Isko do alag lines mein laane ke baare mein neeche padhenge.

Python mein iss code ko chala ke dekho. Iske baad hum isko dhang se samjhenge.


```python
print "AbhishekRanveer"
print "---------------------------------"
print "Abhishek\nRanveer"
print "---------------------------------"
print "Abhishek\n\nRanveer"
print "---------------------------------"
```

Yahan beech ki "-----" lines humne aise hi padhne mein aasani ke liye print kari hain.

1. Pehli print mein humne "Abhishek - Gurgaon" aur "Ranveer - Delhi" mein koi space nahi diya. Isliye woh ek hi line mein print hote hain.
2. Dusri line mein humne "Abhishek - Gurgaon" aur "Ranveer - Delhi" ke beech mein ek `\n` diya hai. Isko new line character kehte hain. Jab yeh print hota hai toh yeh `\n` ki jagah ek nayi line ki tarah print hota hai. Isiliye dono "Abhishek" aur "Ranveer" ek ke neeche ek print hote hain.
3. Teesri line mein hunne 2 `\n` daale hain "Abhishek" aur "Ranveer" ke beech mein. Isliye jab yeh print hote hain, toh inke beech mein ek khaali line aati hai. Pehle `\n` se ek ke neeche ek aa jate hain, aur dusre se inke beech mein ek nayi line aa jati hain.


Issi tareeke se humare file writing/likhne waale example mein, dono `"Abhishek - Gurgaon"` aur `"Ranveer - Delhi"` ke beech mein new line nahi aati hai. Kyuki jab hum `write` function se file mein likhte hain, toh python apne aap new line nahi daalta hai. Ab hum same cheez new line ke saath karenge.

```python
my_file3 = open("people3.txt", "w")
my_file3.write("Abhishek - Gurgaon\n")
my_file3.write("Ranveer - Delhi")
my_file3.close()
```	

Yahan kyunki humne "Abhishek - Gurgaon" ke baad ek "\n" laga diya, ab yeh dono alag alag line mein aayenge. Ab file khol ke dekho. Woh waise dikhegi jaisi. Hum chahte the. Aisi:

```
Abhishek - Gurgaon
Ranveer - Delhi
```

Aap yeh soch sakte ho ki agar hum "\n" ka use kar ke ek nayi line daal sakte hain toh humne yahan do baar `write` function kyun use kiya. Yeh humne sirf apni aasani ke liye kiya. Hum do `write` ki jagah yeh bhi likh sakte hain:

```python
my_file3.write("Abhishek - Gurgaon\nRanveer - Delhi")
```

Yeh kar ke bhi humari file same hi dikhegi.

Ab hum aisa code likhenge jisse hum ek html file bana sakte hain. Socho humare paas ek list hai jisme navgurukul ke saare students ke naam hain. Ab humne ek HTML page mein yeh list dikhani hai. Toh hum uske liye yeh kar code likh sakte hain.

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

Yeh code chala ke, ek baar "navgurukul_students.html" ka code khol ke dekho. HTML code padh ke upar diye gaye python code ko firse padho. Isse aapko yeh code aur ache se samajh aayega. Humne pehle apne HTML document ke saare tags ek ek kar ke print kare.

Fir opening "\<ul\>" print kar ke, hum humne `batch1_students` waali list pe loop chala ke har ek student ke naam ko `li` tags ke andar print kara. Abhi toh humne ek list print kari hai, aise hi hum bahot saare HTML pages python ka use kar ke bana sakte hain.

File mein likhne ke baad `close` karne ki zaroorat kyun padti hai? Yeh samajhne ke liye hum pehle yeh code try karenge:

```python
my_file3 = open("test_file.txt", "w")
my_file3.write("Yahan main kuch likha")
my_file3.write("\nYaha maine kuch aur bhi likha.")
```

Abhi tak humne yeh waali file close nahi kiya. Aapko folder mein ek `test_file.txt` naam ki ek file ko dikhne lag jayegi. Lekin jab aap yeh nahi file kholenge toh aapko woh khaali milegi Kyunki jab tak hum close ka use nahi karte, tab tak python uss file ko save nahi karta hai.

```python
my_file3.close()
```

Ab humne is file ko close kar diya. Ab aap "test_file.txt" ko khol ke dekhoge toh aapko woh dikhega jo humne likha tha. Agar hum ek aisi file mein `write` karne ki koshih karenge jisko hum band kar chuke hain toh python humein error de degi. Yeh karne ki koshish karo:

```python
my_file3.write("Kuch aur likhte hain")
```

Aap dekhoge ki python error dikha deti hain. Error mein python bolti hai, "ValueError: I/O operation on closed file" Iska matlab hai ki hum ek band file ke saath kuch nahi kar sakte