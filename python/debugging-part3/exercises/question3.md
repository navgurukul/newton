```ngMeta
name: Question 3
completionMethod: peer
```

Jaise hum list ki length nikalne ki len ka use karte aa rahe hain, waise hi hum strings ki length nikalne ke liye len ka use kar sakte hain.

```python
string_name = "Shakrudin"
print len(srtring_name)
```

Yahan print command 9 print karegi kyunki `"Shakrudin"` mein 9 letters ya charecters hai.

``python
string_name = "Rishabh Verma"
print len(string_name)
```

Yahan 13 print hoga kyunki "Rishabh" ke 7 letter aur "Verma" ke 5 letter ki ilava beech ka space bhi ek character hai.

Aur jaise hum `in` ka use kar ke yeh dekh sakte hain ki koi item list mein hai ya nahi. Waise hi hum in string ke saath bhi use kar sakte hain. Jaise:

```python
string_name = "navgurukul"
if "n" in string_name:
    print "n hai"
else:
    print "n nahi hai"
```

Wahan hum yeh dekh rahe hain ki `string_name` variable mein `n` hai ya nahi. Basically `in` ka use kar ke hume ek boolean milta hai.

```python
print "n" in string_name:
print type("n" in string_name)
```

Yahan pehli command True print karegi. Kyunki True or False boolean hote hain, hum inko if statement mein use kar sakte hain. agar hum iska data type dekhenge toh woh bhi "bool" dikhayega Aapko agli kuch exercises mein iski zaroorat padegi ;-)

Hum online account banate wakt bahot jagah password set karte hain. Jaise aapne slack aur gmail ka account banate hue bhi apne passwords set kare honge. Humare accounts ke passwords secret hote hain jo kisi ko pata nahi lagna chaiye. Yeh jitne complex honge kisi aur ke liye guess karna utna mushkil ho jayega. Jaise`'rahulverma'` ko guess karna aasan hai, lekin `'rahul$%verma12!'` ko guess karna mushkil hai. Iss vajah se aap jab bhi online account banaoge toh ek acha sakht password set karna important hota hai.

Hum iss program mein ek password checker banayenge jo yeh sunchit karega ki humara password strong hai.

* Pehle user se ek password ka string input lijiye.
* Fir check kariye ki user ka password sakht hai ya nahi. Ek sakht password ko yeh sab rule follow karne chaiye:
	1. Kam se kam uski length 6 honi chaiye
	2. Jada se jada length 16 se jyada na ho
	3. Kam se kam ek dollar ka sign ($) hona chaiye
	4. Kam se kam password mein 2 ya 8 hona chaiye
	5. Password mein capital A ya capital Z hona chaiye
* Agar password yeh rules follow kar raha hai toh "Strong Password" print karo, nahi toh "Weak Password" type karo