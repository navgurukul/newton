```ngMeta
project-automatic-form-filler_key1
```

project-automatic-form-filler_key2
project-automatic-form-filler_key3


project-automatic-form-filler_key4


![image](assets/000021.jpg)project-automatic-form-filler_key5


project-automatic-form-filler_key6


project-automatic-form-filler_key7


project-automatic-form-filler_key8


project-automatic-form-filler_key9


project-automatic-form-filler_key10


project-automatic-form-filler_key11


project-automatic-form-filler_key12


project-automatic-form-filler_key13


project-automatic-form-filler_key14


project-automatic-form-filler_key15


project-automatic-form-filler_key16
project-automatic-form-filler_key17


project-automatic-form-filler_key18


project-automatic-form-filler_key19


project-automatic-form-filler_key20


project-automatic-form-filler_key21


project-automatic-form-filler_key22


project-automatic-form-filler_key23


project-automatic-form-filler_key24


project-automatic-form-filler_key25


project-automatic-form-filler_key26


project-automatic-form-filler_key27


project-automatic-form-filler_key28
project-automatic-form-filler_key29


project-automatic-form-filler_key30


project-automatic-form-filler_key31



project-automatic-form-filler_key32
project-automatic-form-filler_key33
project-automatic-form-filler_key34


project-automatic-form-filler_key35
project-automatic-form-filler_key36


project-automatic-form-filler_key37
project-automatic-form-filler_key38
project-automatic-form-filler_key39
project-automatic-form-filler_key40
project-automatic-form-filler_key41
project-automatic-form-filler_key42
project-automatic-form-filler_key43
project-automatic-form-filler_key44
project-automatic-form-filler_key45
project-automatic-form-filler_key46
project-automatic-form-filler_key47



project-automatic-form-filler_key48
project-automatic-form-filler_key49
project-automatic-form-filler_key50
```python
formData = [{'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'wand',
            'robocop': 4, 'comments': 'Tell Bob I said hi.'},
            {'name': 'Bob', 'fear': 'bees', 'source': 'amulet', 'robocop': 4,
            'comments': 'n/a'},
            {'name': 'Carol', 'fear': 'puppets', 'source': 'crystal ball',
            'robocop': 1, 'comments': 'Please take the puppets out of thebreak room.'},{'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money',
            'robocop': 5, 'comments': 'Protect the innocent. Serve the publictrust. Uphold the law.'},]
```
project-automatic-form-filler_key51



project-automatic-form-filler_key52
project-automatic-form-filler_key53
project-automatic-form-filler_key54


project-automatic-form-filler_key55



project-automatic-form-filler_key56
project-automatic-form-filler_key57
project-automatic-form-filler_key58
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
project-automatic-form-filler_key59


project-automatic-form-filler_key60



project-automatic-form-filler_key61
project-automatic-form-filler_key62
project-automatic-form-filler_key63
```python
❶     print('Entering %s info...' % (person['name']))
❷     pyautogui.click(nameField[0], nameField[1])

       # Fill out the Name field.
❸     pyautogui.typewrite(person['name'] + '\t')

       # Fill out the Greatest Fear(s) field.
❹     pyautogui.typewrite(person['fear'] + '\t')
```
project-automatic-form-filler_key64


project-automatic-form-filler_key65


project-automatic-form-filler_key66
project-automatic-form-filler_key67


project-automatic-form-filler_key68



project-automatic-form-filler_key69
project-automatic-form-filler_key70
project-automatic-form-filler_key71
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
project-automatic-form-filler_key72


project-automatic-form-filler_key73


project-automatic-form-filler_key74
project-automatic-form-filler_key75


project-automatic-form-filler_key76


project-automatic-form-filler_key77


project-automatic-form-filler_key78



project-automatic-form-filler_key79
project-automatic-form-filler_key80
project-automatic-form-filler_key81
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
project-automatic-form-filler_key82


project-automatic-form-filler_key83
project-automatic-form-filler_key84


project-automatic-form-filler_key85


project-automatic-form-filler_key86
