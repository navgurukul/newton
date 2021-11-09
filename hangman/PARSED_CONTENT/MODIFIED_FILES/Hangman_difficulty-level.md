difficulty-level_key1
difficulty-level_key2


difficulty-level_key3


difficulty-level_key4
- difficulty-level_key5
- difficulty-level_key6
difficulty-level_key7
@[youtube](https://www.youtube.com/watch?v=f-2A-OeYSWA)

difficulty-level_key8
difficulty-level_key9
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
```difficulty-level_key10


difficulty-level_key11
```python
    while (True):
        else:
            print "Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed)
            print IMAGES[images_selection_list_indices[total_lives-remaining_lives]] ## <-- CHANGES HERE
            print "Remaining Lives : ", remaining_lives
            print ""
            letters_guessed.append(letter)
            remaining_lives -= 1
```difficulty-level_key12


difficulty-level_key13
