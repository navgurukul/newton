```ngMeta
name: Question 5
completionMethod: peer
```

Yeh question 3 parts mein. Teenon parts ka code likh ke ek hi file mein submit karo.

## Part 1
`calculator` naam ka ek function banao jo teen argument leta ho - `number_x`, `number_y`, `operation`. `number_x` aur `number_y` mein hum humesha do integers denge aur operation mein kaunsa operation karna hai woh denge. Jaise:

* Agar operation mein "add" diya toh number_x aur number_y ko add kar ke returna karega.
*  Agar operation mein "subtract" diya toh number_x aur number_y ko subtract kar ke return karenge.
*  Agar operation mein "multiply" diya toh number_x ko number_y se multiply kar ke returna karega.
*  Agar operation mein "divide" diya toh number_x ko number_y se divide kar ke return karega

Neeche kuch function calls ke examples diye hue hain:

* `calculator(20, 25, "add")` call karne pe 45 returna karega. 45 hume 20+25 karne se milega.
* `calculator(40, 3, "subtract")` call karne pe 37 return karega. 37 hume 40-3 karne se milega.
* `calculator(10, 4, "multiply")` call karne pe 40 return karega. 40 hume 10*4 karne se milega.
* `calculator(40, 4, "divide")` call karnse pe 10 return karega. 10 hume 40/3 karne se milega.

Function likhne ke baad, yeh kaam karne ke liye function call karo aur variable mein value daalo.

* 24 aur 20 ko add karo aur number_1 variable mein value daalo
* 50 aur 60 ko multiply karo aur number_2 variable mein value daalo
* 80 aur 120 ko divide karo aur number_3 variable mein value daalo
* 90 aur 23 ko subtract karo aur number_4 variable mein value daalo


## Part 2

Ab `raw_input` ka use kar ke user se 2 numbers input lo.

**Note: Yeh karne ke liye koi function banane ki zaroorat nahi hai.**

Fir calculator function ko 4 baar call call kar ke inn dono numbers do add, subtract, multiply, divide karo aur result ko 4 alag variables mein daalo. Woh variables ka naam yeh hoga:

* *add_result* add operation ka result store karega
* *subtract_result* subtract operation ka result store karega
* *multiply_result* multiple operation ka result store karega
* *divide_result* divide operation ka result store karega

Fir upar wale chaaron variables ko print karo.


Final code ko submit karo :)

## Part 3

`list_change` naam ka ek function ka code likho jo 2 lists jisme integers arguments ki tarah le aur fir unn lists ki woh items jo same index number (kram) pe hain unko multiply kar ke ek nayi list return karvaye.

**Aapko multiply karne ke liye *calculator* function ka use karna hai. Normal tareeke se multiply nahi kar sakte ho.**

Jaise agar hum function ko aise call karenge toh:

```python
multiple_list = list_change([5, 10, 50, 20], [2, 20, 3, 5])
```

Yahan *multiple_list* ki yeh value honi chaiye:

```python
[10, 200, 150, 100]
```

10, 5 aur 2 ko multiple kar ke aaya, 200 10 aur 20 ko multiple kar ke, 150 50 aur 3 ko, 100 20 aur 5 ko.