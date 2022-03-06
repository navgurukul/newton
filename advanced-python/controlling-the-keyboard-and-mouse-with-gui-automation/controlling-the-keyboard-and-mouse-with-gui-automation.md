```ngMeta
name: controlling-the-keyboard-and-mouse-with-gui-automation
```
# Controlling the Keyboard and Mouse with GUI Automation
Knowing various Python modules for editing spreadsheets, downloading files, and launching programs is useful, but sometimes there just aren’t any modules for the applications you need to work with. The ultimate tools for automating tasks on your computer are programs you write that directly control the keyboard and mouse. These programs can control other applications by sending them virtual keystrokes and mouse clicks, justpython3- as if you were sitting at your computer and interacting with the applications yourself. This technique is known as graphical user interface automation, or GUI automation for short. With GUI automation, your programs can do anything that a human user sitting at the computer can do, except spill coffee on the keyboard.

Think of GUI automation as programming a robotic arm. You can program the robotic arm to type at your keyboard and move your mouse for you. This technique is particularly useful for tasks that involve a lot of mindless clicking or filling out of forms.

The pyautogui module has functions for simulating mouse movements, button clicks, and scrolling the mouse wheel. This chapter covers only a subset of PyAutoGUI’s features; you can find the full documentation at <span><a href="http://pyautogui.readthedocs.org/.">http://pyautogui.readthedocs.org/.</a></span>
# Installing the pyautogui Module
The pyautogui module can send virtual keypresses and mouse clicks to Windows, OS X, and Linux. Depending on which operating system you’re using, you may have to install some other modules (called dependencies) before you can install PyAutoGUI.

On Windows, there are no other modules to install.

On OS X, run sudo pip3 install pyobjc-framework-Quartz, sudo pip3 install pyobjc-core, and then sudo pip3 install pyobjc.

On Linux, run sudo pip3 install python3-xlib, sudo apt-get install scrot, sudo apt-get install python3-tk, and sudo apt-get install python3-dev. (Scrot is a screenshot program that PyAutoGUI uses.)

After these dependencies are installed, run pip install pyautogui (or pip3 on OS X and Linux) to install PyAutoGUI.

Appendix A has complete information on installing third-party modules. To test whether PyAutoGUI has been installed correctly, run import pyautogui from the interactive shell and check for any error messages.
# Staying on Track
Before you jump in to a GUI automation, you should know how to escape problems that may arise. Python can move your mouse and type keystrokes at an incredible speed. In fact, it might be too fast for other programs to keep up with. Also, if something goes wrong but your program keeps moving the mouse around, it will be hard to tell what exactly the program is doing or how to recover from the problem. Like the enchanted brooms from Disney’s The Sorcerer’s Apprentice, which kept filling—and then overfilling—Mickey’s tub with water, your program could get out of control even though it’s following your instructions perfectly. Stopping the program can be difficult if the mouse is moving around on its own, preventing you from clicking the IDLE window to close it. Fortunately, there are several ways to prevent or recover from GUI automation problems.
