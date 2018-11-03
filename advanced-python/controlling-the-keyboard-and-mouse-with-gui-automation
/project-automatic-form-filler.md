```ngMeta
name: project-automatic-form-filler
completionMethod: manual
```
# Project: Automatic Form Filler
Of all the boring tasks, filling out forms is the most dreaded of chores. It’s only fitting that now, in the final chapter project, you will slay it. Say you have a huge amount of data in a spreadsheet, and you have to tediously retype it into some other application’s form interface—with no intern to do it for you. Although some applications will have an Import feature that will allow you to upload a spreadsheet with the information, sometimes it seems that there is no other way than mindlessly clicking and typing for hours on end. You’ve come this far in this book; you know that of course there’s another way.

The form for this project is a Google Docs form that you can find at <span><a href="http://autbor.com/form">http://autbor.com/form</a></span>. It looks like Figure 18-4.

<!-- ![image](assets/000021.jpg)
 -->
Figure 18-4. The form used for this project

At a high level, here’s what your program should do:

Click the first text field of the form.

Move through the form, typing information into each field.

Click the Submit button.

Repeat the process with the next set of data.

This means your code will need to do the following:

Call pyautogui.click() to click the form and Submit button.

Call pyautogui.typewrite() to enter text into the fields.

Handle the KeyboardInterrupt exception so the user can press CTRL-C to quit.

Open a new file editor window and save it as formFiller.py.

# Step 1: Figure Out the Steps
Before writing code, you need to figure out the exact keystrokes and mouse clicks that will fill out the form once. The mouseNow.py script in Project: “Where Is the Mouse Right Now?” can help you figure out specific mouse coordinates. You need to know only the coordinates of the first text field. After clicking the first field, you can just press TAB to move focus to the next field. This will save you from having to figure out the x- and y-coordinates to click for every field.

Here are the steps for entering data into the form:

Click the Name field. (Use mouseNow.py to determine the coordinates after maximizing the browser window. On OS X, you may need to click twice: once to put the browser in focus and again to click the Name field.)

Type a name and then press TAB.

Type a greatest fear and then press TAB.

Press the down arrow key the correct number of times to select the wizard power source: once for wand, twice for amulet, three times for crystal ball, and four times for money. Then press TAB. (Note that on OS X, you will have to press the down arrow key one more time for each option. For some browsers, you may need to press the ENTER key as well.)

Press the right arrow key to select the answer to the Robocop question. Press it once for 2, twice for 3, three times for 4, or four times for 5; or just press the spacebar to select 1 (which is highlighted by default). Then press TAB.

Type an additional comment and then press TAB.

Press the ENTER key to “click” the Submit button.

After submitting the form, the browser will take you to a page where you will need to click a link to return to the form page.

Note that if you run this program again later, you may have to update the mouse click coordinates, since the browser window might have changed position. To work around this, always make sure the browser window is maximized before finding the coordinates of the first form field. Also, different browsers on different operating systems might work slightly differently from the steps given here, so check that these keystroke combinations work for your computer before running your program.

# Step 2: Set Up Coordinates
Load the example form you downloaded (Figure 18-4) in a browser and maximize your browser window. Open a new Terminal or command line window to run the mouseNow.py script, and then mouse over the Name field to figure out its the x- and y-coordinates. These numbers will be assigned to the nameField variable in your program. Also, find out the x- and y-coordinates and RGB tuple value of the blue Submit button. These values will be assigned to the submitButton and submitButtonColor variables, respectively.

Next, fill in some dummy data for the form and click Submit. You need to see what the next page looks like so that you can use mouseNow.py to find the coordinates of the Submit another response link on this new page.

Make your source code look like the following, being sure to replace all the values in italics with the coordinates you determined from your own tests:


#! python3
# formFiller.py - Automatically fills in the form.

import pyautogui, time

# Set these to the correct coordinates for your computer.
nameField = (648, 319)
submitButton = (651, 817)
submitButtonColor = (75, 141, 249)
submitAnotherLink = (760, 224)

# TODO: Give the user a chance to kill the script.

# TODO: Wait until the form page has loaded.

# TODO: Fill out the Name Field.

