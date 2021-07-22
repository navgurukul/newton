```ngMeta
name: Question 7

```

```python
# `raw_input` ka use kar ke user se din aur abhi ka samay (lunch, dinner) input
# leke uss samay ka menu print karvana hai. Abhi hum sirf monday aur tuesday ke
# liye likh rahe hain
# Monday aur Tuesday dono time daal roti banegi, bas Tuesday raat ko Pav Bhaji banegi
# Neeche waale program mein jab tuesday daalte ho toh pav bhaji print nahi hota.
# Isko sahi karo.
day = input("Aaj ka din kya hai? (monday/tuesday) > ")
time = input("Kaunse samay ka khana banana hai? (lunch/dinner) > ")
if day == "monday" or day == "tuesday":
    print ("Daal-Roti banegi aaj")
elif day == "tuesday" and time == "dinner":
    print ("Pav-Bhaji banegi aaj toh :)")
```

Save the correct code in a new file and submit it.
