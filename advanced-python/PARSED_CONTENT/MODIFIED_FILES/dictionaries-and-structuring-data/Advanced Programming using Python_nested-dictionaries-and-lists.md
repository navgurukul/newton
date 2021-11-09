nested-dictionaries-and-lists_key1
nested-dictionaries-and-lists_key2


```python
   allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
                'Bob': {'ham sandwiches': 3, 'apples': 2},
                'Carol': {'cups': 3, 'apple pies': 1}}
```
```python
   def totalBrought(guests, item):
       numBrought = 0
❶     for k, v in guests.items():
❷         numBrought = numBrought + v.get(item, 0)
       return numBrought

   print('Number of things being brought:')
   print(' - Apples         ' + str(totalBrought(allGuests, 'apples')))
   print(' - Cups           ' + str(totalBrought(allGuests, 'cups')))
   print(' - Cakes          ' + str(totalBrought(allGuests, 'cakes')))
   print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
   print(' - Apple Pies     ' + str(totalBrought(allGuests, 'apple pies')))
```
nested-dictionaries-and-lists_key3


nested-dictionaries-and-lists_key4



nested-dictionaries-and-lists_key5
- nested-dictionaries-and-lists_key6
- nested-dictionaries-and-lists_key7
- nested-dictionaries-and-lists_key8
- nested-dictionaries-and-lists_key9
- nested-dictionaries-and-lists_key10
nested-dictionaries-and-lists_key11


nested-dictionaries-and-lists_key12
nested-dictionaries-and-lists_key13
