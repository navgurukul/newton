```ngMeta
name: Mera code kahan raj karta hai aur kahan nahi?
```

- Defining variables inside/outside functions. How does it change?

var taskListGlobal = ['Teach students', 'Cook Food', 'Study', 'Give interview'];

function printList() {
        var taskListLocal = ['Drink milk', 'Drink water'];
        //taskListGlobal accessible
        for (var i = 0 ; i < taskListGlobal.length; i++) {
                console.log(taskListGlobal[i]);
        }        
}
printList()

//taskListLocal not accessible 
//This will throw error: Uncaught ReferenceError: taskListLocal is not defined
for (var i = 0 ; i < taskListLocal.length; i++) {
        console.log(taskListLocal[i]);
}