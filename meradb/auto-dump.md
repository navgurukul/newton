## Auto Dumping
Humein `load` function ko aise modify karna hai, ki agar second argument `True` ho toh - file mei auto dumping enable ho jaye.

Iska matlab hai ki, jaise hi koi bhi value `set` ki jaye, toh woh database mei `reflect` ho jaye.

Sochiye, agar aap aisa nahi karenge toh kya hoga.
To hum jo bhi `set` operations karenge, jab tak database mei `dump` nahi karenge, tab tak hamari file mei write nahi honge.

Par `auto dumping` enable karne se, hamara code har `set` operation ke baad automatically update kar dega. Par yeh update sirf tab hi karega jab `load` ko `True` as an argument milega. Agar usse ya toh

- koi second argument nahi milega
- ya `False` argument milega

toh code pehle ki tarah hi chalega. Yaani agar `dump` function call nahi kiya hoga, toh database mei koi change nahi hoga.