# TODO: Fill out the Greatest Fear(s) field.

# TODO: Fill out the Source of Wizard Powers field.

# TODO: Fill out the Robocop field.

# TODO: Fill out the Additional Comments field.

# TODO: Click Submit.

# TODO: Wait until form page has loaded.

# TODO: Click the Submit another response link.
Now you need the data you actually want to enter into this form. In the real world, this data might come from a spreadsheet, a plaintext file, or a website, and it would require additional code to load into the program. But for this project, you’ll just hardcode all this data in a variable. Add the following to your program:


#! python3
# formFiller.py - Automatically fills in the form.

--snip--
```python
formData = [{'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'wand',
            'robocop': 4, 'comments': 'Tell Bob I said hi.'},
            {'name': 'Bob', 'fear': 'bees', 'source': 'amulet', 'robocop': 4,
            'comments': 'n/a'},
            {'name': 'Carol', 'fear': 'puppets', 'source': 'crystal ball',
            'robocop': 1, 'comments': 'Please take the puppets out of thebreak room.'},{'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money',
            'robocop': 5, 'comments': 'Protect the innocent. Serve the publictrust. Uphold the law.'},]
```
--snip--
The formData list contains four dictionaries for four different names. Each dictionary has names of text fields as keys and responses as values. The last bit of setup is to set PyAutoGUI’s PAUSE variable to wait half a second after each function call. Add the following to your program after the formData assignment statement:


pyautogui.PAUSE = 0.5
# Step 3: Start Typing Data
A for loop will iterate over each of the dictionaries in the formData list, passing the values in the dictionary to the PyAutoGUI functions that will virtually type in the text fields.

Add the following code to your program:


   #! python3
   # formFiller.py - Automatically fills in the form.

   --snip--
```python
   for person in formData:
       # Give the user a chance to kill the script.
       print('>>> 5 SECOND PAUSE TO LET USER PRESS CTRL-C <<<')
❶     time.sleep(5)

       # Wait until the form page has loaded.
❷     while not pyautogui.pixelMatchesColor(submitButton[0], submitButton[1],
       submitButtonColor):
           time.sleep(0.5)
```
   --snip--
As a small safety feature, the script has a five-second pause ❶ that gives the user a chance to hit CTRL-C (or move the mouse cursor to the upper-left corner of the screen to raise the FailSafeException exception) to shut the program down in case it’s doing something unexpected. Then the program waits until the Submit button’s color is visible ❷, letting the program know that the form page has loaded. Remember that you figured out the coordinate and color information in step 2 and stored it in the submitButton and submitButtonColor variables. To use pixelMatchesColor(), you pass the coordinates submitButton[0] and submitButton[1], and the color submitButtonColor.

After the code that waits until the Submit button’s color is visible, add the following:


   #! python3
   # formFiller.py - Automatically fills in the form.

   --snip--
```python
❶     print('Entering %s info...' % (person['name']))
❷     pyautogui.click(nameField[0], nameField[1])

       # Fill out the Name field.
❸     pyautogui.typewrite(person['name'] + '\t')

       # Fill out the Greatest Fear(s) field.
❹     pyautogui.typewrite(person['fear'] + '\t')
```
   --snip--
We add an occasional print() call to display the program’s status in its Terminal window to let the user know what’s going on ❶.

Since the program knows that the form is loaded, it’s time to call click() to click the Name field ❷ and typewrite() to enter the string in person['name'] ❸. The '\t' character is added to the end of the string passed to typewrite() to simulate pressing TAB, which moves the keyboard focus to the next field, Greatest Fear(s). Another call to typewrite() will type the string in person['fear'] into this field and then tab to the next field in the form ❹.

# Step 4: Handle Select Lists and Radio Buttons
The drop-down menu for the “wizard powers” question and the radio buttons for the Robocop field are trickier to handle than the text fields. To click these options with the mouse, you would have to figure out the x- and y-coordinates of each possible option. It’s easier to use the keyboard arrow keys to make a selection instead.

Add the following to your program:


   #! python3
   # formFiller.py - Automatically fills in the form.

   --snip--
