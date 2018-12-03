## Using .bashrc file

`.bashrc` naam se ek file aapki `home directory` mei hogi. Jab bhi aap terminal ka naya session kholte ho, toh woh file `execute` ho jaati hai.

Aap uss file ko apne kisi bhi pasand ke editor mei khol kar, yeh content paste karein.

```bash
echo "I am learning programming"
```

Ab aap file ko save kar kar, close kar sakte hai.

Ab aap ek naya terminal ka window khol kar dekhein.

Agar aapne galti nahi ki hogi, toh aapko apne terminal mei "I am learning programming" dikhega.

Dhyaan rakhein kyuki file tab execute hoti hai - jab naya terminal khulta hai toh, isliye, purane terminal mei koi change nahi dikhayi dega.

`.bashrc` file mei aap koi aur bhi program call kar sakte hai. Jaise, yeh contents `.bashrc` file mei daalein:

```bash
echo "Aap 5 seconds ke liye, ek lambi saans le kar, relax mehsoos karein"
echo "5 Seconds"
sleep 1
echo "4 Seconds"
sleep 1
echo "3 Seconds"
sleep 1
echo "2 Seconds"
sleep 1
echo "1 Seconds"
sleep 1
echo "Now, you can continue your work!"
```