```ngMeta
name: Filters Continued
completionMethod: facilitator
```

# Filters Continued

- Ek aur example se samjhte hai. Iss example mei hum **filter filter** ka use karenge.

- Yeh filter **sirf arrays** par kaam karta hai. Iss filter ka use karke hum array ki items apne hisab 
   se dikha sakte hai. Jaise, 

_index.html_

```html
   <div ng-app="myApp" ng-controller="ctrl">
       <ul>
           <li ng-repeat="name in names | filter:'u'">
   {{ name }}
     </li>
       </ul>
   </div>
```

_app.js_

```javascript
angular.module('myApp', []).controller("ctrl", ["$scope",  function($scope) {
   $scope.names = ["rahul", "nitin", "dhannu", "shivam", "shakru", "manoj", "deepanshu", "suraj", "aslam"];
}]);

```

- Ab Html mei wo naam nhi ayenge jinke naam mei **‘u’ nahi hai.** 

- Humne filter mei **colon(:) ke** baad **‘u’** likha hai, yeh theek ek function ko **argument** dene ki tarah hai. Aap aisa soch 
  sakte ho ki humne **filter ko ‘u’ argument** pass kara hai.

- Dhyan rakhe filter **filter sirf arrays** par use hota hai.

- [Issue](https://github.com/vidur149/angular-todo/issues/1) **resolve karne se pehle yeh concept padho aur samjho.**
    - **filters** [en](https://www.w3schools.com/angular/angular_filters.asp), hi