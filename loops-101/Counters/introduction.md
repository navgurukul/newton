```ngMeta
name: Counters
completionMethod: manual
```

# What are Counters?

While loops mein counter ka ek bahot important concept hota hai. Loops ko hum ek hi kaam ko baar baar karane mein use karte hain. Lekin hum uss kaam ko ek particular time tak hi karana hota hai.

Jaise agar humein 1 se 100 tak numbers print karane hain toh humein toh humein yeh ginti rakhni padegi ki humne kahan tak print kara hai. Isse humein yeh pata chalega ki habhi kitna print karna hai. Loops mein hum counters ka use kar ke yeh ginti rakhte hain.

@[youtube](counter-video-id-here)

## Structure of the Video

1. Take an example of how maintaining a count of things is important. Imagine you have 10,000 balls and you have to transfer 100 to another room. How will you maintain a count? You can keep a track of the number of balls you have transferred till now.
2. Similarly in terms of loops we always need to keep a track of how many times a task needs to be done. In terms of the balls we would see that until the number of balls in the other room gets 100 we will keep on shifting one ball. Write a code for this.
3. Basically counter is helping us keep a track of how many times a loop is run. Two things in combination help us keep a track. The counter and how does the changing of the counter helps us keep a track of how many times a loop needs to run.
4. Let's say we need to print numbers from 1 to 10. Now how can we do it? We will take i as 1 and write the following code:
```python
i = 0.1
while i <=1:
  print("Hello")
  i = i + 0.1
```
Take the notion of a number line basically going from 1 to 10. Basically how many steps does it take to go from 1 to 10. 10 steps. Similarly if the take 0.1 and do a step of 0.1 how does it make a difference? It is doing the same thing. Our loop would still run as many times.
5. How about when we want to print all the even numbers between 1 and 10 and we need to include both the numbers. There are two ways to do this:
```python
# method 1
i = 1
while i <= 10:
  if i % 2 == 0:
    print(i)
  i = i + 1

# method 2
i = 2
while i <= 10:
  print(i)
  i = i + 2
```
6. Let's say we need to write a loop to take an input of some numbers from the user 10 times and then take a sum. There are multiple ways to write this loop and every loop works in a similar way.
```python
# method 1
i = 10
sum = 0
while i >= 1:
  x = input("Enter the number> ")
  x = int(x)
  sum = sum + x
  i = i - 1

# method 2
i = 1
sum = 0
while i <= 10:
  x = input("Enter the number> ")
  x = int(x)
  sum = sum + x
  i = i + 1

# method 3
i = 651
sum = 0
while i <= 660:
  x = input("Enter the number> ")
  x = int(x)
  sum = sum + x
  i = i + 1
```
7. Go through and do some examples which are given for you in the next set of examples.
