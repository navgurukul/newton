```ngMeta
name: absolute-vs-relative-paths
completionMethod: manual
```
# Absolute vs. Relative Paths
There are two ways to specify a file path.

An absolute path, which always begins with the root folder

A relative path, which is relative to the program’s current working directory

There are also the dot (.) and dot-dot (..) folders. These are not real folders but special names that can be used in a path. A single period (“dot”) for a folder name is shorthand for “this directory.” Two periods (“dot-dot”) means “the parent folder.”

Figure 8-2 is an example of some folders and files. When the current working directory is set to C:\bacon, the relative paths for the other folders and files are set as they are in the figure.

<!-- ![image](assets/000032.jpg)
 -->
The relative paths for folders and files in the working directory C:\bacon

The .\ at the start of a relative path is optional. For example, .\spam.txt and spam.txt refer to the same file.