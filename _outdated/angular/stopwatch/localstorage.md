```ngMeta
name: PartIII Local Storage
```
# Part III Local Storage

- **Page refresh** karne par aapki counter app mei counter ki value **0** ho jaati hai. Magar, hum chahte hai ki page refresh karne par bhi counter ki value 0 na ho.

- Aisa, karne ke liye humein counter ki value **store** karni hogi taaki page refresh karne par bhi value 0 na ho. Yeh hum **localstorage** ki madad se kar sakte hai.


- LocalStorage use karne ke liye humein **$window object** ka use karna hoga. Jaise humne **$scope inject** kiya tha, ussi tarah hum $window object ko bhi inject karenge taaki hum $window object ka localStorage use kar paye.

```javascript
angular.module('app ka naam', [])
	.controller('controller ka naam', ['$scope', '$window', function($scope, $window) {
		// controller logic
	}]);

 $window.localStorage.setItem('key', 'value'); 	// value store karne ke liye.
 $window.localStorage.getItem('key');		// value nikalne ke liye.
```


- Ab aapko [yeh](https://github.com/vidur149/angular-stopwatch/issues/3) issue resolve karna hai.
