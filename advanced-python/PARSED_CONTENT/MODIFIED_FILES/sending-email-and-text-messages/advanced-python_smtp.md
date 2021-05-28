```ngMeta
smtp_key1
```
# smtp_key2
smtp_key3

smtp_key4

# smtp_key5
smtp_key6

# smtp_key7
smtp_key8[smtp_key9](mailto:&#x62;&#111;&#x62;&#64;&#x65;&#x78;&#97;&#109;&#x70;&#x6c;&#101;&#x2e;&#99;&#x6f;&#109;)
smtp_key10[smtp_key11](mailto:&#x61;&#108;&#105;&#99;&#x65;&#64;&#x65;&#x78;&#97;&#x6d;&#112;&#x6c;&#101;&#x2e;&#x63;&#x6f;&#109;)
smtp_key12

```python
>>> import smtplib
>>> smtpObj = smtplib.SMTP('smtp.example.com', 587)
>>> smtpObj.ehlo()
```
smtp_key13smtp_key14```python
>>> smtpObj.starttls()
```
smtp_key15```python
>>> smtpObj.login('bob@example.com', ' MY_SECRET_PASSWORD')
```
smtp_key16```python
>>> smtpObj.sendmail('bob@example.com', 'alice@example.com', 'Subject: Solong.\nDear Alice, so long and thanks for all the fish. Sincerely, Bob')
{}
>>> smtpObj.quit()
```
smtp_key17