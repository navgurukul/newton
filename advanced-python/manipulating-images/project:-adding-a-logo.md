```ngMeta
name: project:-adding-a-logo
completionMethod: manual
```
# Project: Adding a Logo
Say you have the boring job of resizing thousands of images and adding a small logo watermark to the corner of each. Doing this with a basic graphics program such as Paintbrush or Paint would take forever. A fancier graphics application such as Photoshop can do batch processing, but that software costs hundreds of dollars. Let’s write a script to do it instead.

Say that Figure 17-11 is the logo you want to add to the bottom-right corner of each image: a black cat icon with a white border, with the rest of the image transparent.

<!-- ![image](assets/000029.jpg)
 -->
Figure 17-11. The logo to be added to the image.

At a high level, here’s what the program should do:

Load the logo image.

Loop over all .png and.jpg files in the working directory.

Check whether the image is wider or taller than 300 pixels.

If so, reduce the width or height (whichever is larger) to 300 pixels and scale down the other dimension proportionally.

Paste the logo image into the corner.

Save the altered images to another folder.

This means the code will need to do the following:

Open the catlogo.png file as an Image object.

Loop over the strings returned from os.listdir('.').

Get the width and height of the image from the size attribute.

Calculate the new width and height of the resized image.

Call the resize() method to resize the image.

Call the paste() method to paste the logo.

Call the save() method to save the changes, using the original filename.

# Step 1: Open the Logo Image
For this project, open a new file editor window, enter the following code, and save it as resizeAndAddLogo.py:


   #! python3
   # resizeAndAddLogo.py - Resizes all images in current working directory to fit
   # in a 300x300 square, and adds catlogo.png to the lower-right corner.
   import os
   from PIL import Image

❶ SQUARE_FIT_SIZE = 300
❷ LOGO_FILENAME = 'catlogo.png'

❸ logoIm = Image.open(LOGO_FILENAME)
❹ logoWidth, logoHeight = logoIm.size

   # TODO: Loop over all files in the working directory.

   # TODO: Check if image needs to be resized.

   # TODO: Calculate the new width and height to resize to.

   # TODO: Resize the image.

   # TODO: Add the logo.

   # TODO: Save changes.
By setting up the SQUARE_FIT_SIZE ❶ and LOGO_FILENAME ❷ constants at the start of the program, we’ve made it easy to change the program later. Say the logo that you’re adding isn’t the cat icon, or say you’re reducing the output images’ largest dimension to something other than 300 pixels. With these constants at the start of the program, you can just open the code, change those values once, and you’re done. (Or you can make it so that the values for these constants are taken from the command line arguments.) Without these constants, you’d instead have to search the code for all instances of 300 and 'catlogo.png' and replace them with the values for your new project. In short, using constants makes your program more generalized.

The logo Image object is returned from Image.open() ❸. For readability, logoWidth and logoHeight are assigned to the values from logoIm.size ❹.

The rest of the program is a skeleton of TODO comments for now.

# Step 2: Loop Over All Files and Open Images
Now you need to find every .png file and .jpg file in the current working directory. Note that you don’t want to add the logo image to the logo image itself, so the program should skip any image with a filename that’s the same as LOGO_FILENAME. Add the following to your code:


   #! python3
   # resizeAndAddLogo.py - Resizes all images in current working directory to fit
   # in a 300x300 square, and adds catlogo.png to the lower-right corner.

   import os
   from PIL import Image

   --snip--

   os.makedirs('withLogo', exist_ok=True)
```python
   # Loop over all files in the working directory.
❶ for filename in os.listdir('.'):
❷     if not (filename.endswith('.png') or filename.endswith('.jpg')) \
          or filename == LOGO_FILENAME:
❸         continue # skip non-image files and the logo file itself

❹     im = Image.open(filename)
       width, height = im.size
```
   --snip--
