callbacks-in-asynchronous-functions_key1


callbacks-in-asynchronous-functions_key2


```javascript
function callback(){
   console.log("hi from callback after 1 second")
}
 
setTimeout(callback, 1000)
 
Let’s see how setTimeout works if you give JavaScript another task to complete:
 
const tenSecondsLater = () => console.log('10 seconds passed!')
 
setTimeout(tenSecondsLater, 10000)

console.log('Start!')
```

callbacks-in-asynchronous-functions_key3


callbacks-in-asynchronous-functions_key4


callbacks-in-asynchronous-functions_key5


callbacks-in-asynchronous-functions_key6


callbacks-in-asynchronous-functions_key7


callbacks-in-asynchronous-functions_key8


callbacks-in-asynchronous-functions_key9


callbacks-in-asynchronous-functions_key10


```javascript
const orderPizza = flavour => {
   
   callPizzaShop(`I want a ${flavour} pizza`)
   
callbacks-in-asynchronous-functions_key11

   
callbacks-in-asynchronous-functions_key12

 
callbacks-in-asynchronous-functions_key13


callbacks-in-asynchronous-functions_key14


callbacks-in-asynchronous-functions_key15


callbacks-in-asynchronous-functions_key16


callbacks-in-asynchronous-functions_key17
callbacks-in-asynchronous-functions_key18
