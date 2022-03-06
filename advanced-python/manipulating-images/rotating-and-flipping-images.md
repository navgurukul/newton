```ngMeta
name: rotating-and-flipping-images
```
# Rotating and Flipping Images
Images can be rotated with the rotate() method, which returns a new Image object of the rotated image and leaves the original Image object unchanged. The argument to rotate() is a single integer or float representing the number of degrees to rotate the image counterclockwise. Enter the following into the interactive shell:

```python
>>> catIm.rotate(90).save('rotated90.png')
>>> catIm.rotate(180).save('rotated180.png')
>>> catIm.rotate(270).save('rotated270.png')
```
Note how you can chain method calls by calling save() directly on the Image object returned from rotate(). The first rotate() and save() call makes a new Image object representing the image rotated counterclockwise by 90 degrees and saves the rotated image to rotated90.png. The second and third calls do the same, but with 180 degress and 270 degress. The results look like Figure 17-7.

<!-- ![image](assets/000051.jpg)
 -->
Figure 17-7. The original image (left) and the image rotated counterclockwise by 90, 180, and 270 degrees

Notice that the width and height of the image change when the image is rotated 90 or 270 degrees. If you rotate an image by some other amount, the original dimensions of the image are maintained. On Windows, a black background is used to fill in any gaps made by the rotation, like in Figure 17-8. On OS X, transparent pixels are used for the gaps instead.

The rotate() method has an optional expand keyword argument that can be set to True to enlarge the dimensions of the image to fit the entire rotated new image. For example, enter the following into the interactive shell:


>>> catIm.rotate(6).save('rotated6.png')
>>> catIm.rotate(6, expand=True).save('rotated6_expanded.png')
The first call rotates the image 6 degrees and saves it to rotate6.png (see the image on the left of Figure 17-8). The second call rotates the image 6 degrees with expand set to True and saves it to rotate6_expanded.png (see the image on the right of Figure 17-8).

<!-- ![image](assets/000093.jpg)
 -->
Figure 17-8. The image rotated 6 degrees normally (left) and with expand=True (right)

You can also get a “mirror flip” of an image with the transpose() method. You must pass either Image.FLIP_LEFT_RIGHT or Image.FLIP_TOP_BOTTOM to the transpose() method. Enter the following into the interactive shell:


>>> catIm.transpose(Image.FLIP_LEFT_RIGHT).save('horizontal_flip.png')
>>> catIm.transpose(Image.FLIP_TOP_BOTTOM).save('vertical_flip.png')
Like rotate(), transpose() creates a new Image object. Here was pass Image.FLIP_LEFT_RIGHT to flip the image horizontally and then save the result to horizontal_flip.png. To flip the image vertically, we pass Image.FLIP_TOP_BOTTOM and save to vertical_flip.png. The results look like Figure 17-9.

<!-- ![image](assets/000058.jpg)
 -->
Figure 17-9. The original image (left), horizontal flip (center), and vertical flip (right)

