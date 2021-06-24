## The Array Data Type

Think about a list of your favourite things. For example, 

your mother’s name, Ramani
Your favourite colour, Black
Your favourite number, 1
Your birthdate, Jan 2, 1996

Now imagine you had to store them together as myFavourtiThings in JS. To do this you will use an Array Data Type.

An array is a type of object used for storing multiple values in a single variable.

The simplest way to create an array is by specifying the array elements as a comma-separated list enclosed by square brackets, as shown in the example below:

```javascript   
var languages = ["Telugu", "Tamil", "Kannada"];
var cities = ["Dharamshala", "Bangalore", "Pune"];
console.log(cities[0]);   // Output: Dharamshala
console.log(cities[2]);   // Output: Pune
 ```

Each value (also called an element) in an array has a numeric position, known as its index, and it may contain data of any data type-numbers, strings, booleans, functions, objects, and even other arrays. The array index starts from 0, so that the first array element is arr[0] not arr[1]. For the example above, colours[0] refers to Red.