```ngMeta
name: Part V StopWatch
completionMethod: facilitator
```

# Part V StopWatch

- Agar hum apni counter app mei counter ki value her 1 second mei 1  se increment kare to stopwatch app ban jayegi. 

- Jaise hum JS mei aisa karne ke liye **setInterval** ka use karte hai ussi tarah angularJs mei $interval object ka use hota hai. Humei $scope, $window ke jaise **$interval** ko apne controller mei **inject** karna hoga.

```javascript
	var interval = $interval(do_something, 2000)
	// aisa karne se do_something function her 2000ms yaani her 2s per call hoga.
```
Aur JS ke **clearInterval** ki jagah hum **$interval.cancel(interval_variable)** use karte hai. Jaise,
	**$interval.cancel(interval);**

- Aapko ab neeche diye gaye issues resolve karne hai:

- [Issue 1](https://github.com/vidur149/angular-multifunctional/issues/4)
- [Issue 2](https://github.com/vidur149/angular-multifunctional/issues/5)

