fibonacci-advanced_key1

fibonacci-advanced_key2

fibonacci-advanced_key3

```python
def fib(number):
    if number == 1:
        return 0
    elif number == 2:
        return 1
    else:
        return fib(number-1) + fib(number-2)

def getFibList(number):
    fib_list = []
    key = 1
    while (key < number + 1):
        fib_list.append(fib(key))
        key += 1
    return fib_list

print(getFibList(10))
```
fibonacci-advanced_key4`getFibList`fibonacci-advanced_key5

## fibonacci-advanced_key6
- fibonacci-advanced_key7
- fibonacci-advanced_key8
- fibonacci-advanced_key9
## fibonacci-advanced_key10
```python
def getFibList(number):
    if number == 1:
        return [1]

    elif number == 2:
        return [1, 1]

    else:
        get_previous_fib_list = getFibList(number-1)
        new_last_element = get_previous_fib_list[-1] + get_previous_fib_list[-2]

        # jab hum list mei kuch append karte hai toh, woh list update ho jaati hai
        get_previous_fib_list.append(new_last_element)

        # get_previous_fib_list ab update ho gayi hai, par kyuki ab yeh current list hai, previous nahi\
        # toh confusion avoid karne ke liye hum ek nayi variable mei yeh list daal kar return karenge
        # jisse code padhne wala confuse na ho

        current_fib_list = get_previous_fib_list

        return current_fib_list
```
