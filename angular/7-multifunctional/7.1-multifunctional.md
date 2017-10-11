```ngMeta
name: Ui-Router Continued
completionMethod: facilitator
```
# Ui-Router Continued

- Aapne tutorial mei notice kiya hogi ki **"hello world"** app mei koi controller use nhi ho raha. Aur **template** keyword ke aage **pura Html** likha hua hai. Magar aisa jaruri nahi hai ki aapki app mei koi controller na ho aur Html bhi chota sa ho. 

```javascript

var homeState = {
    name: 'homestate',
    url: '/home',
    templateUrl: 'templates/home.html',
    controller: 'mainController'
};

```

- Aap state define karte hue ye bhi bata sakte ho ki uss state ko **konsa controller** use karega.

- Aur aap yeh bhi bata sakte ho ki **konsa template** use hoga. Upar wale example mei, angular, templates folder mei **home.html** file ko **homeState** ke template ki tarah use karega.

- Ab aapko routing ka use karke jo aapne **3 apps** banayi thi( stopwatch, todo aur weather) unhe **ek app** mei dalna hai.

- Aapki aap mei neeche diye gaye cheezein honi chahiye.
    - Main page par teeno apps ke naam aana chahiye. 
	- /stopwatch par stopwatch app open honi chahiye
	- /weather par weather app.
	- /todo par todo app.
	- Inn teeno apps par ek back button bhi add karo, jisse click karne par home page khulna chahiye.

Note:- Aapki final app mei [iss](http://vidur149.github.io/angular/angular-multifunctional/) app ke saare features hone chahiye. Magar aisa jaruri nhi hai ki wo ekdum iss app jaisi dekhe.