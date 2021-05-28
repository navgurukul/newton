```ngMeta
project-generating-random-quiz-files_key1
```
# project-generating-random-quiz-files_key2
project-generating-random-quiz-files_key3

project-generating-random-quiz-files_key4

project-generating-random-quiz-files_key5

project-generating-random-quiz-files_key6

project-generating-random-quiz-files_key7

project-generating-random-quiz-files_key8

project-generating-random-quiz-files_key9

project-generating-random-quiz-files_key10

project-generating-random-quiz-files_key11

project-generating-random-quiz-files_key12

project-generating-random-quiz-files_key13

# project-generating-random-quiz-files_key14
project-generating-random-quiz-files_key15


project-generating-random-quiz-files_key16 project-generating-random-quiz-files_key17
 project-generating-random-quiz-files_key18
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
project-generating-random-quiz-files_key19

# project-generating-random-quiz-files_key20
project-generating-random-quiz-files_key21

project-generating-random-quiz-files_key22

project-generating-random-quiz-files_key23


project-generating-random-quiz-files_key24 project-generating-random-quiz-files_key25
 project-generating-random-quiz-files_key26
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
project-generating-random-quiz-files_key27project-generating-random-quiz-files_key28project-generating-random-quiz-files_key29project-generating-random-quiz-files_key30project-generating-random-quiz-files_key31

project-generating-random-quiz-files_key32

# project-generating-random-quiz-files_key33
project-generating-random-quiz-files_key34


project-generating-random-quiz-files_key35 project-generating-random-quiz-files_key36
 project-generating-random-quiz-files_key37
project-generating-random-quiz-files_key38

project-generating-random-quiz-files_key39

project-generating-random-quiz-files_key40

project-generating-random-quiz-files_key41

project-generating-random-quiz-files_key42


project-generating-random-quiz-files_key43 project-generating-random-quiz-files_key44
 project-generating-random-quiz-files_key45
project-generating-random-quiz-files_key46```python
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
project-generating-random-quiz-files_key47

project-generating-random-quiz-files_key48

project-generating-random-quiz-files_key49


project-generating-random-quiz-files_key50

project-generating-random-quiz-files_key51

project-generating-random-quiz-files_key52

1. project-generating-random-quiz-files_key53
2. project-generating-random-quiz-files_key54
project-generating-random-quiz-files_key55


1. project-generating-random-quiz-files_key56
2. project-generating-random-quiz-files_key57
3. project-generating-random-quiz-files_key58
4. project-generating-random-quiz-files_key59
project-generating-random-quiz-files_key60