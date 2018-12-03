Aap `python` ka use kar kar bhi ek executable program bana sakte ho. Uske liye, aapko

```bash
#!/usr/bin/python
```

line ko apni file mei sabse pehli line mei daalna hoga.

Ek example ke through dekhte hai.

```bash
touch merapythonprogram
```

Ab iss file ko apni pasand ke editor se khol kar, kuch content daalte hai

```python
#!/usr/bin/python
print "Yeh mera PYTHON program hai"
print "Jab mai ismei PYTHON KA code add karunga, toh mera program ANACONDA ban jayega"
```

Ab aap iss program ko execute karne ki permissions de

```bash
chmod +x merapythonprogram
```

Ab iss program ko aap, `/usr/bin` directory mei move kar de. Yaha move karne se, yeh program kahi se bhi aap execute kar payenge.

```bash
mv merapythonprogram /usr/bin/
```

Ab aap apne program ko execute kar sakte ho
```bash
merapythonprogram
cd ~/Desktop
merapythonprogram
cd / 
merapythonprogram
```

Aap apna program kahi se bhi execute kar paoge.