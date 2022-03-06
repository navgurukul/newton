```ngMeta
name: Question 6
submission_type: url
```
## Question 6

```python
# Aapke paas ek variable mein `raw_input` se gaadi ki speed ka ek integer hai
speed = int(input("Gaadi ki speed daalo > "))

# Ab aapne speed check kar ke kuch print karna hai:
# Agar 60 se kam hai toh print karna: "Speed kam hai"
# Agar 30 se kam hai toh print karna: "Speed bahot kam hai"
# Agar 100 se zyada hai toh print karo: "Bahot zyada hai"
if speed < 60:
    print("Speed kam hai")
elif speed < 30:
    print("Speed bahot kam hai")
elif speed > 100:
    print("Speed bahot fast hai")

# Isme ek baar speed 20 daal ke dekho aur dekho ki "Speed bahot kam" hai ki
# output aati hai ya nahi. Agar nahi aati toh isko theek karo aur yeh socho
# ki kya problemn hai.
```

Save the correct code in a new file and submit it.
