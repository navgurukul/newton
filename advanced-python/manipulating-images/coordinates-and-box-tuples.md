```ngMeta
name: coordinates-and-box-tuples
```
# Coordinates and Box Tuples
Image pixels are addressed with x- and y-coordinates, which respectively specify a pixel’s horizontal and vertical location in an image. The origin is the pixel at the top-left corner of the image and is specified with the notation (0, 0). The first zero represents the x-coordinate, which starts at zero at the origin and increases going from left to right. The second zero represents the y-coordinate, which starts at zero at the origin and increases going down the image. This bears repeating: y-coordinates increase going downward, which is the opposite of how you may remember y-coordinates being used in math class. Figure 17-1 demonstrates how this coordinate system works.

Many of Pillow’s functions and methods take a box tuple argument. This means Pillow is expecting a tuple of four integer coordinates that represent a rectangular region in an image. The four integers are, in order, as follows:

<!-- ![image](assets/000004.jpg)
 -->
Figure 17-1. The x- and y-coordinates of a 27×26 image of some sort of ancient data storage device

Left: The x-coordinate of the leftmost edge of the box.

Top: The y-coordinate of the top edge of the box.

Right: The x-coordinate of one pixel to the right of the rightmost edge of the box. This integer must be greater than the left integer.

Bottom: The y-coordinate of one pixel lower than the bottom edge of the box. This integer must be greater than the top integer.

<!-- ![image](assets/000096.jpg)
 -->
Figure 17-2. The area represented by the box tuple (3, 1, 9, 6)

Note that the box includes the left and top coordinates and goes up to but does not include the right and bottom coordinates. For example, the box tuple (3, 1, 9, 6) represents all the pixels in the black box in Figure 17-2.