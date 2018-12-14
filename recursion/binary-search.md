```ngMeta
submissionType: url
```
## Binary Search

Humei ek list mei koi element search karna hai. Ek example lete hai.

```python
to_find_list = [2, 5, 9, 12, 81, 23, 71, 28, 90, 67]
to_find_element = 81
```

Ab aise sochiye ki humein dekhna hai ki `to_find_element`, `to_find_list` mei hai ya nahi. Agar aap `to_find_list` ko do parts mei divide kar doge, toh kya aap yeh dekh paa rahe hai, ki agar `to_find_element` - `to_find_list` mei hai, toh woh inn dono mei se kisi part mei toh jaroor hoga.

Kyuki `to_find_list` mei 10 elements hai, toh dono parts ko 5-5 elements each milenge.

```python
first_part = [2 , 5, 9, 12, 81]
second_part = [23, 71, 28, 90, 67]
```

`81` element jo humei search karna tha woh pehle list mei hai.

Toh agar aap dekhein toh

`to_find_element` - `to_find_list` mei hoga agar woh uske dono mei se kisi part mei hai, nahi toh nahi hoga. Toh aap iss information ko use kar kar code likhein jo element ko search karta hai.

Dhyaan rakhein ki dheere dheere dono parts ya toh empty ho jayenge, ya usmei ek single element bachega jo `to_find_element` ke equal hoga.

## Solution
```python
def is_present_in_list(number_to_search, list_to_search):
    length_of_list = len(list_to_search)

    if length_of_list == 0:
        return False

    if length_of_list == 1:
        # list_to_search[0] is the only element left in this list
        if number_to_search == list_to_search[0]:
            return True
        else:
            return False

    first_half_of_list = list_to_search[:length_of_list/2]
    second_half_of_list = list_to_search[length_of_list/2:]

    return is_present_in_list(number_to_search, first_half_of_list) or is_present_in_list(number_to_search, second_half_of_list)

print is_present_in_list(3, [3, 5, 7, 8, 4, 6, 2, 1, 9])
print is_present_in_list(10, [3, 5, 7, 8, 4, 6, 2, 1, 9])
```

## Dhyaan Rakhein
```python
def is_present_in_list(number_to_search, list_to_search):
    counter = 0
    while (counter < len(list_to_search)):
        if number_to_search == list_to_search[counter]:
            return True
        counter += 1

    return False

print is_present_in_list(3, [3, 5, 7, 8, 4, 6, 2, 1, 9])
print is_present_in_list(10, [3, 5, 7, 8, 4, 6, 2, 1, 9])
```

use kar kar abhi tak humne yeh code likha tha. Yeh kaafi efficient tareeka bhi hai. Par humne recursion wala tareeka apni understanding build karne ke liye hi kiya hai.
