```ngMeta
name: project-generating-random-quiz-files
```
# Project: Generating Random Quiz Files
Say you’re a geography teacher with 35 students in your class and you want to give a pop quiz on US state capitals. Alas, your class has a few bad eggs in it, and you can’t trust the students not to cheat. You’d like to randomize the order of questions so that each quiz is unique, making it impossible for anyone to crib answers from anyone else. Of course, doing this by hand would be a lengthy and boring affair. Fortunately, you know some Python.

Here is what the program does:

Creates 35 different quizzes.

Creates 50 multiple-choice questions for each quiz, in random order.

Provides the correct answer and three random wrong answers for each question, in random order.

Writes the quizzes to 35 text files.

Writes the answer keys to 35 text files.

This means the code will need to do the following:

Store the states and their capitals in a dictionary.

Call open(), write(), and close() for the quiz and answer key text files.

Use random.shuffle() to randomize the order of the questions and multiple-choice options.

# Step 1: Store the Quiz Data in a Dictionary
The first step is to create a skeleton script and fill it with your quiz data. Create a file named randomQuizGenerator.py, and make it look like the following:


   #! python3
   # randomQuizGenerator.py - Creates quizzes with questions and answers in
   # random order, along with the answer key.
```python
❶ import random

   # The quiz data. Keys are states and values are their capitals.
❷ capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New'
   Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh','
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West'
   Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}'

   # Generate 35 quiz files.
❸ for quizNum in range(35):
       # TODO: Create the quiz and answer key files.

       # TODO: Write out the header for the quiz.

       # TODO: Shuffle the order of the states.

       # TODO: Loop through all 50 states, making a question for each.
```
Since this program will be randomly ordering the questions and answers, you’ll need to import the random module ❶ to make use of its functions. The capitals variable ❷ contains a dictionary with US states as keys and their capitals as values. And since you want to create 35 quizzes, the code that actually generates the quiz and answer key files (marked with TODO comments for now) will go inside a for loop that loops 35 times ❸. (This number can be changed to generate any number of quiz files.)

# Step 2: Create the Quiz File and Shuffle the Question Order
Now it’s time to start filling in those TODOs.

The code in the loop will be repeated 35 times—once for each quiz—so you have to worry about only one quiz at a time within the loop. First you’ll create the actual quiz file. It needs to have a unique filename and should also have some kind of standard header in it, with places for the student to fill in a name, date, and class period. Then you’ll need to get a list of states in randomized order, which can be used later to create the questions and answers for the quiz.

Add the following lines of code to randomQuizGenerator.py:


   #! python3
   # randomQuizGenerator.py - Creates quizzes with questions and answers in
   # random order, along with the answer key.
```python
   --snip--

   # Generate 35 quiz files.
   for quizNum in range(35):
       # Create the quiz and answer key files.
❶     quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')
❷     answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')

       # Write out the header for the quiz.
❸     quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
       quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
       quizFile.write('\n\n')

       # Shuffle the order of the states.
       states = list(capitals.keys())
❹     random.shuffle(states)

       # TODO: Loop through all 50 states, making a question for each.
```
The filenames for the quizzes will be capitalsquiz<N>.txt, where <N> is a unique number for the quiz that comes from quizNum, the for loop’s counter. The answer key for capitalsquiz<N>.txt will be stored in a text file named capitalsquiz_answers<N>.txt. Each time through the loop, the %s placeholder in 'capitalsquiz%s.txt' and 'capitalsquiz_answers%s.txt' will be replaced by (quizNum + 1), so the first quiz and answer key created will be capitalsquiz1.txt and capitalsquiz_answers1.txt. These files will be created with calls to the open() function at ❶ and ❷, with 'w' as the second argument to open them in write mode.

The write() statements at ❸ create a quiz header for the student to fill out. Finally, a randomized list of US states is created with the help of the random.shuffle() function ❹, which randomly reorders the values in any list that is passed to it.

# Step 3: Create the Answer Options
Now you need to generate the answer options for each question, which will be multiple choice from A to D. You’ll need to create another for loop—this one to generate the content for each of the 50 questions on the quiz. Then there will be a third for loop nested inside to generate the multiple-choice options for each question. Make your code look like the following:


   #! python3
   # randomQuizGenerator.py - Creates quizzes with questions and answers in
   # random order, along with the answer key.

   --snip--

       # Loop through all 50 states, making a question for each.
       for questionNum in range(50):

           # Get right and wrong answers.
❶         correctAnswer = capitals[states[questionNum]]
❷         wrongAnswers = list(capitals.values())
❸         del wrongAnswers[wrongAnswers.index(correctAnswer)]
❹         wrongAnswers = random.sample(wrongAnswers, 3)
❺         answerOptions = wrongAnswers + [correctAnswer]
❻         random.shuffle(answerOptions)

           # TODO: Write the question and answer options to the quiz file.

           # TODO: Write the answer key to a file.
The correct answer is easy to get—it’s stored as a value in the capitals dictionary ❶. This loop will loop through the states in the shuffled states list, from states[0] to states[49], find each state in capitals, and store that state’s corresponding capital in correctAnswer.

The list of possible wrong answers is trickier. You can get it by duplicating all the values in the capitals dictionary ❷, deleting the correct answer ❸, and selecting three random values from this list ❹. The random.sample() function makes it easy to do this selection. Its first argument is the list you want to select from; the second argument is the number of values you want to select. The full list of answer options is the combination of these three wrong answers with the correct answers ❺. Finally, the answers need to be randomized ❻ so that the correct response isn’t always choice D.

Step 4: Write Content to the Quiz and Answer Key Files
All that is left is to write the question to the quiz file and the answer to the answer key file. Make your code look like the following:


   #! python3
   # randomQuizGenerator.py - Creates quizzes with questions and answers in
   # random order, along with the answer key.

   --snip--
```python
       # Loop through all 50 states, making a question for each.
       for questionNum in range(50):
           --snip--

           # Write the question and the answer options to the quiz file.
           quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1,
               states[questionNum]))
❶         for i in range(4):
❷             quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
           quizFile.write('\n')

           # Write the answer key to a file.
❸         answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[
              answerOptions.index(correctAnswer)]))
       quizFile.close()
       answerKeyFile.close()
```
A for loop that goes through integers 0 to 3 will write the answer options in the answerOptions list ❶. The expression 'ABCD'[i] at ❷ treats the string 'ABCD' as an array and will evaluate to 'A','B', 'C', and then 'D' on each respective iteration through the loop.

In the final line ❸, the expression answerOptions.index(correctAnswer) will find the integer index of the correct answer in the randomly ordered answer options, and 'ABCD'[answerOptions.index(correctAnswer)] will evaluate to the correct answer’s letter to be written to the answer key file.

After you run the program, this is how your capitalsquiz1.txt file will look, though of course your questions and answer options may be different from those shown here, depending on the outcome of your random.shuffle() calls:


Name:

Date:

Period:

                    State Capitals Quiz (Form 1)

1. What is the capital of West Virginia?
    A. Hartford
    B. Santa Fe
    C. Harrisburg
    D. Charleston

2. What is the capital of Colorado?
    A. Raleigh
    B. Harrisburg
    C. Denver
    D. Lincoln

--snip--
The corresponding capitalsquiz_answers1.txt text file will look like this:


1. D
2. C
3. A
4. C
--snip--