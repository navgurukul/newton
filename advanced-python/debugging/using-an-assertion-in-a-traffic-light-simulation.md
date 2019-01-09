```ngMeta
name: using-an-assertion-in-a-traffic-light-simulation
```
# Using an Assertion in a Traffic Light Simulation
Say you’re building a traffic light simulation program. The data structure representing the stoplights at an intersection is a dictionary with keys 'ns' and 'ew', for the stoplights facing north-south and east-west, respectively. The values at these keys will be one of the strings 'green', ' yellow', or 'red'. The code would look something like this:


market_2nd = {'ns': 'green', 'ew': 'red'}
mission_16th = {'ns': 'red', 'ew': 'green'}
These two variables will be for the intersections of Market Street and 2nd Street, and Mission Street and 16th Street. To start the project, you want to write a switchLights() function, which will take an intersection dictionary as an argument and switch the lights.

At first, you might think that switchLights() should simply switch each light to the next color in the sequence: Any 'green' values should change to 'yellow', 'yellow' values should change to 'red', and 'red' values should change to 'green'. The code to implement this idea might look like this:


def switchLights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'

switchLights(market_2nd)
You may already see the problem with this code, but let’s pretend you wrote the rest of the simulation code, thousands of lines long, without noticing it. When you finally do run the simulation, the program doesn’t crash—but your virtual cars do!

Since you’ve already written the rest of the program, you have no idea where the bug could be. Maybe it’s in the code simulating the cars or in the code simulating the virtual drivers. It could take hours to trace the bug back to the switchLights() function.

But if while writing switchLights() you had added an assertion to check that at least one of the lights is always red, you might have included the following at the bottom of the function:


assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight)
With this assertion in place, your program would crash with this error message:


   Traceback (most recent call last):
     File "carSim.py", line 14, in <module>
       switchLights(market_2nd)
     File "carSim.py", line 13, in switchLights
       assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight)
❶ AssertionError: Neither light is red! {'ns': 'yellow', 'ew': 'green'}
The important line here is the AssertionError ❶. While your program crashing is not ideal, it immediately points out that a sanity check failed: Neither direction of traffic has a red light, meaning that traffic could be going both ways. By failing fast early in the program’s execution, you can save yourself a lot of future debugging effort.

