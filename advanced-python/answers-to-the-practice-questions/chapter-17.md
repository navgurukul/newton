```ngMeta
name: chapter-17
completionMethod: manual
```
# Chapter 17
An RGBA value is a tuple of 4 integers, each ranging from 0 to 255. The four integers correspond to the amount of red, green, blue, and alpha (transparency) in the color.

A function call to ImageColor.getcolor('CornflowerBlue', 'RGBA') will return (100, 149, 237, 255), the RGBA value for that color.

A box tuple is a tuple value of four integers: the left edge x-coordinate, the top edge y-coordinate, the width, and the height, respectively.

Image.open('zophie.png')

imageObj.size is a tuple of two integers, the width and the height.

imageObj.crop((0, 50, 50, 50)). Notice that you are passing a box tuple to crop(), not four separate integer arguments.

Call the imageObj.save('new_filename.png') method of the Image object.

The ImageDraw module contains code to draw on images.

ImageDraw objects have shape-drawing methods such as point(), line(), or rectangle(). They are returned by passing the Image object to the ImageDraw.Draw() function.