First, the os.makedirs() call creates a withLogo folder to store the finished images with logos, instead of overwriting the original image files. The exist_ok=True keyword argument will keep os.makedirs() from raising an exception if withLogo already exists. While looping through all the files in the working directory with os.listdir('.') ❶, the long if statement ❷ checks whether each filename doesn’t end with .png or .jpg. If so—or if the file is the logo image itself—then the loop should skip it and use continue ❸ to go to the next file. If filename does end with '.png' or '.jpg' (and isn’t the logo file), you can open it as an Image object ❹ and set width and height.

# Step 3: Resize the Images
The program should resize the image only if the width or height is larger than SQUARE_FIT_SIZE (300 pixels, in this case), so put all of the resizing code inside an if statement that checks the width and height variables. Add the following code to your program:


   #! python3
   # resizeAndAddLogo.py - Resizes all images in current working directory to fit
   # in a 300x300 square, and adds catlogo.png to the lower-right corner.

   import os
   from PIL import Image

   --snip--
```python
      # Check if image needs to be resized.
      if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
          # Calculate the new width and height to resize to.
          if width > height:
❶            height = int((SQUARE_FIT_SIZE / width) * height)
              width = SQUARE_FIT_SIZE
          else:
❷            width = int((SQUARE_FIT_SIZE / height) * width)
              height = SQUARE_FIT_SIZE

          # Resize the image.
          print('Resizing %s...' % (filename))
     ❸     im = im.resize((width, height))
```
--snip--
If the image does need to be resized, you need to find out whether it is a wide or tall image. If width is greater than height, then the height should be reduced by the same proportion that the width would be reduced ❶. This proportion is the SQUARE_FIT_SIZE value divided by the current width. The new height value is this proportion multiplied by the current height value. Since the division operator returns a float value and resize() requires the dimensions to be integers, remember to convert the result to an integer with the int() function. Finally, the new width value will simply be set to SQUARE_FIT_SIZE.

If the height is greater than or equal to the width (both cases are handled in the else clause), then the same calculation is done, except with the height and width variables swapped ❷.

Once width and height contain the new image dimensions, pass them to the resize() method and store the returned Image object in im ❸.

# Step 4: Add the Logo and Save the Changes
Whether or not the image was resized, the logo should still be pasted to the bottom-right corner. Where exactly the logo should be pasted depends on both the size of the image and the size of the logo. Figure 17-12 shows how to calculate the pasting position. The left coordinate for where to paste the logo will be the image width minus the logo width; the top coordinate for where to paste the logo will be the image height minus the logo height.

<!-- ![image](assets/000061.jpg)
 -->
Figure 17-12. The left and top coordinates for placing the logo in the bottom-right corner should be the image width/height minus the logo width/height.

After your code pastes the logo into the image, it should save the modified Image object. Add the following to your program:


   #! python3
   # resizeAndAddLogo.py - Resizes all images in current working directory to fit
   # in a 300x300 square, and adds catlogo.png to the lower-right corner.

   import os
   from PIL import Image

--snip--

    # Check if image needs to be resized.
    --snip--
```python
    # Add the logo.
❶  print('Adding logo to %s...' % (filename))
❷  im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)

    # Save changes.
❸  im.save(os.path.join('withLogo', filename))
```
The new code prints a message telling the user that the logo is being added ❶, pastes logoIm onto im at the calculated coordinates ❷, and saves the changes to a filename in the withLogo directory ❸. When you run this program with the zophie.png file as the only image in the working directory, the output will look like this:


Resizing zophie.png...
Adding logo to zophie.png...
The image zophie.png will be changed to a 225×300-pixel image that looks like Figure 17-13. Remember that the paste() method will not paste the transparency pixels if you do not pass the logoIm for the third argument as well. This program can automatically resize and “logo-ify” hundreds of images in just a couple minutes.

<!-- ![assets](assets/000066.jpg)
 -->
# Ideas for Similar Programs
Being able to composite images or modify image sizes in a batch can be useful in many applications. You could write similar programs to do the following:

Add text or a website URL to images.

Add timestamps to images.

Copy or move images into different folders based on their sizes.

Add a mostly transparent watermark to an image to prevent others from copying it.

