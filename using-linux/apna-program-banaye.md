## Apna Program Banana Seekhte hai

Ek bahut simple si file banao:

```bash
touch meraprogram
```

Ab iss file ko apni pasand ke editor se khol kar, kuch content daalte hai
```bash
echo "Yeh mera program hai"
echo "Jab mai ismei code add karunga, toh mera program bada ho jayega"
```

Ab aap iss program ko execute karne ki permissions de

```bash
chmod +x meraprogram
```

Ab iss program ko aap, `/usr/bin` directory mei move kar de. Yaha move karne se, yeh program kahi se bhi aap execute kar payenge.

```bash
mv meraprogram /usr/bin/
```

Ab aap apne program ko execute kar sakte ho
```bash
meraprogram
cd ~/Desktop
meraprogram
cd / 
meraprogram
```

Aap apna program kahi se bhi execute kar paoge.