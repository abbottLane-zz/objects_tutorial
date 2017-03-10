"""
Instructions:

From pycharm, you can run this script by right-clicking in the text area, and
selecting the 'Run Bennett' option with the green arrow next to it.

I'm putting some basic exercises on this script to get you warmed up. Wherever your pycharm edito shows a red squiggly,
it means something is wrong with the code. Fix it in a way that conforms with the instructions
in the nearby comment.
"""

# Basic maths
x = 5
y = 9
answer =  # using only x and y variables above, make "answer" equal 40
print ("Answer equals: " + str(answer))

# Classes
#   One of the most useful paradigms in programming is the 'object oriented' paradigm.
#   This just basically means we construct "objects" with code, and we can define the objects behaviors
#   somewhere else, and then build them and invoke those behaviors elsewhere.
#
#
#   For example, I defined some objects (or classes) in the file named "Classes.py". Take a look
#   at that file and try to figure out whats going on there.
#
#   Below, I will use the classes I defined in the Classes.py file
from Classes import Dog,Cat

fido = Dog("Fido", 23)
james_the_dog = Dog("James", 2)

print("Fido says: " + fido.make_dog_bark())
print("James says: "+ james_the_dog.make_dog_bark())
print("James is " + str(james_the_dog.dog_age) + " years old") # I wrapped the age in the str() function because age is a number, and you can only print out text to the console, so this forces the number to become text.

# Change the way james barks
james_the_dog.change_bark_sound("wooooof")
print("Now james says: " + james_the_dog.make_dog_bark())

### Assignement: Make Fido bark like this "quack!!"
### Assignment: Make a Cat named bernard, and use the print() function (used above) to
###    see what sound a cat makes. Try to change the sound a cat makes.
### Assignment: go to the Classes.py page and make a Snake class. Then make a Helicopter one.
###    remember that attributes of the object are defined under the __init__() function, while behaviors
###    of the objkect are defined as functions of the object.
###    Think about: what behaviors could you define for a helicopter? Make a beeping sound? Fly away? Rev engine?