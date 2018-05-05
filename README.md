## Pokemon Wave Blue

This is a scaled down and remade version of Pokemon Leaf Green or Fire Red, with a few small changes to make grinding more bearable and reduce total play-time.


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

- Write all variables and functions with underscores between the names like so
```
this_is_a_function_with_a_name_that_is_too_long()
```
Only **classes** are written in CamelCase. *(First letter is uppercase)*

- Comments **should** be punctuated properly (i.e includes a capital letter and a period) and be one space after the # character.
```
# This print statement tells the user the location that they have just entered.
print "Welcome To the Abyss."
```
Try to place comments either in front of blocks of code that share similar qualities, or two spaces after a line of code.

- Don't let a line of code go over 70-100 characters.  Ever!  Pretty much if it is going off the screen, use a variable to make it two lines.

- Write any class member variables with either an \*m_\* infront of them, or an \*\_\* infront of them if they are not being accessed outside of the class.  The \*m_\* and \*\_\* tell other users which variables shouldn't be accessed or changed **outside of the class**, although it doesn't stop them.
```
class NumberWithName:
    """This class holds a name that can be accessed and a secret number that should not be accessed."""
    def __init__(self, name, secret_number):
        self.m_name = name
        self._secret_number = secret_number
```

- Any variable that isn't being modified is called a **constant**.  If you ever make a constant name it in all caps like so:
```
SCREEN_WIDTH = 600
FPS = 120  # This is the default frames per second for the game.
```
Always favor making a constant instead of placing a number in the middle of a function.  Reason:
```
# Updates the position of my_rect.
my_rect = that_object.convert_to_rect(100, 300, my_rect[0], my_rect[1], 8)
```
What does 8 mean?  The comment doesn't help either.

## Other Notes

- A function in a class is called a method.
- GBA screen size is 240px x 160px.
- Use this for the assets ( https://www.spriters-resource.com/game_boy_advance/pokemonfireredleafgreen/ ) 
- Here is a speed run to use for mechanics examples ( https://www.youtube.com/watch?v=fAWgVLz3OZo )
- Here is the gen 1 pokemon capture rate algorithm ( https://www.dragonflycave.com/mechanics/gen-i-capturing )
- Some pokemon stat algorithms ( https://bulbapedia.bulbagarden.net/wiki/Statistic ), we can just use the base stats for each pokemon.
