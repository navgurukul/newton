```ngMeta
name: Do While loop
```

### Example:

```javascript
var i=1
do{
  if(i%2==1){
  console.log(i)
  }
  i++
}
while (i <=10)

// Output:
// 1
// 3
// 5
// 7
// 9    
```
### Explanation:

When i = 1, i%2 =1, and 1==1 true, therefore, 1 is printed. After that it is incremented to 2.

When i = 2, now it will check for loop condition 2<=10 this is true, and it will go to do again, i%2  is 0 not 1, therefore, nothing is printed. After that it is incremented to 3.

When i = 3, now it will check for loop condition 3<=10 this is true, and it will go to do again, i%2==1 true, therefore, 3 is printed. After that it is incremented to 4.

When i = 4, now it will check for loop condition 4<=10 this is true, and it will go to do again, i%2  is 0 not 1, therefore, nothing is printed. After that it is incremented to 5.

When i = 5 now it will check for loop condition 5<=10 this is true, and it will go to do again, i%2==1 true, therefore, 5 is printed. After that it is incremented to 6.

When i = 6, now it will check for loop condition 6<=10 this is true, and it will go to do again, i%2  is 0 not 1, therefore, nothing is printed. After that it is incremented to 7.

When i = 7 now it will check for loop condition 7<=10 this is true, and it will go to do again, i%2==1 true, therefore, 7 is printed. After that it is incremented to 8.

When i = 8, now it will check for loop condition 8<=10 this is true, and it will go to do again, i%2  is 0 not 1, therefore, nothing is printed. After that it is incremented to 9.

When i = 9 now it will check for loop condition 9<=10 this is true, and it will go to do again, i%2==1 true, therefore, 9 is printed. After that it is incremented to 10.

When i = 10, now it will check for loop condition 10<=10 this is true, and it will go to do again, i%2  is 0 not 1, therefore, nothing is printed. After that it is incremented to 11.

When i = 11 now it will check for loop condition 11<=10 clearly this is false, and it won’t go further.

#### Note

The do while loop is a variant of the while loop which evaluates the condition at the end of each loop iteration.
          

### Example:

```javascript
let m=5;
let n=1
do{
   console.log(m*n)
n++
}        
while(n<=4)

// Output:
// 5
// 10
// 15
// 20
```

### Explanation:

m = 5, n = 1, m*n = 5, n++ is 2, 2<=10, so loop will execute another time.

n=2, 2<=4 true, m=5, m*n(5*2) is 10, so 10 is printed and n incremented to 3 

n=3, 3<=4 true, m=5, m*n(5*3) is 15, so 15 is printed and n incremented to 4

n=2, 4<=4 true, m=5, m*n(5*4) is 20, so 20 is printed and n incremented to 5

n=5, 5<=4 is false so loop will stop. 

### Example:

```javascript
let sum=0
let i=0
do{
  sum=sum+i 
  console.log(sum)
  i++
}
while(i<=10)

// Output :-
  
// 0
// 1
// 3
// 6
// 10
// 15
// 21
// 28
// 36
// 45
// 55
```
### Explanation:

In this code i is initial variable it starts from 0 and it will run till 10 

sum is another variable for storing the value of  (sum+i) this operation. every time sum value will change because sum value is inside the loop and variable nature is that it updates the value.when condition will be false then it will give us the last update value.

#### NOTE:  

In do while loop we have to do increment inside the do block if increment will happen out of the do block it will give you error.

### Example:
```javascript
let v=0
do{
   console.log(v)
}
v++
while(v<=3)
 
// Output :-
// SyntaxError: Unexpected identifier
```
	
In the next example, we will increment the variable completely outside the do..while statement.

### Example:

```javascript
let v=0
  do{
   console.log(v)
}
while(v<=3)
v++

// Output:-
// 0
// 0
// 0
// loop will run to infinity
```
### Explanation:

In the first iteration, v is 0, v gets printed, 0<= 3, so loop runs again.

In the second iteration, v is 0, v gets printed, 0<= 3, so loop runs again.

In the third iteration, v is 0, v gets printed, 0<= 3, so loop runs again.

…

Do you see what is happening? v is never getting incremented. Thus this program will run to infinity. 
