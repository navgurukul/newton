```ngMeta
reading-json-with-the-loads()-function_key1
```
# reading-json-with-the-loads()-function_key2
reading-json-with-the-loads()-function_key3

```python
>>> stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0,"felineIQ": null}'
```python
>>> import json
>>> jsonDataAsPythonValue = json.loads(stringOfJsonData)
>>> jsonDataAsPythonValue
```
reading-json-with-the-loads()-function_key4

reading-json-with-the-loads()-function_key5

```python
>>> pythonValue = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie',
'felineIQ': None}
>>> import json
>>> stringOfJsonData = json.dumps(pythonValue)
>>> stringOfJsonData
'{"isCat": true, "felineIQ": null, "miceCaught": 0, "name": "Zophie" }'
```
reading-json-with-the-loads()-function_key6