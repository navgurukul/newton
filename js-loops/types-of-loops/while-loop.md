**Example** :-

```javascript
var count = 1;
while (count < 10) {
   console.log(count);
   count +=2;
}

// Output :

// 1
// 3
// 5
// 7
// 9

```

**Explanation**:-

count +=2 really just means count = count + 2.

When this loop runs the first time, the value of count is 1, therefore count is printed

When this loop runs the second time, the value of count is 3, therefore count is printed

When this loop runs the third time, the value of count is 5, therefore count is printed

When this loop runs the fourth time, the value of count is 7, therefore count is printed

When this loop runs the fifth time, the value of count is 9, therefore count is printed

When this loop runs the sixth time, the value of count is 11. Clearly, 11>10, so the while loop will stop.

While loop helps us to execute a block of code. While runs upto a specified condition is true and stops once that condition is no longer true.


**Example**:

```javascript

var i=0;
while (i<7){
    if(i%2==0){
console.log(i)
    }
    i++;
}
 

// Output:-
// 0
// 2
// 4
// 6

```


**Explanation**:-

When this loop runs the first time, the value of i is 0, 0< 7 is true, 0%2 ==0 true ,therefore i is printed, and incremented i to 1

When this loop runs the second time, the value of i is 1, 1<7 true, 1%2 ==0 false, therefore i is not printed, and directly incremented to 2

When this loop runs the third time, the value of i is 2, 2< 7 is true, 2%2 ==0 true ,therefore i is printed, and incremented i to 3

When this loop runs the fourth time, the value of i is 3, 3<7 true, 3%2 ==0 false, therefore i is not printed, and directly incremented to 4

When this loop runs the fifth time, the value of i is 4, 4< 7 is true, 4%2 ==0 true ,therefore i is printed, and incremented i to 5

When this loop runs the sixth time,the value of i is 5, 5<7 true, 5%2 ==0 false, therefore i is not printed, and directly incremented to 6

When this loop runs the seventh time, the value of i is 6, 6< 7 is true, 6%2 ==0 true ,therefore i is printed, and incremented i to 7

When this loop runs the eighth time, the value of i is 7, clearly 7<7 is false so the loop breaks here.
