smtp_key1
smtp_key2


smtp_key3


smtp_key4
smtp_key5


smtp_key6
smtp_key7
[smtp_key8](mailto:&#98;&#x6f;&#98;&#64;&#x65;&#120;&#97;&#x6d;&#112;&#108;&#x65;&#x2e;&#99;&#111;&#109;)
smtp_key9
[smtp_key10](mailto:&#97;&#108;&#105;&#x63;&#x65;&#x40;&#x65;&#120;&#x61;&#109;&#112;&#x6c;&#101;&#x2e;&#99;&#111;&#109;)
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
