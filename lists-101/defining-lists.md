## Defining Lists

Lists ko define kar ne ke liye hum `square brackets use karte hai` - [].

Jab bhi aap `[` dekhein, toh samjhe, list ki definition shuru ho gayi hai, aur `]` se list ki defintion khatam ho gayi hai.

# Kuch Examples

Iss example mein hum kuch bachon ki naam ki list store kar rahe hain.

```python
names_list = ["rahul", "shivam", "kavay", "ashish", "rohit"]
print names_list
print type(names_list)
```

Aakhri line mein humne `type` ka use kiya hai. `type` function se hum dekhenge python mein iska type kya hai.

Yeh ek `strings ki list` hai kyunki iski saari values mein string hain.

**Note kariye, ki LIST ko start karne ke liye `[` use hota hai and band karne ke liye `]` use hota hai. `[ ]` ki shape square jaise dekhti hai, isliye inhe SQUARE BRACKEtS kaha jata hai**

Lists ke andar hum koi bhi object daal sakte hain. Yeh string, integer ya kisi bhi aur data type ka ho sakta hai.

## STRINGS ki LIST
Yeh kuch banks ke naam ki list hai
```python
banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
print banks_list
print type(banks_list)
```

## INTEGERS ki LIST
Yeh ek student ke boards ki marks ki list hai.

```python
marks_list = [70, 80, 75, 65, 68]
print marks_list   
print type(marks_list)
```

## FLOATS ki LIST
Yeh pichle saat dinon mein temperatures ki list hai.

```python
temperature_list = [21.1, 24.3, 19, 25, 17, 18, 23]
print temperature_list
```

Lekin hum jab bhi ek list variable pe `type` function ka use karenge, toh humesha uska type list dikhayega. Lekin list ke andar kuch bhi type ho sakte hain.

## Exercises

1. Aap apne friends ki ek `list` banaye
2. Aap aap jin jin countries ko visit karna chahte hai unki ek `list` banaye
3. Aap peechle 5 mahine ke `total expenses` kitne hue, uski ek `list` banaye (jaise maan lo, peechle mahine 58750 ke expenses hue, and so on)