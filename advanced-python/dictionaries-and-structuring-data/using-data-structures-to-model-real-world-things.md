```ngMeta
name: using-data-structures-to-model-real-world-things
```
# Using Data Structures to Model Real-World Things
Even before the Internet, it was possible to play a game of chess with someone on the other side of the world. Each player would set up a chessboard at their home and then take turns mailing a postcard to each other describing each move. To do this, the players needed a way to unambiguously describe the state of the board and their moves.

In algebraic chess notation, the spaces on the chessboard are identified by a number and letter coordinate, as in Figure

<!-- ![](assets/000002.jpg)
 -->
The coordinates of a chessboard in algebraic chess notation

The chess pieces are identified by letters: K for king, Q for queen, R for rook, B for bishop, and N for knight. Describing a move uses the letter of the piece and the coordinates of its destination. A pair of these moves describes what happens in a single turn (with white going first); for instance, the notation 2. Nf3 Nc6 indicates that white moved a knight to f3 and black moved a knight to c6 on the second turn of the game.

There’s a bit more to algebraic notation than this, but the point is that you can use it to unambiguously describe a game of chess without needing to be in front of a chessboard. Your opponent can even be on the other side of the world! In fact, you don’t even need a physical chess set if you have a good memory: You can just read the mailed chess moves and update boards you have in your imagination.

Computers have good memories. A program on a modern computer can easily store billions of strings like '2. Nf3 Nc6'. This is how computers can play chess without having a physical chessboard. They model data to represent a chessboard, and you can write code to work with this model.

This is where lists and dictionaries can come in. You can use them to model real-world things, like chessboards. For the first example, you’ll use a game that’s a little simpler than chess: tic-tac-toe.

# A Tic-Tac-Toe Board
A tic-tac-toe board looks like a large hash symbol (#) with nine slots that can each contain an X, an O, or a blank. To represent the board with a dictionary, you can assign each slot a string-value key, as shown in Figure 5-2.

You can use string values to represent what’s in each slot on the board: 'X', 'O', or ' ' (a space character). Thus, you’ll need to store nine strings. You can use a dictionary of values for this. The string value with the key 'top-R' can represent the top-right corner, the string value with the key 'low-L' can represent the bottom-left corner, the string value with the key 'mid-M' can represent the middle, and so on.

<!-- ![Anoop](assets/000003.png)
 -->
 The slots of a tic-tactoe board with their corresponding keys

This dictionary is a data structure that represents a tic-tac-toe board. Store this board-as-a-dictionary in a variable named theBoard. Open a new file editor window, and enter the following source code, saving it as ticTacToe.py:

```python
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
```
The data structure stored in the theBoard variable represents the tic-tactoe board in 

<!-- ![Anoop](assets/000006.png)
 -->
 An empty tic-tac-toe board

Since the value for every key in theBoard is a single-space string, this dictionary represents a completely clear board. If player X went first and chose the middle space, you could represent that board with this dictionary:

```python
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': 'X', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
```
The data structure in theBoard now represents the tic-tac-toe board in Figure

<!-- ![Anoop](assets/000008.png)
 -->
The first move

A board where player O has won by placing Os across the top might look like this:

```python
theBoard = {'top-L': 'O', 'top-M': 'O', 'top-R': 'O',
            'mid-L': 'X', 'mid-M': 'X', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': 'X'}
```
The data structure in theBoard now represents the tic-tac-toe board in Figure

<!-- ![image](assets/000010.png)
 -->
Player O wins.

Of course, the player sees only what is printed to the screen, not the contents of variables. Let’s create a function to print the board dictionary onto the screen. Make the following addition to ticTacToe.py (new code is in bold):

```python
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
printBoard(theBoard)
```
When you run this program, printBoard() will print out a blank tic-tactoe board.


| |
-+-+-
| |
-+-+-
| |
The printBoard() function can handle any tic-tac-toe data structure you pass it. Try changing the code to the following:

```python
theBoard = {'top-L': 'O', 'top-M': 'O', 'top-R': 'O', 'mid-L': 'X', 'mid-M':
'X', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': 'X'}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
printBoard(theBoard)
```
Now when you run this program, the new board will be printed to the screen.


O|O|O
-+-+-
X|X|
-+-+-
| |X
Because you created a data structure to represent a tic-tac-toe board and wrote code in printBoard() to interpret that data structure, you now have a program that “models” the tic-tac-toe board. You could have organized your data structure differently (for example, using keys like 'TOP-LEFT' instead of 'top-L'), but as long as the code works with your data structures, you will have a correctly working program.

For example, the printBoard() function expects the tic-tac-toe data structure to be a dictionary with keys for all nine slots. If the dictionary you passed was missing, say, the 'mid-L' key, your program would no longer work.


O|O|O
-+-+-
Traceback (most recent call last):
  File "ticTacToe.py", line 10, in <module>
    printBoard(theBoard)
  File "ticTacToe.py", line 6, in printBoard
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
KeyError: 'mid-L'
Now let’s add code that allows the players to enter their moves. Modify the ticTacToe.py program to look like this:


   theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': '
   ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
```python
   def printBoard(board):
       print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
       print('-+-+-')
       print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
       print('-+-+-')
       print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
   turn = 'X'
   for i in range(9):
❶      printBoard(theBoard)
        print('Turn for ' + turn + '. Move on which space?')
❷      move = input()
❸      theBoard[move] = turn
❹      if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
   printBoard(theBoard)
```
The new code prints out the board at the start of each new turn ❶, gets the active player’s move ❷, updates the game board accordingly ❸, and then swaps the active player ❹ before moving on to the next turn.

When you run this program, it will look something like this:


 | |
-+-+-
 | |
-+-+-
 | |
Turn for X. Move on which space?
mid-M
 | |
-+-+-
 |X|
-+-+-
 | |
Turn for O. Move on which space?
low-L
 | |
-+-+-
 |X|
-+-+-
O| |

--snip--

O|O|X
-+-+-
X|X|O
-+-+-
O| |X
Turn for X. Move on which space?
low-M
O|O|X
-+-+-
X|X|O
-+-+-
O|X|X
This isn’t a complete tic-tac-toe game—for instance, it doesn’t ever check whether a player has won—but it’s enough to see how data structures can be used in programs.

Note
If you are curious, the source code for a complete tic-tac-toe program is described in the resources available from<span><a href=" http://nostarch.com/automatestuff/.">automatestuff</a></span>