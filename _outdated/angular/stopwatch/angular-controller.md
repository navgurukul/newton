```ngMeta
name: PartII Counter
```
# Part II Counter

- Aapko ab _[yeh](https://github.com/vidur149/angular-multifunctional/issues/2)_ issue resolve karna hai. Issue resolve karne se pehle iss slide ko dhyan se padhe.

- **AngularJS** ka code Html mein nahi likhna chahiye. Isliye hum **angularJS** ka code ek **separate JS** file mein likhenge. Aur usse apne Html mei **include** kar denge.

- Html DOM ko JS se control karne ke liye controller ka use karte hai. 
Kissi bhi Html tag par ```<html_tag ng-controller = "controller ka naam">``` likhne se controller ki shuruwaat ho jaati hai.

- Controller mei hum **variables** aur **functions** define kar sakte hai. Inn variables aur functions ko Html mei use karne ke liye **$scope** ka use kiya jaata hai. $scope humein apne controller mei inject karna hota hai yaani ki controller mei daalna hota taaki hum usse use kar paaye.
```javascript
angular.module('app ka naam', [])
	.controller('controller ka naam', ['$scope', function($scope) {
	   	// controller logic
	}]);
```
- Jaise hum Jquery mei click event par function call karte hai, ussi tarah hum html tag par 
    ```<html_tag ng-click = "function ka naam">``` se controller ka function **click** par call kar sakte hai. 

**Assignment karne se pehle, yeh concepts padho aur samjho:**
  - **Data-Binding**, [en](http://learnkode.com/Tutorial/Angular/angular-databinding), hi
  - **Angular-controller** [en](https://www.w3schools.com/angular/angular_modules.asp#ez-insert-after-placeholder-124), hi
  - **ng-click** [en](http://tutlane.com/tutorial/angularjs/angularjs-ng-click-event-function-with-example), hi
  - **Scope**, [en](https://www.w3schools.com/angular/angular_scopes.asp), hi