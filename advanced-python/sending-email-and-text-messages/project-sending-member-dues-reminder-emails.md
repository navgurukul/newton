```ngMeta
name: project-sending-member-dues-reminder-emails
```
# Project: Sending Member Dues Reminder Emails
Say you have been “volunteered” to track member dues for the Mandatory Volunteerism Club. This is a truly boring job, involving maintaining a spreadsheet of everyone who has paid each month and emailing reminders to those who haven’t. Instead of going through the spreadsheet yourself and copying and pasting the same email to everyone who is behind on dues, let’s—you guessed it—write a script that does this for you.

At a high level, here’s what your program will do:

Read data from an Excel spreadsheet.

Find all members who have not paid dues for the latest month.

Find their email addresses and send them personalized reminders.

This means your code will need to do the following:

Open and read the cells of an Excel document with the openpyxl module. (See Chapter 12 for working with Excel files.)

Create a dictionary of members who are behind on their dues.

Log in to an SMTP server by calling smtplib.SMTP(), ehlo(), starttls(), and login().

For all members behind on their dues, send a personalized reminder email by calling the sendmail() method.

Open a new file editor window and save it as sendDuesReminders.py.

Step 1: Open the Excel File
Let’s say the Excel spreadsheet you use to track membership dues payments looks like Figure 16-2 and is in a file named duesRecords.xlsx. You can download this file from <span><a href="http://nostarch.com/automatestuff/">http://nostarch.com/automatestuff/</a></span>.

<!-- ![image](assets/000022.jpg)
 -->
Figure 16-2. The spreadsheet for tracking member dues payments

This spreadsheet has every member’s name and email address. Each month has a column tracking members’ payment statuses. The cell for each member is marked with the text paid once they have paid their dues.

The program will have to open duesRecords.xlsx and figure out the column for the latest month by calling the get_highest_column() method. (You can consult Chapter 12 for more information on accessing cells in Excel spreadsheet files with the openpyxl module.) Enter the following code into the file editor window:


   #! python3
   # sendDuesReminders.py - Sends emails based on payment status in spreadsheet.

   import openpyxl, smtplib, sys

   # Open the spreadsheet and get the latest dues status.
❶ wb = openpyxl.load_workbook('duesRecords.xlsx')
❷ sheet = wb.get_sheet_by_name('Sheet1')

❸ lastCol = sheet.get_highest_column()
❹ latestMonth = sheet.cell(row=1, column=lastCol).value

   # TODO: Check each member's payment status.

   # TODO: Log in to email account.

   # TODO: Send out reminder emails.
After importing the openpyxl, smtplib, and sys modules, we open our duesRecords.xlsx file and store the resulting Workbook object in wb ❶. Then we get Sheet 1 and store the resulting Worksheet object in sheet ❷. Now that we have a Worksheet object, we can access rows, columns, and cells. We store the highest column in lastCol ❸, and we then use row number 1 and lastCol to access the cell that should hold the most recent month. We get the value in this cell and store it in latestMonth ❹.

# Step 2: Find All Unpaid Members
Once you’ve determined the column number of the latest month (stored in lastCol), you can loop through all rows after the first row (which has the column headers) to see which members have the text paid in the cell for that month’s dues. If the member hasn’t paid, you can grab the member’s name and email address from columns 1 and 2, respectively. This information will go into the unpaidMembers dictionary, which will track all members who haven’t paid in the most recent month. Add the following code to sendDuesReminder.py.


   #! python3
   # sendDuesReminders.py - Sends emails based on payment status in spreadsheet.

   --snip--
```python
   # Check each member's payment status.
   unpaidMembers = {}
❶ for r in range(2, sheet.get_highest_row() + 1):
❷     payment = sheet.cell(row=r, column=lastCol).value
       if payment != 'paid':
❸         name = sheet.cell(row=r, column=1).value
❹         email = sheet.cell(row=r, column=2).value
❺         unpaidMembers[name] = email
```
This code sets up an empty dictionary unpaidMembers and then loops through all the rows after the first ❶. For each row, the value in the most recent column is stored in payment ❷. If payment is not equal to 'paid', then the value of the first column is stored in name ❸, the value of the second column is stored in email ❹, and name and email are added to unpaidMembers ❺.

# Step 3: Send Customized Email Reminders
Once you have a list of all unpaid members, it’s time to send them email reminders. Add the following code to your program, except with your real email address and provider information:


#! python3
# sendDuesReminders.py - Sends emails based on payment status in spreadsheet.

--snip--
```python
# Log in to email account.
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login(' my_email_address@gmail.com ', sys.argv[1])
```
Create an SMTP object by calling smtplib.SMTP() and passing it the domain name and port for your provider. Call ehlo() and starttls(), and then call login() and pass it your email address and sys.argv[1], which will store your password string. You’ll enter the password as a command line argument each time you run the program, to avoid saving your password in your source code.

Once your program has logged in to your email account, it should go through the unpaidMembers dictionary and send a personalized email to each member’s email address. Add the following to sendDuesReminders.py:


   #! python3
   # sendDuesReminders.py - Sends emails based on payment status in spreadsheet.

   --snip--
```python
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
This code loops through the names and emails in unpaidMembers. For each member who hasn’t paid, we customize a message with the latest month and the member’s name, and store the message in body ❶. We print output saying that we’re sending an email to this member’s email address ❷. Then we call sendmail(), passing it the from address and the customized message ❸. We store the return value in sendmailStatus.

Remember that the sendmail() method will return a nonempty dictionary value if the SMTP server reported an error sending that particular email. The last part of the for loop at ❹ checks if the returned dictionary is nonempty, and if it is, prints the recipient’s email address and the returned dictionary.

After the program is done sending all the emails, the quit() method is called to disconnect from the SMTP server.

When you run the program, the output will look something like this:


Sending email to <span><a href="alice@example.com">alice@example.com...</a></span>
Sending email to <span><a href="bob@example.com">bob@example.com...</a></span>
Sending email to <span><a href=" eve@example.com"> eve@example.com...</a></span>
The recipients will receive an email that looks like Figure 16-3.

<!-- ![image](assets/000025.jpg)
 -->
Figure 16-3. An automatically sent email from sendDuesReminders.py

