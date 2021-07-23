```ngMeta
using-data-structures-to-model-real-world-things_key1
```

using-data-structures-to-model-real-world-things_key2
using-data-structures-to-model-real-world-things_key3


using-data-structures-to-model-real-world-things_key4


using-data-structures-to-model-real-world-things_key5


using-data-structures-to-model-real-world-things_key6


using-data-structures-to-model-real-world-things_key7


using-data-structures-to-model-real-world-things_key8


using-data-structures-to-model-real-world-things_key9


using-data-structures-to-model-real-world-things_key10
using-data-structures-to-model-real-world-things_key11


using-data-structures-to-model-real-world-things_key12


![Anoop](assets/000003.png)using-data-structures-to-model-real-world-things_key13


using-data-structures-to-model-real-world-things_key14


```python
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
```
using-data-structures-to-model-real-world-things_key15


![Anoop](assets/000006.png)using-data-structures-to-model-real-world-things_key16


using-data-structures-to-model-real-world-things_key17


```python
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': 'X', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
```
using-data-structures-to-model-real-world-things_key18


![Anoop](assets/000008.png)using-data-structures-to-model-real-world-things_key19


using-data-structures-to-model-real-world-things_key20


```python
theBoard = {'top-L': 'O', 'top-M': 'O', 'top-R': 'O',
            'mid-L': 'X', 'mid-M': 'X', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': 'X'}
```
using-data-structures-to-model-real-world-things_key21


![image](assets/000010.png)using-data-structures-to-model-real-world-things_key22


using-data-structures-to-model-real-world-things_key23


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
using-data-structures-to-model-real-world-things_key24



using-data-structures-to-model-real-world-things_key25


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
using-data-structures-to-model-real-world-things_key26



using-data-structures-to-model-real-world-things_key27


using-data-structures-to-model-real-world-things_key28



using-data-structures-to-model-real-world-things_key29



using-data-structures-to-model-real-world-things_key30
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
using-data-structures-to-model-real-world-things_key31


using-data-structures-to-model-real-world-things_key32



using-data-structures-to-model-real-world-things_key33


using-data-structures-to-model-real-world-things_key34


using-data-structures-to-model-real-world-things_key35


using-data-structures-to-model-real-world-things_key36
