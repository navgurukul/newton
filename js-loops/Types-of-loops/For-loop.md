**Example** :-
```javascript
for(var i = 0; i < 3; i++){
   console.log(i)
}
// Output :-
// 0
// 1
// 2    

```

**Explanation**:

When this loop runs the first time, the value of i is 0, 0<3 is true, and it is incremented due to i++, i value will become 1, therefore i is printed
When this loop runs the second time, the value of i is 1, 1<3 is true, and it is incremented due to i++,i value will become 2, therefore i is printed
When this loop runs the third time, the value of i is 2, 2<3 is true, and it is incremented due to i++,i value will become 3, therefore i is printed
When this loop runs the fourth time, the value of i is 3. Clearly, 3<3, so the for loop will stop.

When we are using a for loop, we can in one line initialize the variable, give the condition, and increment or decrement the variable. For loop runs for a specific number of times.


**Example** :

```javascript
for(var n=9;n>0;n--){
   console.log(n)
}

// Output:-
// 9
// 8
// 7
// 6
// 5
// 4
// 3
// 2
// 1

```

**Explanation**:-

When this loop runs the first time, the value of n is 9, n>0 is true, and it is decremented due to n--, n value will become 8, therefore i is printed
When this loop runs the second time, the value of n is 8, n>0 is true, and it is decremented due to n--,n value will become 7, therefore i is printed
When this loop runs the third time, the value of n is 7, n>0 is true, and it is decremented due to n--, n value will become 6, therefore i is printed
When this loop runs the fourth time, the value of n is 6, n>0 is true, and it is decremented due to n--, n value will become 5, therefore i is printed
….
….
….
….
….
When this loop runs the tenth time, the value of n is 0, 0>0 is false, and the loop breaks.

**Example :-**
```javascript
for (var s=25;s<=30;s++){
   console.log(s)
}


// Output:-
// 25
// 26
// 27
// 28
// 29
// 30
```
**Explanation:-**

When this loop runs the first time, the value of s is 25, 25<=30 is true, and it is incremented due to i++, i value will become 26, therefore 25 is printed

When this loop runs the second time, the value of i is 26, 26<=30 is true, and it is incremented due to i++,i value will become 27, therefore 26 is printed

When this loop runs the third time, the value of i is 27, 27<=30 is true, and it is incremented due to i++,i value will become 28, therefore 27 is printed

When this loop runs the third time, the value of i is 28, 28<=30 is true, and it is incremented due to i++,i value will become 29, therefore 28 is printed

When this loop runs the third time, the value of i is 29, 29<=30 is true, and it is incremented due to i++,i value will become 30, therefore 29 is printed

When this loop runs the third time, the value of i is 30, 30<=30 is true, and it is incremented due to i++,i value will become 31, therefore 30 is printed

When this loop runs the fourth time, the value of i is 3. Clearly, 31<=30 false, so the for loop will stop.
