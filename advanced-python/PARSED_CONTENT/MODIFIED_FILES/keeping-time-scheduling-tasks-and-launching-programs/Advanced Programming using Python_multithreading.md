multithreading_key1
multithreading_key2


```python
import time, datetime

startTime = datetime.datetime(2029, 10, 31, 0, 0, 0)
while datetime.datetime.now() < startTime:
    time.sleep(1)

print('Program now starting on Halloween 2029')
```

multithreading_key3


multithreading_key4


multithreading_key5


multithreading_key6


```python
   import threading, time
   print('Start of program.')

❶ def takeANap():
       time.sleep(5)
       print('Wake up!')

❷ threadObj = threading.Thread(target=takeANap)
❸ threadObj.start()

   print('End of program.')
```

multithreading_key7


multithreading_key8



multithreading_key9


multithreading_key10


multithreading_key11
