```ngMeta
name: practice-projects
completionMethod: manual
```
# Practice Projects
For practice, write programs that do the following.

# Random Chore Assignment Emailer
Write a program that takes a list of people’s email addresses and a list of chores that need to be done and randomly assigns chores to people. Email each person their assigned chores. If you’re feeling ambitious, keep a record of each person’s previously assigned chores so that you can make sure the program avoids assigning anyone the same chore they did last time. For another possible feature, schedule the program to run once a week automatically.

Here’s a hint: If you pass a list to the random.choice() function, it will return a randomly selected item from the list. Part of your code could look like this:


chores = ['dishes', 'bathroom', 'vacuum', 'walk dog']
randomChore = random.choice(chores)
chores.remove(randomChore) # this chore is now taken, so remove it
# Umbrella Reminder
Chapter 11 showed you how to use the requests module to scrape data from <span><a href="http://weather.gov/">http://weather.gov/</a></span>. Write a program that runs just before you wake up in the morning and checks whether it’s raining that day. If so, have the program text you a reminder to pack an umbrella before leaving the house.

# Auto Unsubscriber
Write a program that scans through your email account, finds all the unsubscribe links in all your emails, and automatically opens them in a browser. This program will have to log in to your email provider’s IMAP server and download all of your emails. You can use BeautifulSoup (covered in Chapter 11) to check for any instance where the word unsubscribe occurs within an HTML link tag.

Once you have a list of these URLs, you can use webbrowser.open() to automatically open all of these links in a browser.

You’ll still have to manually go through and complete any additional steps to unsubscribe yourself from these lists. In most cases, this involves clicking a link to confirm.

But this script saves you from having to go through all of your emails looking for unsubscribe links. You can then pass this script along to your friends so they can run it on their email accounts. (Just make sure your email password isn’t hardcoded in the source code!)