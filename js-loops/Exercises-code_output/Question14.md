Try to print this pattern
 
5 5 5 5 5

4 4 4 4 4

3 3 3 3 3

2 2 2 2 2

1 1 1 1 1


```javascript
// please write code here
```

```soolution
var row = 5
while (row>=1){
   var column=1
   str=""
   while(column<=5){
       str=str+row+" ";
       column+=1;
   }
   console.log(str);
   row-=1;
}
```