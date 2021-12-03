```ngMeta
name: Arrays
```
##### Look at this example :

#### Example:

This program is trying to print numbers whose value is greater than 5.

```javascript

var numbers = [1, 2, 6, 8, 12, 14];
var result = numbers.filter(element => element>5)
console.log(result);
```
 
Output:
[6, 8, 12, 14]


#### Explanation:

Filter directly works on arrays in the above example you can see. It will run a loop through the entire length of the array (as in the array numbers above)

When the filter function receives the first element in the numbers array i.e. 1, it checks the condition
is 1>5, that is false,So 1 is not added to our new variable result. The function then moves on to the next element in the array numbers, which is 2.

The filter is running for the second element in the numbers array i.e. 2, it checks the condition
is 2>5, that is false ,So 1 is not added to our new variable result. The function then moves on to the next element in the array numbers, which is 6.

The filter is running for the third element in the numbers array i.e. 6, it checks the condition
is 6>5, that is true ,So 6 is  added to our new variable result. The function then moves on to the next element in the array numbers, which is 6.

The filter is running for the fourth element in the numbers array i.e. 8, it checks the condition
is 8>5, that is true ,So 6 is  added to our new variable result. The function then moves on to the next element in the array numbers, which is 12.

The filter is running for the third element in the numbers array i.e. 12, it checks the condition
is 12>5, that is true ,So 12 is  added to our new variable result. The function then moves on to the next element in the array numbers, which is 14.

The filter is running for the third element in the numbers array i.e. 14, it checks the condition
is 14>5, that is true ,So 14 is  added to our new variable result. The function then moves on to the next element in the array numbers ,And there are no other elements so it will stop running the loop.


As the result filter will print the new list with the elements that have been true by the test condition i.e element>5. So, we will get [6, 8, 12, 14].

Think that you went to a shopping mall to buy a dress, the shop members show you the best collection of their dresses, but you won’t choose all, you will filter them by the design, color or by measurements.. Sometimes you may select one, sometimes if you like two you will buy two that are totally based on your conditions whether you are selecting them or  not.


#### Note:

Filter returns a new array of the original array elements (with no change to the original values). filter will only return elements where they pass some test applied in function.