```python
       # Fill out the Source of Wizard Powers field.
❶     if person['source'] == 'wand':
❷         pyautogui.typewrite(['down', '\t'])
       elif person['source'] == 'amulet':
           pyautogui.typewrite(['down', 'down', '\t'])
       elif person['source'] == 'crystal ball':
           pyautogui.typewrite(['down', 'down', 'down', '\t'])
       elif person['source'] == 'money':
           pyautogui.typewrite(['down', 'down', 'down', 'down', '\t'])

       # Fill out the Robocop field.
❸     if person['robocop'] == 1:
❹         pyautogui.typewrite([' ', '\t'])
       elif person['robocop'] == 2:
           pyautogui.typewrite(['right', '\t'])
       elif person['robocop'] == 3:
           pyautogui.typewrite(['right', 'right', '\t'])
       elif person['robocop'] == 4:
           pyautogui.typewrite(['right', 'right', 'right', '\t'])
       elif person['robocop'] == 5:
           pyautogui.typewrite(['right', 'right', 'right', 'right', '\t'])
```
   --snip--
Once the drop-down menu has focus (remember that you wrote code to simulate pressing TAB after filling out the Greatest Fear(s) field), pressing the down arrow key will move to the next item in the selection list. Depending on the value in person['source'], your program should send a number of down arrow keypresses before tabbing to the next field. If the value at the 'source' key in this user’s dictionary is 'wand' ❶, we simulate pressing the down arrow key once (to select Wand) and pressing TAB ❷. If the value at the 'source' key is 'amulet', we simulate pressing the down arrow key twice and pressing TAB, and so on for the other possible answers.

The radio buttons for the Robocop question can be selected with the right arrow keys—or, if you want to select the first choice ❸, by just pressing the spacebar ❹.

# Step 5: Submit the Form and Wait
You can fill out the Additional Comments field with the typewrite() function by passing person['comments'] as an argument. You can type an additional '\t' to move the keyboard focus to the next field or the Submit button. Once the Submit button is in focus, calling pyautogui.press('enter') will simulate pressing the ENTER key and submit the form. After submitting the form, your program will wait five seconds for the next page to load.

Once the new page has loaded, it will have a Submit another response link that will direct the browser to a new, empty form page. You stored the coordinates of this link as a tuple in submitAnotherLink in step 2, so pass these coordinates to pyautogui.click() to click this link.

With the new form ready to go, the script’s outer for loop can continue to the next iteration and enter the next person’s information into the form.

Complete your program by adding the following code:


#! python3
# formFiller.py - Automatically fills in the form.

--snip--
```python
    # Fill out the Additional Comments field.
    pyautogui.typewrite(person['comments'] + '\t')

    # Click Submit.
    pyautogui.press('enter')

    # Wait until form page has loaded.
    print('Clicked Submit.')
    time.sleep(5)

    # Click the Submit another response link.
```
    pyautogui.click(submitAnotherLink[0], submitAnotherLink[1])
Once the main for loop has finished, the program will have plugged in the information for each person. In this example, there are only four people to enter. But if you had 4,000 people, then writing a program to do this would save you a lot of time and typing!

# Summary
GUI automation with the pyautogui module allows you to interact with applications on your computer by controlling the mouse and keyboard. While this approach is flexible enough to do anything that a human user can do, the downside is that these programs are fairly blind to what they are clicking or typing. When writing GUI automation programs, try to ensure that they will crash quickly if they’re given bad instructions. Crashing is annoying, but it’s much better than the program continuing in error.

You can move the mouse cursor around the screen and simulate mouse clicks, keystrokes, and keyboard shortcuts with PyAutoGUI. The pyautogui module can also check the colors on the screen, which can provide your GUI automation program with enough of an idea of the screen contents to know whether it has gotten offtrack. You can even give PyAutoGUI a screen-shot and let it figure out the coordinates of the area you want to click.

You can combine all of these PyAutoGUI features to automate any mindlessly repetitive task on your computer. In fact, it can be downright hypnotic to watch the mouse cursor move on its own and see text appear on the screen automatically. Why not spend the time you saved by sitting back and watching your program do all your work for you? There’s a certain satisfaction that comes from seeing how your cleverness has saved you from the boring stuff.