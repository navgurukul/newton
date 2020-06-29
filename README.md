# Newton - NG Curriculum

The complete structure of a course is explained here. This will help you create a new course in this repo :) You can also browse through other courses (every directory is a course) to understand more about the structure. 

# Structure of a course on SARAL
Every course has a seperate directory within this repo. Like the Python Course has a `python` directory, HTML Course has a `html` directory and so on.

## index.md?
This is the single most important file where you store the list of the contents in the course. Looking at following for an example:

### Course Structure
```bash
- index.md
- details
	- info.md
	- details.md
```

### index.md
```markdown
- introduction-to-programming.md
- hello-world.md
- introduction-to-loops
	- understanding-while-loops.md
	- understanding-break-conditions.md
- exercise-4.md
- exercise-5.md
```

These files have to exist in the parent directory. `introduction-to-loops` is a folder, and `understanding-while-loops.md` etc. are files that are to exist in the directory. 

The `details` directory has two main files, `info.md` and `details.md`

### info.md

This has some meta information of the course which is used when putting the course in the database. Here is a sample file

````markdown
```ngMeta
name: Basics of Programming using Python
type: python
daysToComplete: 45
shortDescription: We will learn the basics of programming using this course.
logo: http://google.com/logo.png
```
````

All the meta information about a course needs to be nested within a `ngMeta` tag in the markdown file.

### details.md
Leave this empty for now.

## Order of Exercises
The files can be named anything we want as curriculum developers. The order of files (the order in screenshot) is decided by the order written in `index.md` file.

The structure of `index.md` will be like this:

```
exercise-1.md
exercise-2.md
exercise-3/exercise-3.md
	- another-child-of-exercie-3.md
	- yet-another-child.md
```

Notice how `exercise-3` directory has three files inside while the tree structure in the screenshot only has 2 children under it. This is because here in `index.md` the file `exercise-3.md` is marked as a parent exercise while the other two are marked as child. Notice how they are intended in the above snippet. When the learner/student clicks on `Exercise 3` on SARAL the contents of `exercise-3.md` will be shown.


## Images in the Course

The images related to a course should exist within directory of the particular course. In case there are a lot of images it can also make sense to have exercise specific directories for images to make organising this easy.

*Note: Image paths in markdown file should be specific relative to the location of the file. You can use `..` to for accessing the contents of the directory above the directory of the markdown file. Similarly `../..` for two directories above.*

To learn Markdown visit [GitHub Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
