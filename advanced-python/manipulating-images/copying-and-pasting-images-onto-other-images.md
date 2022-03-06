```ngMeta
name: copying-and-pasting-images-onto-other-images
```
# Copying and Pasting Images onto Other Images
The copy() method will return a new Image object with the same image as the Image object it was called on. This is useful if you need to make changes to an image but also want to keep an untouched version of the original. For example, enter the following into the interactive shell:

```python
>>> catIm = Image.open('zophie.png')
>>> catCopyIm = catIm.copy()
```
The catIm and catCopyIm variables contain two separate Image objects, which both have the same image on them. Now that you have an Image object stored in catCopyIm, you can modify catCopyIm as you like and save it to a new filename, leaving zophie.png untouched. For example, let’s try modifying catCopyIm with the paste() method.

The paste() method is called on an Image object and pastes another image on top of it. Let’s continue the shell example by pasting a smaller image onto catCopyIm.

```python
>>> faceIm = catIm.crop((335, 345, 565, 560))
>>> faceIm.size
```
(230, 215)
```python
>>> catCopyIm.paste(faceIm, (0, 0))
>>> catCopyIm.paste(faceIm, (400, 500))
>>> catCopyIm.save('pasted.png')
```
First we pass crop() a box tuple for the rectangular area in zophie.png that contains Zophie’s face. This creates an Image object representing a 230×215 crop, which we store in faceIm. Now we can paste faceIm onto catCopyIm. The paste() method takes two arguments: a “source” Image object and a tuple of the x- and y-coordinates where you want to paste the top-left corner of the source Image object onto the main Image object. Here we call paste() twice on catCopyIm, passing (0, 0) the first time and (400, 500) the second time. This pastes faceIm onto catCopyIm twice: once with the top-left corner of faceIm at (0, 0) on catCopyIm, and once with the top-left corner of faceIm at (400, 500). Finally, we save the modified catCopyIm to pasted.png. The pasted.png image looks like Figure 17-5.

<!-- ![image](assets/000031.jpg)
 -->
Figure 17-5. Zophie the cat, with her face pasted twice

Note
Despite their names, the copy() and paste() methods in Pillow do not use your computer’s clipboard.

Note that the paste() method modifies its Image object in place; it does not return an Image object with the pasted image. If you want to call paste() but also keep an untouched version of the original image around, you’ll need to first copy the image and then call paste() on that copy.

Say you want to tile Zophie’s head across the entire image, as in Figure 17-6. You can achieve this effect with just a couple for loops. Continue the interactive shell example by entering the following:

```python
   >>> catImWidth, catImHeight = catIm.size
   >>> faceImWidth, faceImHeight = faceIm.size
❶  >>> catCopyTwo = catIm.copy()
❷ >>> for left in range(0, catImWidth, faceImWidth):
❸         for top in range(0, catImHeight, faceImHeight):
               print(left, top)
               catCopyTwo.paste(faceIm, (left, top))
```
   0 0
   0 215
   0 430
   0 645
   0 860
   0 1075
   230 0
   230 215
   --snip--
   690 860
   690 1075
```python
   >>> catCopyTwo.save('tiled.png')
```
Here we store the width of height of catIm in catImWidth and catImHeight. At ❶ we make a copy of catIm and store it in catCopyTwo. Now that we have a copy that we can paste onto, we start looping to paste faceIm onto catCopyTwo. The outer for loop’s left variable starts at 0 and increases by faceImWidth(230) ❷. The inner for loop’s top variable start at 0 and increases by faceImHeight(215) ❸. These nested for loops produce values for left and top to paste a grid of faceIm images over the catCopyTwo Image object, as in Figure 17-6. To see our nested loops working, we print left and top. After the pasting is complete, we save the modified catCopyTwo to tiled.png.

<!-- ![image](assets/000049.jpg)
 -->
Figure 17-6. Nested for loops used with paste() to duplicate the cat’s face (a duplicat, if you will).

Pasting Transparent Pixels

Normally transparent pixels are pasted as white pixels. If the image you want to paste has transparent pixels, pass the Image object as the third argument so that a solid rectangle isn’t pasted. This third argument is the “mask” Image object. A mask is an Image object where the alpha value is significant, but the red, green, and blue values are ignored. The mask tells the paste() function which pixels it should copy and which it should leave transparent. Advanced usage of masks is beyond this book, but if you want to paste an image that has transparent pixels, pass the Image object again as the third argument.