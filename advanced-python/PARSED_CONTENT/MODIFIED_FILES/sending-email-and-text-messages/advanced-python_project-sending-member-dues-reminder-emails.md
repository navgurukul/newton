```ngMeta
project-sending-member-dues-reminder-emails_key1
```
# project-sending-member-dues-reminder-emails_key2
project-sending-member-dues-reminder-emails_key3

project-sending-member-dues-reminder-emails_key4

project-sending-member-dues-reminder-emails_key5

project-sending-member-dues-reminder-emails_key6

project-sending-member-dues-reminder-emails_key7

project-sending-member-dues-reminder-emails_key8

project-sending-member-dues-reminder-emails_key9

project-sending-member-dues-reminder-emails_key10

project-sending-member-dues-reminder-emails_key11

project-sending-member-dues-reminder-emails_key12

project-sending-member-dues-reminder-emails_key13

project-sending-member-dues-reminder-emails_key14project-sending-member-dues-reminder-emails_key15project-sending-member-dues-reminder-emails_key16

project-sending-member-dues-reminder-emails_key17

project-sending-member-dues-reminder-emails_key18

project-sending-member-dues-reminder-emails_key19


project-sending-member-dues-reminder-emails_key20 project-sending-member-dues-reminder-emails_key21
project-sending-member-dues-reminder-emails_key22

 project-sending-member-dues-reminder-emails_key23
project-sending-member-dues-reminder-emails_key24

project-sending-member-dues-reminder-emails_key25

 project-sending-member-dues-reminder-emails_key26
 project-sending-member-dues-reminder-emails_key27
 project-sending-member-dues-reminder-emails_key28
project-sending-member-dues-reminder-emails_key29

# project-sending-member-dues-reminder-emails_key30
project-sending-member-dues-reminder-emails_key31


project-sending-member-dues-reminder-emails_key32 project-sending-member-dues-reminder-emails_key33
project-sending-member-dues-reminder-emails_key34```python
   # Check each member's payment status.
   unpaidMembers = {}
❶ for r in range(2, sheet.get_highest_row() + 1):
❷     payment = sheet.cell(row=r, column=lastCol).value
       if payment != 'paid':
❸         name = sheet.cell(row=r, column=1).value
❹         email = sheet.cell(row=r, column=2).value
❺         unpaidMembers[name] = email
```
project-sending-member-dues-reminder-emails_key35

# project-sending-member-dues-reminder-emails_key36
project-sending-member-dues-reminder-emails_key37


project-sending-member-dues-reminder-emails_key38# project-sending-member-dues-reminder-emails_key39
project-sending-member-dues-reminder-emails_key40```python
# Log in to email account.
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login(' my_email_address@gmail.com ', sys.argv[1])
```
project-sending-member-dues-reminder-emails_key41

project-sending-member-dues-reminder-emails_key42


project-sending-member-dues-reminder-emails_key43 project-sending-member-dues-reminder-emails_key44
project-sending-member-dues-reminder-emails_key45```python
   # Send out reminder emails.
   for name, email in unpaidMembers.items():
❶     body = "Subject: %s dues unpaid.\nDear %s,\nRecords show that you have not
   paid dues for %s. Please make this payment as soon as possible. Thank you!'" %
   (latestMonth, name, latestMonth)
❷     print('Sending email to %s...' % email)
❸     sendmailStatus = smtpObj.sendmail('my_email_address@gmail.com', email, body)

❹     if sendmailStatus != {}:
           print('There was a problem sending email to %s: %s' % (email,
           sendmailStatus))
   smtpObj.quit()
```
project-sending-member-dues-reminder-emails_key46

project-sending-member-dues-reminder-emails_key47

project-sending-member-dues-reminder-emails_key48

project-sending-member-dues-reminder-emails_key49


project-sending-member-dues-reminder-emails_key50project-sending-member-dues-reminder-emails_key51project-sending-member-dues-reminder-emails_key52project-sending-member-dues-reminder-emails_key53project-sending-member-dues-reminder-emails_key54project-sending-member-dues-reminder-emails_key55project-sending-member-dues-reminder-emails_key56

project-sending-member-dues-reminder-emails_key57

