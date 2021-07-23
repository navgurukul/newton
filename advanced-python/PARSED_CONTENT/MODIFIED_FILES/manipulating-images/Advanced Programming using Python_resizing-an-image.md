```ngMeta
resizing-an-image_key1
```

resizing-an-image_key2
resizing-an-image_key3


```python
❶ >>> width, height = catIm.size
❷ >>> quartersizedIm = catIm.resize((int(width / 2), int(height / 2)))
   >>> quartersizedIm.save('quartersized.png')
❸ >>> svelteIm = catIm.resize((width, height + 300))
   >>> svelteIm.save('svelte.png')
```
resizing-an-image_key4


resizing-an-image_key5


resizing-an-image_key6


resizing-an-image_key7
