```ngMeta
name: Operations on primitive data types
```

As you previously read about different data types in javascript. There are some primitive data types on which some operations can be performed which we are going to know about it now.

## Operations on Strings 

- ### Finding the length of a string

To find the length of a string you just need to use a simple property called length.

### Example:

```javascript
let browserType = 'mozi lla';
console.log(browserType.length); // output 8
```

### Explanation:

In the above example we have found the length of a string. This means by using length function it is possible in strings as well, like arrays. Just the difference is in this it counts each and every alphabet of a string including space as well.

If you see, upto m-length is 1, for o-length is 2, for z-length is 3, for i-length is 4, for space -length is 5, for l-length is 6, for again l-length is 7, for a-length is 8.

But in the list the elements are separated by commas.

- ### Retrieving a specific string character

### Example:
```javascript
let browserType = 'mozilla';
browserType[0]; // output ‘m’
 ```

### Explanation:

If we want a particular alphabet of a string so we can access it too by using square brackets same as arrays. Just specify the variable name and the position(Index) of the particular alphabet in [ ] (square brackets). Indexing starts from the same number 0.
 
### Example:
```javascript
let browserType = 'mozilla';
browserType[browserType.length-1]; // output ‘a’
 ```
### Explanation:

In the case of accessing the last element first like python, negative indexing is not available but To retrieve the last character of any string, we could use the following line, combining this technique with the length property we looked at above. The length of "mozilla" is 8, but because the count starts at 0, the character position is 7; using  length-1 gets us the last character.
 
- ### Finding a substring inside a string and extracting it
	
### Example:
```javascript
let browserType = 'mozilla is a company';
browserType.indexOf(‘company’); // output 13
```
 
### Explanation:

This gives us a result of 13, because the substring "company" starts at position 13 (0, 1, 2  — so 13 characters in) inside "mozilla is a company". Such code could be used to filter strings.

### Example:
```javascript
let browserType = 'mozilla is a company';
browserType.indexOf(‘are’); // output -1
```
### Explanation:

This should give you a result of -1 — this is returned when the substring, in this case 'are', is not found in the main string.
 
- ### Changing case
	
### Example:
```javascript	
let radData = 'My NaMe Is MuD';
radData.toLowerCase();  // output ‘my name is mud’
radData.toUpperCase();  // output ‘MY NAME IS MUD’
```
### Explanation:
	
The string methods toLowerCase() and toUpperCase() take a string and convert all the characters to lower- or uppercase, respectively.
 
- ### Updating parts of a string

```javascript
let browserType = 'mozilla';
browserType.replace(‘moz’, ’van’); // output ‘vanilla’
```
### Explanation:

This returns "vanilla" in the console. But if you check the value of browserType, it is still "mozilla". To actually update the value of the browserType variable in a real program, you'd have to set the variable value to be the result of the operation; it doesn't just update the substring value automatically. So you'd have to actually write this: browserType = browserType.replace('moz','van');

**For the next course [clickHere](https://www.merakilearn.org/course/153/exercise/3745)**
 
