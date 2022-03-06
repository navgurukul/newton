```ngMeta
name: resizing-an-image
```
# Resizing an Image
The resize() method is called on an Image object and returns a new Image object of the specified width and height. It accepts a two-integer tuple argument, representing the new width and height of the returned image. Enter the following into the interactive shell:

```python
❶ >>> width, height = catIm.size
❷ >>> quartersizedIm = catIm.resize((int(width / 2), int(height / 2)))
   >>> quartersizedIm.save('quartersized.png')
❸ >>> svelteIm = catIm.resize((width, height + 300))
   >>> svelteIm.save('svelte.png')
```
Here we assign the two values in the catIm.size tuple to the variables width and height ❶. Using width and height instead of catIm.size[0] and catIm.size[1] makes the rest of the code more readable.

The first resize() call passes int(width / 2) for the new width and int(height / 2) for the new height ❷, so the Image object returned from resize() will be half the length and width of the original image, or one-quarter of the original image size overall. The resize() method accepts only integers in its tuple argument, which is why you needed to wrap both divisions by 2 in an int() call.

This resizing keeps the same proportions for the width and height. But the new width and height passed to resize() do not have to be proportional to the original image. The svelteIm variable contains an Image object that has the original width but a height that is 300 pixels taller ❸, giving Zophie a more slender look.

Note that the resize() method does not edit the Image object in place but instead returns a new Image object.