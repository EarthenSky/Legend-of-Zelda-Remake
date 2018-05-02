## Legend-of-Zelda-Remake

This is a scaled down "remake version" of the Legend of Zelda (1986)


## Project Structure

While designing this project structure I used (https://hiltmon.com/blog/2013/07/03/a-simple-c-plus-plus-project-structure/) as inspiration.  Here is a simple explanation of all the important folders.

**bin:** This folder (meaning binary) holds all the executables or bianary files.

**docs:** This folder is for all extra documentation on the project.

**resc:** This folder is for any resources, images, sprite-sheets, maps, or sounds.

**src:** This folder contains all the source code for the project, being all the scripts and the code.

**test:** This folder contains all test code.


## Documentation

When writing test files or any extra documentation, write your initials at the end of all files like so.

```
camera_physics_GS.txt
collision_math_CS.txt
```


## General Code Style Guidelines

Some basic rules to follow when writing code:

- Write all variables, classes, and functions with underscores between the names like so
```
this_is_a_function_with_a_name_that_is_too_long()
```
No camelCase variable names.

- Comments should be punctuated properly (i.e includes a capital letter and a period.)
```
# This print statement tells the user the location that they have just entered.
print "Welcome To the Abyss."
```
Try to place comments either in front of blocks of code that share similar qualities, or two spaces after a line of code.

- Don't let a line of code go over 70-100 characters.  Pretty much if it is going off the screen, use a variable and make it two lines.

- Write any class member variables with an \*m_\* infront of them, or just an \*\_\* infront of them if they are not being accessed outside of the class.  The \*m_\* and \*\_\* tell other users which variables shouldn't be accessed or changed **outside of the class**, though it doesn't stop them.
```
class foo:
    """This class holds a name that can be accessed and a secret number that should not be accessed."""
    def __init__(self, name, secret_number):
        self.m_name = name
        self._secret_number = secret_number
```

- Any variable that isn't being modified is called a **constant**.  If you ever make a constant name it in all caps like so:
```
SCREEN_WIDTH = 600
FPS = 120
```


## Other Notes

- A function in a class is called a method.
- This is cool (http://zelda.speedruns.com/loz/generalknowledge/item-drops-chart)
- Use this for mechanics reference (https://www.youtube.com/watch?v=4bt5VHG3Jpw)
- Use this for finding assets (https://www.spriters-resource.com/nes/legendofzelda/sheet/8366/)
- NES default resolution is 256x224.
