palindrome-string_key1
palindrome-string_key2


palindrome-string_key3


palindrome-string_key4


palindrome-string_key5
- palindrome-string_key6
- palindrome-string_key7
- palindrome-string_key8
- palindrome-string_key9
palindrome-string_key10
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
