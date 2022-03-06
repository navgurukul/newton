callbacks-in-synchronous-functions_key1


callbacks-in-synchronous-functions_key2


callbacks-in-synchronous-functions_key3


```javascript
const addOne = (n) => n + 1
addOne(1) // 2
addOne(2) // 3
addOne(3) // 4
addOne(4) // 5
```

callbacks-in-synchronous-functions_key4


callbacks-in-synchronous-functions_key5


callbacks-in-synchronous-functions_key6


```javascript
const numbers = [3, 4, 10, 20]
const lesserThanFive = numbers.filter(num => num < 5)
```

callbacks-in-synchronous-functions_key7


```javascript
const numbers = [3, 4, 10, 20]
const getLessThanFive = num => num < 5
 
// Passing getLessThanFive function into filter
const lesserThanFive = numbers.filter(getLessThanFive)
```
callbacks-in-synchronous-functions_key8


callbacks-in-synchronous-functions_key9


```javascript
const numbers = [3, 4, 10, 20]
const getLessThanFive = num => num < 5
const getMoreThanTen = num => num > 10
 
// Passing getLessThanFive function into filter
const lesserThanFive = numbers.filter(getLessThanFive)
 
// Passing getMoreThanTen function into filter
const moreThanTen = numbers.filter(getMoreThanTen)
```

callbacks-in-synchronous-functions_key10
