```ngMeta
opening-files-with-default-applications_key1
```
# opening-files-with-default-applications_key2
opening-files-with-default-applications_key3

opening-files-with-default-applications_key4

```python
>>> fileObj = open('hello.txt', 'w')
>>> fileObj.write('Hello world!')
```
opening-files-with-default-applications_key5```python
>>> fileObj.close()
>>> import subprocess
>>> subprocess.Popen(['start', 'hello.txt'], shell=True)
```
opening-files-with-default-applications_key6

opening-files-with-default-applications_key7

```python
>>> subprocess.Popen(['open', '/Applications/Calculator.app/'])
<subprocess.Popen object at 0x10202ff98>
```
opening-files-with-default-applications_key8

# opening-files-with-default-applications_key9
opening-files-with-default-applications_key10

opening-files-with-default-applications_key11

opening-files-with-default-applications_key12

opening-files-with-default-applications_key13

opening-files-with-default-applications_key14opening-files-with-default-applications_key15