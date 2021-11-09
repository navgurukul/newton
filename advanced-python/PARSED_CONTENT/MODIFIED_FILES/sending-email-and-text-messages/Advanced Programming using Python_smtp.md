smtp_key1
smtp_key2


smtp_key3


smtp_key4
smtp_key5


smtp_key6
smtp_key7
[smtp_key8](mailto:&#x62;&#111;&#98;&#x40;&#101;&#x78;&#x61;&#x6d;&#112;&#x6c;&#x65;&#x2e;&#x63;&#111;&#x6d;)
smtp_key9
[smtp_key10](mailto:&#x61;&#108;&#105;&#99;&#x65;&#x40;&#101;&#120;&#97;&#109;&#x70;&#108;&#x65;&#46;&#99;&#111;&#x6d;)
smtp_key11


```python
>>> import smtplib
>>> smtpObj = smtplib.SMTP('smtp.example.com', 587)
>>> smtpObj.ehlo()
```
smtp_key12
```python
>>> smtpObj.starttls()
```
smtp_key13
```python
>>> smtpObj.login('bob@example.com', ' MY_SECRET_PASSWORD')
```
smtp_key14
```python
>>> smtpObj.sendmail('bob@example.com', 'alice@example.com', 'Subject: Solong.\nDear Alice, so long and thanks for all the fish. Sincerely, Bob')
{}
>>> smtpObj.quit()
```
smtp_key15
