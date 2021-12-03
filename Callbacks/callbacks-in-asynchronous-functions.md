```ngMeta
name: Callbacks in asynchronous functions
```

**Asynchronous** here means that, if JavaScript needs to wait for something to complete, it will execute the rest of the tasks given to it while waiting.

An example of an asynchronous function is setTimeout. It takes in a callback function to execute at a later time:

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

In the code above, JavaScript executes setTimeout. Then, it waits for ten second and logs “10 seconds passed!”.

Meanwhile, while waiting for setTimeout to complete in 10 seconds, JavaScript executes console.log("Start!").

So, this is what you’ll see if you log the above code:
What happens:

// > Start! (almost immediately)
// >10 seconds passed! (after 10 seconds)

Ugh. Asynchronous operations sound complicated, aren’t they? But why do we use them everywhere in JavaScript?

To see why asynchronous operations are important, imagine JavaScript is a robot helper you have in your house. This helper is pretty dumb. It can only do one thing at a time. (This behavior is called single-threaded).

Let’s say you tell the robot helper to order some pizza for you. But, the robot is so dumb, that after calling the pizza house, the robots sits at your front door and waits for the pizza to be delivered. It can’t do anything else in the meantime.

You can’t get it to iron clothes, mop the floor, or do anything while it’s waiting. You need to wait 20 minutes till the pizza arrives before it’s willing to do anything else…
(This behavior is called blocking. Other operations are blocked when you wait for something to complete).

```javascript
const orderPizza = flavour => {
   
   callPizzaShop(`I want a ${flavour} pizza`)
   
   waits20minsForPizzaToCome() // Nothing else can happen here
   
   bringPizzaToYou()
 
 }

orderPizza('Hawaiian')

 // These two only starts after orderPizza is completed

mopFloor()

ironClothes()
```
Let’s explain by one more example by putting the dumb robot helper into the context of a browser. Imagine you tell it to change the color of a button when the button is clicked.
