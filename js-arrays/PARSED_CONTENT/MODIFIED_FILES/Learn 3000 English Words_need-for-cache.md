need-for-cache_key1
```python
import requests
import random

def get_exercises(course_id):
    print "Finding Exercises for course id :", course_id
    url = 'http://saral.navgurukul.org/api/courses/'+str(course_id)+'/exercises'
    resp = requests.get(url)
    jsonObject = resp.json()

    exercise_names = map(lambda exercise: exercise["name"], jsonObject["data"])
    '''
    I can write above line as following also:

    exercise_names = []
    exercises = jsonObject["data"]
    for exercise in exercises:
        exercise_names.append(exercise["name"])
    '''

    return exercise_names

def get_three_courses():
    print "finding list of all courses"
    url = 'http://saral.navgurukul.org/api/courses'
    resp = requests.get(url)
    jsonObject = resp.json()
    courses = jsonObject["availableCourses"]

    id_list = map(lambda course:course["id"], courses)
    '''
    I can write above line as following also:

    id_list = []
    for course in courses:
        id_list.append(course["id"])
    '''

    return id_list[:3]

for i in range(100):
    print "running loop to get exercises of a random course:", i
    id_3_courses = get_three_courses()
    random_course_id = random.choice(id_3_courses)
    exercises = get_exercises(random_course_id)
```

need-for-cache_key2
- need-for-cache_key3
- need-for-cache_key4
- need-for-cache_key5
- need-for-cache_key6
- need-for-cache_key7
