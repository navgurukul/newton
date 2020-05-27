```ngMeta
submission_type:url
```
## Difficulty Level
Game shuru karne se pehle aap user se poocho, ki user kitna difficulty level par khelna chahta hai. - Easy, Medium ya Hard.
Easy, Medium aur Hard levels ke liye user ko 8, 6, 4 chances respectively do. (Yaani Easy ke liye 8, Medium ke liye 6 aur Hard ke liye 4).

Dhyaan rakhna ki humne graphics bhi use kiye the user ki remaining lives dikhane ke liye, toh hum uss code mei kaise change karenge? Jaise hard wale level mei - ek ek image skip kar kar dikha sakte hai.

## Hint
- Program ka control flow sahi se samajhna bahut important hai
- Kyuki yeh sirf user se ek baar poochna hai, toh yeh loop ke bahar hona chahiye

## Solution

@[youtube](https://www.youtube.com/watch?v=f-2A-OeYSWA)

## Possible Solution
..................... in the hangman function ............................
...
...
...
```python
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is " + str(len(secret_word)) + " letters long."
    print ""

    user_difficulty_choice = raw_input("Aap abhi kitni difficulty par yeh game khelna chahte ho?\na)\tEasy\nb)\tMedium\nc)\tHard\n\nApni choice a, b, ya c ki terms mei batayein\n"))

    total_lives = remaining_lives = 8
    # images_selection_list_indices mei hum woh images ke indices
    # store kar rahe hai, jo hume display karni hai, kyuki jab
    # total_lives 8 se kam hogi toh hum kuch hi images dikha sakte hai

    images_selection_list_indices = [0, 1, 2, 3, 4, 5, 6, 7]

    if user_difficult_choice not in ["a", "b", "c"]:
        print "Aapki choice invalid hai.\nGame easy mode mei start kar rahe hai")

    else:
        if user_difficulty_choice == "b":
            total_lives = remaining_lives = 6
            images_selection_list_indices = [0, 2, 3, 5, 6, 7]

        elif user_difficulty_choice == "c":
            total_lives = remaining_lives = 4
            images_selection_list_indices = [1, 3, 5, 7]
        
    letters_guessed = []
```
...
...
...

..................... in the hangman function ............................
...
...
...
```python
    while (True):
        else:
            print "Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed)
            print IMAGES[images_selection_list_indices[total_lives-remaining_lives]] ## <-- CHANGES HERE
            print "Remaining Lives : ", remaining_lives
            print ""
            letters_guessed.append(letter)
            remaining_lives -= 1
```
...
...
...

Aap yeh kaam alag tarah se bhi kar sakte hai, yeh sirf ek possible solution hai.
