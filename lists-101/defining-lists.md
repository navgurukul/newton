## Defining Lists


To define lists we can use `square brackets` - `[]`.

Whenever you see `[`, then think that list definition has started, and when you see `]`, then think that list definition is ending.

### Some Examples

In this example, we will store the names of students in a list.


```python
names_list = ["rahul", "shivam", "kavay", "ashish", "rohit"]
print names_list
print type(names_list)
```
In the last line we have used `type`. By using this function we will come to know that what is its data type.

This is the `list of strings` because all of its values contain strings.


**Please note that in order to start a `List` ,`[` is used and in order to close `]` is used. `[]` looks like a square shape, that is why these are called `SQUARE BRACKETS`.**

We can put any object inside a `list`. This can be `string, integer` or any other data type.

### `LIST OF STRINGS` 
Yeh kuch banks ke naam ki list hai
```python
banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
print banks_list
print type(banks_list)
```

### `LIST OF INTEGERS`

This is the list of students marks.

```python
marks_list = [70, 80, 75, 65, 68]
print marks_list   
print type(marks_list)
```

### `LIST OF FLOATS` 

This is the list of temperatures of last seven days.

```python
temperature_list = [21.1, 24.3, 19, 25, 17, 18, 23]
print temperature_list
```
But if we will use type function on a list variable, it will always show the type as list.But we the data iside a list can be of any type.

### Exercises

1. Make a `list` of your friends.
2. Make a `list` of all the countries that you want to visit.
3. Make a list of `total expenses` of last 5 months (suppose , your last month expenses were 58750 and so on.)