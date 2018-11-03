```ngMeta
name: identifying-photo-folders-on-the-hard-drive
completionMethod: manual
```
# Identifying Photo Folders on the Hard Drive
I have a bad habit of transferring files from my digital camera to temporary folders somewhere on the hard drive and then forgetting about these folders. It would be nice to write a program that could scan the entire hard drive and find these leftover “photo folders.”

Write a program that goes through every folder on your hard drive and finds potential photo folders. Of course, first you’ll have to define what you consider a “photo folder” to be; let’s say that it’s any folder where more than half of the files are photos. And how do you define what files are photos?

First, a photo file must have the file extension .png or .jpg. Also, photos are large images; a photo file’s width and height must both be larger than 500 pixels. This is a safe bet, since most digital camera photos are several thousand pixels in width and height.

As a hint, here’s a rough skeleton of what this program might look like:


#! python3 #
Import modules and write comments to describe this program.

for foldername, subfolders, filenames in os.walk('C:\\'):
    numPhotoFiles = 0
    numNonPhotoFiles = 0
    for filename in filenames:
        # Check if file extension isn't .png or .jpg.
        if TODO:
            numNonPhotoFiles += 1
            continue    # skip to next filename

        # Open image file using Pillow.

        # Check if width & height are larger than 500.
        if TODO:
            # Image is large enough to be considered a photo.
            numPhotoFiles += 1
        else:
            # Image is too small to be a photo.
            numNonPhotoFiles += 1

    # If more than half of files were photos,
    # print the absolute path of the folder.
    if TODO:
        print(TODO)
When the program runs, it should print the absolute path of any photo folders to the screen.

# Custom Seating Cards
Chapter 13 included a practice project to create custom invitations from a list of guests in a plaintext file. As an additional project, use the pillow module to create images for custom seating cards for your guests. For each of the guests listed in the guests.txt file from the resources at <span><a href="http://nostarch.com/automatestuff/">http://nostarch.com/automatestuff/</a></span>, generate an image file with the guest name and some flowery decoration. A public domain flower image is available in the resources at <span><a href=" http://nostarch.com/automatestuff/"> http://nostarch.com/automatestuff/</a></span>.

To ensure that each seating card is the same size, add a black rectangle on the edges of the invitation image so that when the image is printed out, there will be a guideline for cutting. The PNG files that Pillow produces are set to 72 pixels per inch, so a 4×5-inch card would require a 288×360-pixel image.

