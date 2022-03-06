```ngMeta
name:  colors-and-rgba-values
```
# Colors and RGBA Values
Computer programs often represent a color in an image as an RGBA value. An RGBA value is a group of numbers that specify the amount of red, green, blue, and alpha (or transparency) in a color. Each of these component values is an integer from 0 (none at all) to 255 (the maximum). These RGBA values are assigned to individual pixels; a pixel is the smallest dot of a single color the computer screen can show (as you can imagine, there are millions of pixels on a screen). A pixel’s RGB setting tells it precisely what shade of color it should display. Images also have an alpha value to create RGBA values. If an image is displayed on the screen over a background image or desktop wallpaper, the alpha value determines how much of the background you can “see through” the image’s pixel.

In Pillow, RGBA values are represented by a tuple of four integer values. For example, the color red is represented by (255, 0, 0, 255). This color has the maximum amount of red, no green or blue, and the maximum alpha value, meaning it is fully opaque. Green is represented by (0, 255, 0, 255), and blue is (0, 0, 255, 255). White, the combination of all colors, is (255, 255, 255, 255), while black, which has no color at all, is (0, 0, 0, 255).

If a color has an alpha value of 0, it is invisible, and it doesn’t really matter what the RGB values are. After all, invisible red looks the same as invisible black.

Pillow uses the standard color names that HTML uses. Table 17-1 lists a selection of standard color names and their values.

Table 17-1. Standard Color Names and Their RGBA Values

Name                  RGBA Value                      Name                              RGBA Value

White            (255, 255, 255, 255)                  Red                              (255, 0, 0, 255)

Green 			(0, 128, 0, 255) 					   Blue 							(0, 0, 255, 255)

Gray 			(128, 128, 128, 255)				   yellow 							(255, 255, 0, 255)

Black  			(0, 0, 0, 255)						   Purple							(128, 0, 128, 255)

Pillow offers the ImageColor.getcolor() function so you don’t have to memorize RGBA values for the colors you want to use. This function takes a color name string as its first argument, and the string 'RGBA' as its second argument, and it returns an RGBA tuple.

## CMYK and RGB Coloring

In grade school you learned that mixing red, yellow, and blue paints can form other colors; for example, you can mix blue and yellow to make green paint. This is known as the subtractive color model, and it applies to dyes, inks, and pigments. This is why color printers have CMYK ink cartridges: the Cyan (blue), Magenta (red), Yellow, and blacK ink can be mixed together to form any color.

However, the physics of light uses what’s called an additive color model. When combining light (such as the light given off by your computer screen), red, green, and blue light can be combined to form any other color. This is why RGB values represent color in computer programs.

To see how this function works, enter the following into the interactive shell:

```python
❶ >>> from PIL import ImageColor
❷ >>> ImageColor.getcolor('red', 'RGBA')
   (255, 0, 0, 255)
❸ >>> ImageColor.getcolor('RED', 'RGBA')
   (255, 0, 0, 255)
   >>> ImageColor.getcolor('Black', 'RGBA')
   (0, 0, 0, 255)
   >>> ImageColor.getcolor('chocolate', 'RGBA')
   (210, 105, 30, 255)
   >>> ImageColor.getcolor('CornflowerBlue', 'RGBA')
   (100, 149, 237, 255)
```
First, you need to import the ImageColor module from PIL ❶ (not from Pillow; you’ll see why in a moment). The color name string you pass to ImageColor.getcolor() is case insensitive, so passing 'red' ❷ and passing 'RED' ❸ give you the same RGBA tuple. You can also pass more unusual color names, like 'chocolate' and 'Cornflower Blue'.

Pillow supports a huge number of color names, from 'aliceblue' to 'whitesmoke'. You can find the full list of more than 100 standard color names in the resources at <span><a href=" http://nostarch.com/automatestuff/."> http://nostarch.com/automatestuff/.</a></span>