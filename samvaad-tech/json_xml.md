```ngMeta
name: Json and Xml
```


# JSON
 
Json ek aasaan text-based open source data-interchange ka format hai . yah pooree tarah se independent language hai aur is ka jyadatar hisaa modern programming languages ke saath use kiya ja sakata hai .
 
json javascript object notation par sthir hai . json object server aur client ke beech data ko transfer karane ke lie upayog kiya jaata hai .
json xml par kaee phaayade hain haalaanki xml ek hee purpose ke lie work karata hai .
json file ko .json extension se banaya jaata hai . json ka internet media type "application/json" hai .
json array,object, string, number aur values ko supports karata hai

@[youtube](bMqevPKAPD4)


## JSON Example
aapako is example se maloom hoga ki apane topic aur edition ke aadhaar par books se sambandhit jaanakaaree store karane ke lie json ka upayog kaise karate hai.
```
{
   "book": [
	
    {
         "id":"01",
         "language": "Java",
         "edition": "First",
         "author": "‎James Gosling"
      },
	
      {
         "id":"07",
         "language": "C++",
         "edition": "second",
         "author": "E.Balagurusamy"
      }
   ]
}
```
uparokt example dekhane ke baad aap neeche ek aur example dekh sakate hai jisko json.htm ke roop mein save kiya gaya hai .
```
<html>
   <head>
      <title>JSON Example</title>
		
      <script language = "javascript" >
  
         var object1 = { "language" : "Java", "author"  : "James Gosling" };
         document.write("<h1>JSON with JavaScript example</h1>");
         document.write("<br>");
         document.write("<h3>Language = " + object1.language+"</h3>");  
         document.write("<h3>Author = " + object1.author+"</h3>");   

         var object2 = { "language" : "C++", "author"  : "E-Balagurusamy" };
         document.write("<br>");
         document.write("<h3>Language = " + object2.language+"</h3>");  
         document.write("<h3>Author = " + object2.author+"</h3>");   
  
         document.write("<hr />");
         document.write(object2.language + " programing language will be studied " 
            + "from book written by " + object2.author);
         document.write("<hr />")  
      </script>
		
   </head>
	
   <body>
   </body>
	
</html>
```


# XML

xml ka upayog vyaapak roop se data-interchange pattarn ke roop mein bhi kiya jaata hai. isalie ham un donon ke beech compare karane kee koshish karenge .

hamaara compare karane ka purpose yah nahin hai ki kaun nishchit roop se us line mein nahin hai balki ham yah samajhane kee koshish karenge ki kaun sa specefic data store karane ke lie upyukt hai .

1. xml json ke compare mein bahut adhik complex hai .
2. xml ke lie schhaim(metadata) ko discribe karane ke lie kai characteristics hain.
3. xml mein xml data se query karane ke lie Xquery specify hai.lekin json maano JAQL, JSONiq aadi shaamil hote hai lekin ye general roop se upayog nahin hote hai.
4. xml mein XSLT ko specification kiya gaya hai.jo kisee bhee xml document mein ek style ko laagoo karane ke lie upayog kiya ja sakata hai. haalaanki json mein kuchh nahin hai.

# Do log ko mil kar sabse pehle yeh videos dekhni hai


@[youtube](F7a_6r575RQ)

## JSON Example
```
{"employees":[  
    {"name":"Alia", "email":"alia050@gmail.com"},  
    {"name":"Kareena", "email":"kareenal12@gmail.com"},  
    {"name":"Salman", "email":"salman0202@gmail.com"}  
]}  
```
## XML Example
```
<employees>  
    <employee>  
        <name>Alia</name>   
        <email>alia050@gmail.com</email>  
    </employee>  
    <employee>  
        <name>Kareena</name>   
        <email>kareenal12@gmail.com</email>  
    </employee>  
    <employee>  
        <name>Salman</name>   
        <email>salman0202@gmail.com</email>  
    </employee>  
</employees>
```
# Ab aapko 30 mins ke liye aapas mei english mei inn topics ke baarein mei baat karni hai.
Baat karte karte, aap observe karein, ki aap kitne tech words use kar paa rahe hai.
Aur agar aapka partner koi aisa tech word bolta hai, jo aapko nahi pata, ya aap generally use nahi kartein. Inn words ko bhi samajhne ki phir koshish karein.

# Iss discussion ko karte hue, aap inn points ke baarein mei bhi soch sakte hai:
1. What is Json?
2. What is XML?
3. Json aur XML mai antar kya hain?
4. Xml Html se kaise alag hain?
5. XML ke benifits kya hain?
