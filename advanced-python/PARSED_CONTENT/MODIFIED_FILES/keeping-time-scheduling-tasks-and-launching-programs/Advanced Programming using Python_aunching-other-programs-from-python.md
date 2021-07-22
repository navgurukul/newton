```ngMeta
aunching-other-programs-from-python_key1
```

aunching-other-programs-from-python_key2
aunching-other-programs-from-python_key3


aunching-other-programs-from-python_key4


aunching-other-programs-from-python_key5


![image](assets/000013.jpg)aunching-other-programs-from-python_key6


aunching-other-programs-from-python_key7


aunching-other-programs-from-python_key8


```python
>>> import subprocess
>>> subprocess.Popen('C:\\Windows\\System32\\calc.exe')
```
aunching-other-programs-from-python_key9
```python
>>> import subprocess
>>> subprocess.Popen('/usr/bin/gnome-calculator')
```
aunching-other-programs-from-python_key10


aunching-other-programs-from-python_key11


aunching-other-programs-from-python_key12


aunching-other-programs-from-python_key13


aunching-other-programs-from-python_key14


```python
❶ >>> calcProc = subprocess.Popen('c:\\Windows\\System32\\calc.exe')
❷ >>> calcProc.poll() == None
```
aunching-other-programs-from-python_key15
```python
❸ >>> calcProc.wait()
```
aunching-other-programs-from-python_key16
```python
   >>> calcProc.poll()
```
aunching-other-programs-from-python_key17
