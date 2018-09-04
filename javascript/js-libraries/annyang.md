```ngMeta
name: Annyang.js
completionMethod: manual
```

# Part II  another JS library

- [Link](https://codepen.io/navgurukul/full/GrMyGv/) - Assignment ka link.
- **Annyang.js**, jQuery jaisi ek aur library hai. Isko use kar kar hum apne page mein
	"**voice recognition**" daal sakte hai.
- Sabse pehle hum isko apne page mein include karenge, theek jQuery ki tarah.

-  src=["//cdnjs.cloudflare.com/ajax/libs/annyang/2.6.0/annyang.min.js"](https://cdnjs.cloudflare.com/ajax/libs/	annyang/2.6.0/annyang.min.js)> 

- Iske baad hum check karenge ki annyang aapke page mein include hui ya nahi.
	- **if(annyang)** { 	//code yahan likhenge	}
	- **annyang.addComands**({ "speech_jo_apko_recognise_karani hai": function_ka_naam_jo_call_karan_hai, .}); // 		aap  yahan speech aur function ka naam likhte hai
	- **annyang.start()**; // likhne se yeh library start ho jaati hai.	
	- **annyang.setLanguage**(‘’language_ka_naam");
- Annyang ke baare mein aur padhne ke liye iss [link](https://www.talater.com/annyang/) ka use kare.



