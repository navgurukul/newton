python-introduction_key1
python-introduction_key2


python-introduction_key3
python-introduction_key4


python-introduction_key5


1. python-introduction_key6
2. python-introduction_key7
3. python-introduction_key8
4. python-introduction_key9
python-introduction_key10


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

python-introduction_key11
