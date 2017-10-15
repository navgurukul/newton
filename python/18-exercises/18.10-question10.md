```ngMeta
name: Question 10
completionMethod: peer
```

Python mein hum ek loop ke andar loop bhi chala sakte hain Sochiye humare paas ek list hai jisme aur list hain jinme integers hain. Kuch aise:

```python
big_list = [[1,2,3], [5,8,9], [4,3,77,521,31,311]]
```

Iss list se agar humne saare numbers ko ek ek kar ke print karna hai toh hum kuch aisa code likh sakte hain:

```python
big_list = [[1,2,3], [5,8,9], [4,3,77,521,31,311]]
counter1 = 0
while counter1 < len(big_list):
    small_list_length = len(big_list[counter1])
    counter2 = 0
    while counter2 < small_list_length:
        print big_list[counter1][counter2]
        counter2 = counter2 + 1
    counter1 = counter1 + 1
    print '-----'
```
 
Iski output kuch aisi aayegi:

```
1
2
3
-----
5
8
9
-----
4
3
77
521
31
311
```

* Yahan pehle woh `for small_list in big_list` wala loop chala ke uski pehli iteration mein pahunchta hai.
* Fir jab small_list ki value mein pehli list, [1,2,3] aati hai uspe pura dusra loop chalta hai
* Dusra loop poora chalne ke baad print `-----` line chalti hai aur fir yeh code pehle loop mein jaata hai
* Fir `small_list` ki value mein `[5,8,9]` jaata hai aur fir pura andar waala loop chalta hai.

Iss code ko python visualizer (www.pythontutor.com) mein chala ke ache se samjho


## Question

Socho aapke paas ek school ki class mein har student ke har subject ke marks hain. Jaise

```python
marks = [[45, 21, 42, 63], [12, 42, 42, 53], [42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]]
```

Yeh ek list mein andar aur lists hain. Andar waali list mein har bache ke saare subjects mein marks hain. Ek `max_marks` naam ka function banao jo ki ek aisi list le aur har students ke maximum marks print kare.

Jaise agar main aapke `max_marks` function ko upar waali list ke saath call karunga , 

```python
max_marks(marks)
```

Toh uski output yeh honi chaiye:

```
63
53
90
94
99
```
Dekhiye ki har line har student ke maximum marks print hue hain.