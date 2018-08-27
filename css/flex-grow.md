```ngMeta
name: flex-grow : Item Property
completionMethod: manual
```

# flex-grow: Item Property

## Usage: **flex-grow: \<number>**

 - Yeh property batati hai ki kiss hisab se container ke andar ki jagah items mein batengi.

 - By default yaani ki pehle se iski value **0** hoti hai.

 - Jaise, agar container ki width **1200px** hai. Aur uss container ke andar 4 items hai. Agar aap inn 4 items ko **width** nhi dete aur inka **flex-grow:1** set kar dete ho to her item **300px** jagah legi. Iska matlab 1200 px 4 items mein bat jayega. Iss [example](http://codepen.io/navgurukul/pen/ZLgppd) ko dekho aur samjho.

 - Magar agar hum kisi item ko pehle se width de dete hai. Jaise iss [example](http://codepen.io/navgurukul/pen/egqdPp) **item3** ki width **200px** hai aur baaki sab item ki **0**. Tab pehle item3 **200px** width lega. Uske baad **1000px(1200-200)** 4 items mein distribute hoga. Yaani ki her item ko **250 px(1000/4)** width milegi. Aur item3 ko **450px(250+200)** width milegi. 

 - Socho aapke container mein 3 items hai. Aur aap chahte hai ki pehli item ki width dusri aur teesri item ke mukable double ho. Tab aap pehli item ka flex-grow:2 set karoge aur baaki items ka flex-grow:1. Iss [example](http://codepen.io/navgurukul/pen/qReqZp) ko dekho aur samjho.

- Ab aap yeh [assignment](http://codepen.io/navgurukul/full/KaLWvw/) karne ke liye ready ho ;)


