Remove the element “BasketBall” in this array?

```javascript
let myFavouriteGames = ["chess", "Ludo", "Badminton", "Basketball", "Carom", "Cricket"];
```

```solution
let myFavouriteGames = ["chess", "Ludo", "Badminton", "Basketball", "Carom", "Cricket"];
let removedItems = myFavouriteGames.splice(3,1);
console.log(myFavouriteGames);
```
