```ngMeta
getting-the-traceback-as-a-string_key1
```
# getting-the-traceback-as-a-string_key2
getting-the-traceback-as-a-string_key3

getting-the-traceback-as-a-string_key4


getting-the-traceback-as-a-string_key5

getting-the-traceback-as-a-string_key6


getting-the-traceback-as-a-string_key7getting-the-traceback-as-a-string_key8

getting-the-traceback-as-a-string_key9

getting-the-traceback-as-a-string_key10

```python
>>> import traceback
>>> try:
         raise Exception('This is the error message.')
except:
         errorFile = open('errorInfo.txt', 'w')
         errorFile.write(traceback.format_exc())
         errorFile.close()
         print('The traceback info was written to errorInfo.txt.')
```
getting-the-traceback-as-a-string_key11


getting-the-traceback-as-a-string_key12getting-the-traceback-as-a-string_key13