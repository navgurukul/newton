```ngMeta
continue_key1
```
# continue_key2
continue_key3

![continue_key4](https://merakidebug.s3.ap-south-1.amazonaws.com/course_images/loops-101/assets/how-continue-statement-works.jpg)

```python
i = 1
while(i <= 10):
    if(i == 5):
         print("Skipped Element :", i)
      continue
    print(i)
```
`Output`continue_key5



```python
counter = 0
string = "navgurukul"
while (counter < len(string)):
    counter += 1

    if string[counter] == "a":
        continue

    if string[counter] == "u":
        continue
    
    print(string[counter])

print("The end", string[counter])
```
continue_key6

continue_key7[continue_key8](https://www.youtube.com/watch?v=rOfNF7gj5t0)
