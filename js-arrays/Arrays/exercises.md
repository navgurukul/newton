## Exercises:


1. Create an array named “myFavouriteGames” and store the elements of different games in it.

    ```js
    var myFavouriteGames = ["chess", "Ludo", "Badminton", "Volleyball"]
    console.log(myFavouriteGames);
    ```

2. Create an array named myFavouriteFruits, with 4 elements. Console the third element of the array.

    ```js
    var myFavouriteFruits = ["Mango", "Orange", "Banana", "Grapes"]
    
    console.log(myFavouriteFruits[2])
    ```

3. What is the output for the following code?
    ```js
    var myFavouriteFruits = ["Mango", "Orange", "Banana"]

    console.log(myFavouriteFruits.pop())

    // ouput [“Mango”, “orange”]
	```

4. Add “Basketball” in the beginning of the array?
    ```js
    var myFavouriteGames = ["Chess", "Ludo", "Badminton"]
    ```
    ```js
    let myFavouriteGames = ["Chess", "Ludo", "Badminton"]
    myFavouriteGames.unshift("Basketball")
    console.log(myFavouriteGames)
    ```


5. What output will it show :
    ```js
    let myFavouriteGames = ["chess", "Ludo", "Badminton"]
    console.log(myFavouriteGames.2)
    ```
    Feedback after submit
        
        Syntax error!
 
6. Remove the element “BasketBall” in this array:
    ```js
    let myFavouriteGames = ["chess", "Ludo", "Badminton", "Basketball", "Carom", "Cricket"]
    ```
    ```js
    let myFavouriteGames = ["chess", "Ludo", "Badminton", "Basketball", "Carom", "Cricket"]
    let removedItems = myFavouriteGames.splice(3,1)
    console.log(myFavouriteGames)
    ```
	
