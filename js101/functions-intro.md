```ngMeta
name: Ek baar karo! Anek baar karvao. Functions ka dhamaal
```

- Convert the print list to a function and perform different operations on list and print this list

function printList(listToPrint) {
        var listLength = listToPrint.length;
        var index = 0;
        while(index < listLength)
            console.log(listToPrint[i]);
            index = index + 1;
        }
}

var taskList = ['Teach students', 'Cook Food', 'Study', 'Give interview'];
taskList.push('Be honest');
printList(taskList)

taskList.splice(0, 1)
printList(taskList)