```ngMeta
name: Question 11
completionMethod: peer
```

Google jaise bade search engine ek web page pe saare text ko samajhte hain. Fir aap kuch bhi search karo, toh google sahi webpages dikha deta hai. Inn sab kaam ke liye google ko ek page se saare words nikalne padte hain. Hume pehle ek poore paragraph mein se words nikalne hain. Iske liye pehle strings mein se hume words nikalne padenge. Socho aapke paas ek string hai.

```python
sentence = "NavGurukul is an alternative to higher education reducing the barriers of current formal education system"
```

Aapne ek `break_into_words` naam ka function likhna hai, jo ek parameter lega jisme ek string hoga. Isko jab hum ek words ka string denge. Jaise break_into_words(sentence) doge toh usko ek words ki list return karni hai.

Jaise aapke `break_into_words(sentence)` ki output yeh honi chaiye:

```python
['NavGurukul', 'is', 'an', 'alternative', 'to', 'higher', 'education', 'reducing', 'the', 'barriers', 'of', 'current', 'formal', 'education', 'system']
```

Hint: Python mein strings bhi list ki tarah hote hain. Jaise:

```python
words = "navgurukul is great"
counter = 0
while counter < len(words)
    print words[counter]
````

Iss loop mein har iteration mein i ki value ek ek character se update hogi. Ek baar iss code ko python visualizer mein run kar ke dhang se samajh lo.

