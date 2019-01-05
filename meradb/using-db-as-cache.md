## Understanding Cache

[Cache](https://kids.kiddle.co/Cache) ke baarein mei Internet par
padh sakte hai. Jo problem humne peechli assignment mei face ki thi,
woh cache se hum solve kar sakte hai. Simple words mei,

Jab hum API call karenge,
toh uss API ka result hum, uss API url ke against store kar lenge.

Yaani,
API request ke liye jo URL tha, usko `key` bana kar
Jo values hai, usko uss `key` ki `value` ki tarah store kar denge

Jab bhi koi API hit karenge, toh hum dekhenge, ki hamare paas
Uss `URL` (`key`) ke liye `value` hai ya nahi

Agar hai, toh hum apne database se value return kar denge

Agar nahi hai, toh hum API request kar kar, uss value ko, 
apne database mei store kar denge, jisse ki koi agar dobara
uss API ko call karta hai, toh usse woh value mil jaye.

Jo code peechli exercise mei tha, usko modify kar kar, yeh
solution implement karein.
