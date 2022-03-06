intro_key1
intro_key2


intro_key3
intro_key4


intro_key5


1. intro_key6
2. intro_key7
3. intro_key8
4. intro_key9
intro_key10


```python
❶ passwordFile = open('SecretPasswordFile.txt')
❷ secretPassword = passwordFile.read()
❸ print('Enter your password.')
typedPassword = input()
❹ if typedPassword == secretPassword:
❺   	 print('Access granted')
❻	if typedPassword == '12345':
❼	print('That password is one that an idiot puts on their luggage.')
else:
❽ 	print('Access denied')
```

intro_key11
