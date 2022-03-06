```ngMeta
name:  cropping-images
```
# Cropping Images
Cropping an image means selecting a rectangular region inside an image and removing everything outside the rectangle. The crop() method on Image objects takes a box tuple and returns an Image object representing the cropped image. The cropping does not happen in place—that is, the original Image object is left untouched, and the crop() method returns a new Image object. Remeber that a boxed tuple—in this case, the cropped section—includes the left column and top row of pixels but only goes up to and does not include the right column and bottom row of pixels.

Enter the following into the interactive shell:

```python
>>> croppedIm = catIm.crop((335, 345, 565, 560))
>>> croppedIm.save('cropped.png')
```
This makes a new Image object for the cropped image, stores the object in croppedIm, and then calls save() on croppedIm to save the cropped image in cropped.png. The new file cropped.png will be created from the original image, like in Figure 17-4.

<!-- ![image](assets/000043.jpg)
 -->
Figure 17-4. The new image will be just the cropped section of the original image.


