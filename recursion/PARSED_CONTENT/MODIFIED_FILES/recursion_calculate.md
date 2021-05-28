## calculate_key1
```python
def operate(num1, operator, num2):
    if operator=='+':
        return num1 + num2
    elif operator=='-':
        return num1 - num2
    elif operator=='*':
        return num1 * num2
    else:
        return num1 / num2
```
calculate_key2

calculate_key3

calculate_key4

calculate_key5

calculate_key6

## calculate_key7
- calculate_key8
- calculate_key9
- calculate_key10
calculate_key11`base cases`calculate_key12`operate`calculate_key13

`['3', '+', '5', '-', '2', '*', '4', '/', '2', '+', '8', '-', '10', '*', '9']`calculate_key14`[value, '/', '3']`calculate_key15

```python
def operate(num1, operator, num2):
    if operator=='+':
        return num1 + num2
    elif operator=='-':
        return num1 - num2
    elif operator=='*':
        return num1 * num2
    else:
        return num1 / num2

def solve(question_list):
    if len(question_list)==1:
        return int(question_list[0])
    elif len(question_list)==3:
        return operate(int(question_list[0]), question_list[1], int(question_list[2]))
    else:
        return operate(solve(question_list[:-2]), question_list[-2], int(question_list[-1])) 

solve(['3', '+', '5', '-', '2', '*', '4', '/', '2', '+', '8', '-', '10', '*', '9', '/', '3'])
```
## calculate_key16
calculate_key17