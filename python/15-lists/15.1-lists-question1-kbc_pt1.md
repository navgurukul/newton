```ngMeta
name: KBC Part 1
completionMethod: peer
```


**Lists ke baare mein seekhne ke liye hum Kaun Banega Crorepati jaise ek game banayenge python ka use kar ke.**

*Yaad rakho ki jahan bhi aap faso, pehle paper pe flowchart banane ki koshish karo.*

Yeh questions alag alag parts mein divided hai. Saare parts ko ek hi file mein code likh kar submit karna hai.

## Part 1

Ek `question` naam ki list banao jisme 5 apni pasand ke questions daalo.

## Part 2

Ab KBC ki tarah har questions ki 4 options hogi, jisme se ek sahi hogi.

Jo bhi 5 questions hain unki options ko alag list mein daalo.

1. Saare questions ki pehli option, `first_options` naam ki list mein daalo.
2. Saare questions ki dusri option, `second_options` naam ki list mein daalo.
3. Saare questions ki teesri option, `third_options` naam ki list mein daalo.
4. Saare questions ki chauthi option, `fourth_options` naam ki list mein daalo.

Jaise maan lo 2 questions aur unki options hain hain:

1. Which country is Delhi located in?
	* India
	* USA
	* France	
	* Czech Republic
2. What is the capital of India?
	* Chandigarh
	* Bhopal
	* Delhi
	* Jaipur

1. Isme `first_options` waali list mein `India` aur `Chandigarh` hogi values.
2. `second_options` waali lsit mein `USA` aur `Bhopal` hogi values.

Aur aise hi dusri lists ki values. 5 questions ke liye har list mein 5 values hogi.

## Part 3

Ek LIST banao jiska naam ho `all_options` jiske ITEMS `first_options`, `second_options`, v aur `fourth_options` wali list ho. Iss list mein dusri lists hongi.

## Part 4
 
Ek LIST banao jiske ITEMS answer key hogi, iss list ka naam `ans_key` hona chaiye. Jaise agar pehle question ka answer pehla option hai toh list ans_key mein 0 daalo aur doosra option hai toh answer key mein 1 daalo.

Example humare example mein pehle question ka sahi javab pehla option hai aur doosre question ka sahi javab teesra option hai. Isliye humari ans_key waali list aisi dikhegi:

```python
ans_key = [0, 2]
```

