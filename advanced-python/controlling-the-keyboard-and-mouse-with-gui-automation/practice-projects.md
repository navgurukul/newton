```ngMeta
name: practice-projects
```
# Practice Projects
For practice, write programs that do the following.

#  Looking Busy
Many instant messaging programs determine whether you are idle, or away from your computer, by detecting a lack of mouse movement over some period of time—say, ten minutes. Maybe you’d like to sneak away from your desk for a while but don’t want others to see your instant messenger status go into idle mode. Write a script to nudge your mouse cursor slightly every ten seconds. The nudge should be small enough so that it won’t get in the way if you do happen to need to use your computer while the script is running.

# Instant Messenger Bot
Google Talk, Skype, Yahoo Messenger, AIM, and other instant messaging applications often use proprietary protocols that make it difficult for others to write Python modules that can interact with these programs. But even these proprietary protocols can’t stop you from writing a GUI automation tool.

The Google Talk application has a search bar that lets you enter a username on your friend list and open a messaging window when you press ENTER. The keyboard focus automatically moves to the new window. Other instant messenger applications have similar ways to open new message windows. Write a program that will automatically send out a notification message to a select group of people on your friend list. Your program may have to deal with exceptional cases, such as friends being offline, the chat window appearing at different coordinates on the screen, or confirmation boxes that interrupt your messaging. Your program will have to take screen-shots to guide its GUI interaction and adopt ways of detecting when its virtual keystrokes aren’t being sent.

# Note
You may want to set up some fake test accounts so that you don’t accidentally spam your real friends while writing this program.

# Game-Playing Bot Tutorial
There is a great tutorial titled “How to Build a Python Bot That Can Play Web Games” that you can find at <span><a href="http://nostarch.com/automatestuff/">http://nostarch.com/automatestuff/</a></span>. This tutorial explains how to create a GUI automation program in Python that plays a Flash game called Sushi Go Round. The game involves clicking the correct ingredient buttons to fill customers’ sushi orders. The faster you fill orders without mistakes, the more points you get. This is a perfectly suited task for a GUI automation program—and a way to cheat to a high score! The tutorial covers many of the same topics that this chapter covers but also includes descriptions of PyAutoGUI’s basic image recognition features.