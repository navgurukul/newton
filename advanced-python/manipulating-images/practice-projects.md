```ngMeta
name: practice-projects
completionMethod: manual
```
# Practice Projects
For practice, write programs that do the following.

Extending and Fixing the Chapter Project Programs
The resizeAndAddLogo.py program in this chapter works with PNG and JPEG files, but Pillow supports many more formats than just these two. Extend resizeAndAddLogo.py to process GIF and BMP images as well.

Another small issue is that the program modifies PNG and JPEG files only if their file extensions are set in lowercase. For example, it will process zophie.png but not zophie.PNG. Change the code so that the file extension check is case insensitive.

<!-- ![image](assets/000080.jpg)
 -->
Figure 17-16. When the image isn’t much larger than the logo, the results look ugly.

Finally, the logo added to the bottom-right corner is meant to be just a small mark, but if the image is about the same size as the logo itself, the result will look like Figure 17-16. Modify resizeAndAddLogo.py so that the image must be at least twice the width and height of the logo image before the logo is pasted. Other wise, it should skip adding the logo.
