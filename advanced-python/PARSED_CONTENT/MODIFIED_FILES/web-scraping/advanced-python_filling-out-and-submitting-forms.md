```ngMeta
filling-out-and-submitting-forms_key1
```
# filling-out-and-submitting-forms_key2
filling-out-and-submitting-forms_key3filling-out-and-submitting-forms_key4filling-out-and-submitting-forms_key5

```python
>>> from selenium import webdriver
>>> browser = webdriver.Firefox()
>>> browser.get('https://mail.yahoo.com')
>>> emailElem = browser.find_element_by_id('login-username')
>>> emailElem.send_keys('not_my_real_email')
>>> passwordElem = browser.find_element_by_id('login-passwd')
>>> passwordElem.send_keys('12345')
>>> passwordElem.submit()
```
filling-out-and-submitting-forms_key6

# filling-out-and-submitting-forms_key7
filling-out-and-submitting-forms_key8

filling-out-and-submitting-forms_key9

filling-out-and-submitting-forms_key10

filling-out-and-submitting-forms_key11

filling-out-and-submitting-forms_key12

filling-out-and-submitting-forms_key13

filling-out-and-submitting-forms_key14

filling-out-and-submitting-forms_key15

filling-out-and-submitting-forms_key16

filling-out-and-submitting-forms_key17

```python
>>> from selenium import webdriver
>>> from selenium.webdriver.common.keys import Keys
>>> browser = webdriver.Firefox()
>>> browser.get('http://nostarch.com')
>>> htmlElem = browser.find_element_by_tag_name('html')
>>> htmlElem.send_keys(Keys.END)     # scrolls to bottom
>>> htmlElem.send_keys(Keys.HOME)    # scrolls to top
```
filling-out-and-submitting-forms_key18filling-out-and-submitting-forms_key19filling-out-and-submitting-forms_key20filling-out-and-submitting-forms_key21

