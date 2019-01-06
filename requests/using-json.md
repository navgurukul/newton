## Using JSON

Jo code humne likha tha, requests library kar kar, courses download karne ke liye, uss code mei yeh changes karo.

### Abhi tak woh code kya karta hai?
`requests` module use kar kar, courses ka `API Endpoint` ya `URL` call kar kar, data `courses.json` file mei store karta hai.

### Ab aapko kya karna hai?

    - `courses.json` file padh kar
    - aapko iss object ko ek json argument mei load karna hai
    - uss json object ko parse kar kar
    - aapko saare courses ki list print karni hai

Yeh karne se pehle aap ek chota sa change karo, ki

    agar `courses.json` pehle se exist karti hai, toh aap
    dobara API call mat karo. isse aap debugging fast kar
    paoge.

isse aap fast debugging kar paoge, nahi toh baar baar
aapko API call khatam hone ka wait karna padega.