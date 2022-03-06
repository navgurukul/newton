using-data-structures-to-model-real-world-things_key1
using-data-structures-to-model-real-world-things_key2


using-data-structures-to-model-real-world-things_key3


![](assets/000002.jpg)
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

```using-data-structures-to-model-real-world-things_key4
using-data-structures-to-model-real-world-things_key5


![Anoop](assets/000006.png)
using-data-structures-to-model-real-world-things_key6


using-data-structures-to-model-real-world-things_key7


```python
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': 'X', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
```
using-data-structures-to-model-real-world-things_key8


![Anoop](assets/000008.png)
using-data-structures-to-model-real-world-things_key9


using-data-structures-to-model-real-world-things_key10


```python
theBoard = {'top-L': 'O', 'top-M': 'O', 'top-R': 'O',
            'mid-L': 'X', 'mid-M': 'X', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': 'X'}
```
using-data-structures-to-model-real-world-things_key11


![image](assets/000010.png)
using-data-structures-to-model-real-world-things_key12


using-data-structures-to-model-real-world-things_key13


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
using-data-structures-to-model-real-world-things_key14



using-data-structures-to-model-real-world-things_key15


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
using-data-structures-to-model-real-world-things_key16



using-data-structures-to-model-real-world-things_key17


using-data-structures-to-model-real-world-things_key18



using-data-structures-to-model-real-world-things_key19



using-data-structures-to-model-real-world-things_key20
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
using-data-structures-to-model-real-world-things_key21


using-data-structures-to-model-real-world-things_key22



using-data-structures-to-model-real-world-things_key23


using-data-structures-to-model-real-world-things_key24


using-data-structures-to-model-real-world-things_key25


using-data-structures-to-model-real-world-things_key26
