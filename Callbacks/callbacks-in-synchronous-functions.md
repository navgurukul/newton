```ngMeta
name: Callbacks in synchronous functions
```

Callbacks are used in two different ways — in ***synchronous functions** and **asynchronous functions**.

If your code executes in a top to bottom, left to right fashion, sequentially, and waiting until one code has finished before the next line begins, then your code is synchronous.

Let’s look at an example:

```javascript
const addOne = (n) => n + 1
addOne(1) // 2
addOne(2) // 3
addOne(3) // 4
addOne(4) // 5
```

In the example above, addOne(1) executes first. Once it’s done, addOne(2) begins to execute. Once addOne(2) is done, addOne(3) executes. This process goes on until the last line of code gets executed.

Callbacks are used in synchronous functions when you want a part of the code to be easily swapped with something else.

Let’s go through another example. This time, let’s say you wanted to filter an array of numbers to get a list that’s less than five. Here, you pass a callback into the filter function:

```javascript
const numbers = [3, 4, 10, 20]
const lesserThanFive = numbers.filter(num => num < 5)
```

Now, if you do the above code with named functions, filtering the array would look like this instead:

```javascript
const numbers = [3, 4, 10, 20]
const getLessThanFive = num => num < 5
 
// Passing getLessThanFive function into filter
const lesserThanFive = numbers.filter(getLessThanFive)
```
In this case, getLessThanFive is the callback. Array.filter is a function that accepts a callback function.

So, back in the Array.filter example above, although we filtered the array to contain numbers that are less than five, you could easily reuse Array.filter to obtain an array of numbers that are greater than ten:

```javascript
const numbers = [3, 4, 10, 20]
const getLessThanFive = num => num < 5
const getMoreThanTen = num => num > 10
 
// Passing getLessThanFive function into filter
const lesserThanFive = numbers.filter(getLessThanFive)
 
// Passing getMoreThanTen function into filter
const moreThanTen = numbers.filter(getMoreThanTen)
```

This is why you’d use callbacks in a synchronous function. Now, let’s move on and look at why we use callbacks in asynchronous functions.
