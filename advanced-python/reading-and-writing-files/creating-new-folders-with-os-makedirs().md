```ngMeta
name: creating-new-folders-with-os-makedirs()
completionMethod: manual
```
# Creating New Folders with os.makedirs()
Your programs can create new folders (directories) with the os.makedirs() function. Enter the following into the interactive shell:

```python
>>> import os
>>> os.makedirs('C:\\delicious\\walnut\\waffles')
```
This will create not just the C:\delicious folder but also a walnut folder inside C:\delicious and a waffles folder inside C:\delicious\walnut. That is, os.makedirs() will create any necessary intermediate folders in order to ensure that the full path exists. Figure 8-3 shows this hierarchy of folders.

<!-- ![image](assets/000036.jpg)
 -->
The result of os.makedirs('C:\\delicious \\walnut\\waffles')