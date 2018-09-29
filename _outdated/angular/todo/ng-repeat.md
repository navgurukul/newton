```ngMeta
name: Part I ng-repeat
completionMethod: peer
```
# Part I ng-repeat

- ToDo app ki help se humein jitne bhi kaam karne hai unhe yaad rakh sakte hai. Iss project mei aap aise hi ek ToDo app banoge.Hum step-by-step apni ToDo app mein features add karte jayenge.

- Aapko yaad hoga ki hum angular app ki shuruwaat **ng-app** se karte hai, **ng-controller** se controller ki. Inko **angular directives** bolte hai. Directives **normal Html tags** ko aur **powerful** bana dete hai.

- Aisa hi ek aur directive hota hai **ng-repeat.** Iss directive ki help se hum apne **Html ko repeat** kar sakte hai. Jaise,

_index.html_
```html

<ul ng-controller="learn-repeat">
    <li ng-repeat="name in names">
            {{ name}}
   </li>
</ul>
```

_app.js_

```javascript
angular.module('learn',[])
    .controller('learn-repeat',['$scope', function ($scope) {
$scope.names = ['rahul', 'nitin', 'dhannu', 'shivam', 'shakru', 'manoj', 'deepanshu', 'suraj', 'aslam'];
    }]);

```


- ng-repeat ki help se jitne names list mei items hai utne li tags ban jayenge.

- [Issue](https://github.com/vidur149/angular-todo/issues/1) **resolve karne se pehle yeh concept padho aur samjho.**
    - ng-repeat [en](https://www.w3schools.com/angular/ng_ng-repeat.asp), hi