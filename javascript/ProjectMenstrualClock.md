```ngMeta
name: Project Menstrual Clock
```

Watch the short film here:
@[youtube](H-BrSO47IXw)

You can learn more about periods [here](https://www.girlshealth.gov/body/period/) and [here](https://www.medicinenet.com/menstruation/article.htm)


# Project Menstrual Clock v 1

1. Ek HTML/CSS page banao jo date and a clock display kare. Date and Clock [iss](https://codepen.io/josephshambrook/full/xmtco) tarah ke placeholder mein design karke dalein. Try karein ki aap code na dekhe.
   *transform* and *transform-origin* css style properties use karke aap clock ke hands ko kahi bhi position kar sakte hain.
   Sochiye ki css ki kaun si properties use karke aap clock ke hands ko kahi bhi position kar sakte hain. (Hint: try "transform" and "transform-origin")

2. JavaScript mein, present date using [Date](https://www.w3schools.com/js/js_dates.asp) nikale. Us date object se day, month and year alag alag nikale using the pre-defined date [methods](https://www.w3schools.com/js/js_date_methods.asp). Usko alag variables mein store karein.
 
Apne html page ke date placeholder ko modify karein taaki ab wo current date dikhaye.   Aapko iske liye DOM mei changes karne padenge. Aap kisi bhi method jaise kisi object ki innerHTML change, queryselector(), etc. use kar kar change kar sakte ho.

3. Usi tarah javascript mein ek function likhe jo hour, minute and seconds ko Date Object se extract kare. Hour, minute and second hands ki position change karein to reflect the current time. Aapko hour, minute and second ko degrees mein convert karna padega. Aapko fir "transform" style property change karke hands ko sahi position karna padega.

4. Aapko clock ko regularly update karne honga - har ek second pe. Upar ke function ko har second update karne ke liye setInterval() function ka use kijiye. Aap css ke "transition" property use karke clock hands ko smoothly move kar sakte hain.

5. Apne web browser mein aap apne last period date ko permanently store kar sakte hain using [localStorage](https://www.w3schools.com/html/html5_webstorage.asp).

Isi tarah apna period cycle bhi store karein. Aapka period cycle 28-35 days ke beech mein vary kar sakta hai.

6. Javascript mein Current date se period date ka difference check kijiye. Agar yeh difference hai, aur maan lo 28 days ki period cycle hai, toh yeh nikaliye ki kitne din bachche hai next period mei. Clearly, yeh din 28 se kam honge. Sochiye iske liye aap ko kaunsa function use karna hoga.

Agar result 0 ya uske aas paas hai, iska matlab period ki date aa gayi hai.

7. Period date ke approach hone pe aap kisi tarah ka indicator de sakte hain - jaise change in background ya snowfall ya aur kuch. Aap khud sochiye ki aapko apne liye kis tarah ka indicator chahiye. Apne project mein us indicator ko add kijiye.

8. Apne project mein aur kisi tarah ke changes karna chahenge jisse aapka Menstrual clock aur behter ho. Iske baare mein sochiye aur extra features ki list banaiye. 
Iske liye aap

- Periods ke baarein mei aur research kar kar samajh sakte hai ki kaise features useful ho sakte hai
- Period tracker naam se apps dhoondh sakte hai playstore par, aur unn apps se inspire ho kar soch sakte hai ki aap kya changes karna chahte hai
   
Look at [this](http://www.periodgame.com/#intro) period game that aims to educate people about periods. Can you think of a similar game in javascript?
