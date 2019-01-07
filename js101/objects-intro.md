```ngMeta
name: Objects ke baare mein seekhte hain
```

- introducing key, value concept and how to define an object and access its properties

//Concept of objects
var task = {
        'id' : 1,
        'task': 'Complete the JS course',
        'status': 'Pending'
}
console.log(task)
console.log(task['id'])

//Create a list of objects
taskList = [{
                'id' : 1,
                'task': 'Complete the JS course',
                'status': 'Pending'
        },
        {
                'id' : 2,
                'task': 'Complete the CSS course',
                'status': 'Pending'
        },
        {
                'id' : 3,
                'task': 'Cook the food',
                'status': 'Complete'
        }]
var listLength = taskList.length;
var index = 0;
while(index < listLength)
        console.log(taskList[i]);
        index = index + 1;
}
