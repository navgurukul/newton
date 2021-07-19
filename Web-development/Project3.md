```ngMeta
name: Get HTML elements
```

Understand about prompt below :

You already know about readline-sync that is useful for taking an input, but in browsers we have one default function named prompt which will give an popup whenever it is called to take input.

```javascript
var yourName= prompt("Please enter your name");
```

You can read more about the prompt here. [how to use promt](https://www.w3schools.com/jsref/met_win_prompt.asp)

Write a programme in Javascript like a web crawler, you have to take input from the user, who is interested in finding the links based on that particular substring. you have to fetch all the links which contain the user given substring as a text in all links.

    - Take the Substring by using prompt
    - Get the document first
    - Collect all links from document
    - From all links find all the links whose text is equal to Substring that user entered in prompt

Website: www.navgurukul.org

Substring: MERAKI

![links by using substring](https://lh6.googleusercontent.com/8j7X_fFROpVQo5zZ9IH2Vnqi1lmC3hffi5cyf4WYVdZ8ORIqJ_3Dfui4_syghC5k1O8nMBSZvsOJbMWqymzpiywkNxxX3KhEVIZihOr7v3gwCkQYWmi2Q2UOy3lcR8MozeK0dift)

How to add Script file in html

[Understand the script tag](https://www.w3schools.com/tags/att_script_src.asp)

A Small Exercise

See the [video](https://drive.google.com/file/d/1pc4Q-8BxoBZg4blNdMiRoAGNY7Qr6K27/view?usp=sharing) to get to know about the project.

[https://github.com/vknayak/JS-projects/tree/main/A%20small%20exercise](https://github.com/vknayak/JS-projects/tree/main/A%20small%20exercise)

This is the html page of a small web page. What you need to do is write a script to get the h1 tag content or text that is there.

And the script file is attached with html in script tag with src attribute.

**Script.js**

// Get the value of h1 tag that is there in given webpage by using dom 
method: getElementById store it in a variable and console it
 
// write the code from below line….

**Finding HTML Elements**

You can manipulate html Elements by using Javascript, you have so many type to do that but the basic one we will discuss now.

Think that you need to call someone how you call him, 
    - By his name if you know like hey kumar.
    - By what colour of dress he is wearing like hey red colour shirt

Or in some other ways right.

Like the same we will call our html elements by their id and class names and css selectors etc.,

Lets See a small example on how to get elements by Id.

Js you can add by writing your code in a separate file right now I am writing the JS code inside html only.

```
<!DOCTYPE html>

<html>
<body>

<h2>JavaScript HTML DOM</h2>

<p id="intro">Finding HTML Elements by Id</p>
<p>This example demonstrates the <b>getElementsById</b> method.</p>

<p id="demo"></p>

<script>
const element = document.getElementById("intro");

document.getElementById("demo").innerHTML = "new data";

</script>

</body>
</html>

```

Here, in the above HTML page you have p element which has the content Finding HTML Elements by Id and id of that element id intro.

If you want to get the p tag by its id. You will use document, why document because we all know document is the owner of all elements everything will come inside that. So, in the document we need to use, getElementById like 

document.getElementById("intro");

And in the parenthesis we will write the id of the particular element that we are going to get.

And you can store it in a variable if you are feeling you can use it in future.

Not only getting elements you can write the data into the HTML by using innerHTML.

If you see we have 1 empty p tag with id demo, if you want to write anything get that first and use innerHTML and update value by assignment operator.

```javascript
document.getElementById("demo").innerHTML = "new data";
```

You can get more [here](https://www.w3schools.com/js/js_htmldom_elements.asp)
please go through  this link.






