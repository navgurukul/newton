```ngMeta
smtp_key1
```

smtp_key2
smtp_key3


smtp_key4


smtp_key5
smtp_key6


smtp_key7
smtp_key8


```python
>>> import smtplib
>>> smtpObj = smtplib.SMTP('smtp.example.com', 587)
>>> smtpObj.ehlo()
```
smtp_key9
```python
>>> smtpObj.starttls()
```
smtp_key10
```python
>>> smtpObj.login('bob@example.com', ' MY_SECRET_PASSWORD')
```
smtp_key11
```python
>>> smtpObj.sendmail('bob@example.com', 'alice@example.com', 'Subject: Solong.\nDear Alice, so long and thanks for all the fish. Sincerely, Bob')
{}
>>> smtpObj.quit()
```
smtp_key12
