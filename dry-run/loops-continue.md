```ngMeta
name: Using Continue
completionMethod: manual
```

![How Continue Statements Work!](assets/how-continue-statement-works.jpg)
Agar aap yeh diagram dekhoge toh aap samjhoge, ki `continue` command se hum loop mei
- jo bhi `continue` ke baad code hai uss loop mei, woh `execute` nahi hota
- loop ki starting mei `control flow` pahuch jaata hai

Ab iss idea ko use karte hue in example codes ka `dry run` karein.

__Ek baar dhyaan se dekhein ki break aur continue mei kya difference hai__

```python
for val in "string":
    if val == "i":
        continue
    print(val)

print("The end")
```