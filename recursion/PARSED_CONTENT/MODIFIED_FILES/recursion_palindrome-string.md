## palindrome-string_key1
palindrome-string_key2`nayan`palindrome-string_key3`nayan`palindrome-string_key4`nayan`palindrome-string_key5

`naina`palindrome-string_key6`naina`palindrome-string_key7`anian`palindrome-string_key8

palindrome-string_key9`string`palindrome-string_key10`palindrome`palindrome-string_key11

## palindrome-string_key12
- palindrome-string_key13
- palindrome-string_key14
- palindrome-string_key15
- palindrome-string_key16
## palindrome-string_key17
```python
def ifPalindrome(string):
    if string == "":  # BASE CASE CONDITION
        return True
    elif len(string) == 1:  # BASE CASE CONDITION
        return True
    elif string[0] == string[len(string)-1]:  # RECURSION
        return ifPalindrome(string[1:][:-1])
    else:
        return False
```
