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

def get_courses():
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

    return id_list

for i in range(100):
    id_list = get_courses()
    random_id = random.choice(id_list)
    print get_exercises(random_id)
