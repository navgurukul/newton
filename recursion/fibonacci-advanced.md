```ngMeta
name: Fibonacci Advanced
submission_type: url
```
Iss program mei hum ek aisa function banayenge jo fibonacci numbers ki list generate karta ho. Ek bahut asaan tareeka yeh hai ki, jo function humne pehle fibonacci numbers solve karne ke liye banaya tha, hum usi function ko use kar le.

Yeh wala program bahut mushkil nahi hai - agar aap dhyaan se notebook par sochoge.

Jaise:

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

Iss code ka dry run kar kar ya terminal par run kar kar dekhiye, kaise `getFibList` ek list return karta hai, jismei fibonacci numbers hai. Ab yehi list humei recursion se banani hai. Kya aap yeh bana sakte hai?

## Hint

- Yeh single recursion se ho jayega - iska matlab aap koi bhi fibonacci list sirf peechli wali fibonacci list ko use kar kar hi nikal sakte ho

- Ab aapka base case, ek list return karega

- Kyuki aapka function ab ek list return kar raha hai, toh aapko yeh sochna padega ki aapki list mei kya function use karenge recursion karne ke liye.

## Solution
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
