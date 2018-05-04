# Project Menstrual Clock

1. Ek HTML/CSS page banao jo date and a clock display kare. Date placeholder iss format DD - MM - YY mein hona chahiye.
   
   Clock [iss](https://fr.123rf.com/photo_87564976_ic%C3%B4ne-de-l-horloge-vector-illustration-design-plat-facile-%C3%A0-utiliser-et-%C3%A9diter-eps10-fond-jaune-avec-une.html)
   *transform* and *transform-origin* css style properties use karke aap clock ke hands ko kahi bhi position kar sakte hain.

2. JavaScript mein, present date using [Date](https://www.w3schools.com/js/js_dates.asp) nikale. Us date object se day, month and year alag alag nikale using the pre-defined date [methods](https://www.w3schools.com/js/js_date_methods.asp). Usko alag variables mein store karein.
Apne html page ke date placeholder ko modify karein taaki ab wo current date dikhaye.  Aapko iske liye .queryselector() use karna pad sakta hai to select the text you are changing.

3. Usi tarah javascript mein ek function likhe to extract hour, minute and seconds from the Date. hour, minute and second hands ki position change karein to reflect the current time. Aapko hour, minute and second ko degrees mein convert karna padega. Aapko fir "transform" style property change karke hands ko sahi position karna padega.
4. Aapko clock ko regularly update karne honga - har ek second pe. Upar ke function ko har second update karne ke liye setInterval() function ka use kijiye. Aap css ke "transition" property use karke clock hands ko smoothly move kar sakte hain.
5. Apne web browser mein aap apne period date ko permanently store kar sakte hain using [localStorage](https://www.w3schools.com/html/html5_webstorage.asp)
6. Current date se period date ka difference check kijiye. Agar wo difference agar aapke period cycle (28-30) ke beech mein hai, toh snowfall kijiye.  
   
