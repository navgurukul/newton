## Exercises:


1. Create an array named “myFavouriteGames” and store the elements of different games in it.

    ```javascript
    var myFavouriteGames = ["chess", "Ludo", "Badminton", "Volleyball"]
    console.log(myFavouriteGames);
    ```

2. Create an array named myFavouriteFruits, with 4 elements. Console the third element of the array.

    ```javascript
    var myFavouriteFruits = ["Mango", "Orange", "Banana", "Grapes"]
    
    console.log(myFavouriteFruits[2])
    ```

3. What is the output for the following code?
    ```javascript
    var myFavouriteFruits = ["Mango", "Orange", "Banana"]

    console.log(myFavouriteFruits.pop())

    // ouput [“Mango”, “orange”]
	```

4. Add “Basketball” in the beginning of the array?
    ```javascript
    var myFavouriteGames = ["Chess", "Ludo", "Badminton"]
    ```
    ```javascript
    let myFavouriteGames = ["Chess", "Ludo", "Badminton"]
    myFavouriteGames.unshift("Basketball")
    console.log(myFavouriteGames)
    ```


5. What output will it show :
    ```javascript
    let myFavouriteGames = ["chess", "Ludo", "Badminton"]
    console.log(myFavouriteGames.2)
    ```
    Feedback after submit
        
        Syntax error!
 
6. Remove the element “BasketBall” in this array:
    ```javascript
    let myFavouriteGames = ["chess", "Ludo", "Badminton", "Basketball", "Carom", "Cricket"]
    ```
    ```javascript
    let myFavouriteGames = ["chess", "Ludo", "Badminton", "Basketball", "Carom", "Cricket"]
    let removedItems = myFavouriteGames.splice(3,1)
    console.log(myFavouriteGames)
    ```
	
