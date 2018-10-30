```ngMeta
name:  practice-questions
completionMethod: manual
```
# Practice Questions

Q:

1. What does the code for an empty dictionary look like?

Q:

2. What does a dictionary value with a key 'foo' and a value 42 look like?

Q:

3. What is the main difference between a dictionary and a list?

Q:

4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?

Q:

5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?

Q:

6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?

Q:

7. What is a shortcut for the following code?


if 'color' not in spam:
    spam['color'] = 'black'
Q:

8. What module and function can be used to “pretty print” dictionary values?

# Practice Projects
For practice, write programs to do the following tasks.

# Fantasy Game Inventory
You are creating a fantasy video game. The data structure to model the player’s inventory will be a dictionary where the keys are string values describing the item in the inventory and the value is an integer value detailing how many of that item the player has. For example, the dictionary value {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} means the player has 1 rope, 6 torches, 42 gold coins, and so on.

Write a function named displayInventory() that would take any possible “inventory” and display it like the following:


Inventory:
12 arrow
42 gold coin
1 rope
6 torch
1 dagger
Total number of items: 62
Hint: You can use a for loop to loop through all the keys in a dictionary.


# inventory.py
```python
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        # FILL IN THE CODE HERE
    print("Total number of items: " + str(item_total))

displayInventory(stuff)
```
