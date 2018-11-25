## Palindrome
Palindrome woh string ya number hota hai, jo left se right aur right se left same hota hai. Jaise `nayan` string. Aap isse left se dekhoge toh bhi `nayan` hai, aur right se dekhoge toh bhi `nayan` hai. 

`naina` jaise palindrome nahi hai. Left se yeh `naina` hai, par right se `anian` hai. Aur dono alag alag hai.

Aapko ek function likhna hai recursion use kar kar jo dekhega ki given `string` `palindrome` hai ya nahi.

## Hint
- Agar pehla aur aakhiri character list mei alag hoga, toh list palindrome nahi hai.
- Agar pehla aur aakhiri character list mei same hai, toh list palindrome hai agar bacchi hui list (list mei agar pehla aur aakhiri element hata do toh) palindrome hai. 
- Agar list mei ek character hai, toh woh hamesha palindrome hoga.
- Agar list mei do character hai, aur woh dono same hai toh palindrome hoga, else palindrome nahi hoga.
  
## Solution
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