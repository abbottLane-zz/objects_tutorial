class Dog:
    '''
    Here the class of objects named "Dog" is defined. This class is basically a template
    for what any dog you create must look and behave like.

     As we can see below, any dog we create must have certain attributes:
        a name
        and age
        and a bark sound
    Attributes are defined under the __init__() funtion.
    '''
    def __init__(self, dog_name_input, dog_age_input):
        '''
        When you create a "Dog", you must define the name and age of the dog. The dog's bark
        sound is defined by default to be "bark", but you can use the Dog's member functions to change
        the bark sound to whatever you want.

        :param dog_name_input: The name of the dog you are creating
        :param dog_age_input: The age of the dog you are creating
        '''
        self.dog_name = dog_name_input
        self.dog_age = dog_age_input
        self.bark_sound = "bark!"

    # What follows below are member funtions of the class "Dog". You can tell it belongs to class "Dog" because
    # it is defined (hence the "def" keyword) underneath the class declaration "class Dog"
    # and it is tabbed (4 spaces) which is how python expresses that it belongs to this class.
    # Think like how when you take notes in school you type a title, then any sub-points related to that title
    # are typed in the next line, but tabbed underneath the title to show that it belongs to that title
    #
    # Member functions basically define behaviors of the dog, or make changes to the dog's behavior. The function
    # names are pretty descriptive, I think you can figure out what they do.
    def increment_dog_age(self):
        '''
        Adds one year to the dog's age
        '''
        self.dog_age = self.dog_age + 1

    def change_bark_sound(self, new_sound):
        '''
        Changes the set value of the dog's bark sound.
        :param new_sound: The sound you pass in, this is the new sound the dog will make
        from now on.
        '''
        self.bark_sound = new_sound

    def make_dog_bark(self):
        '''
        Makes the dog bark  in the terminal
        '''
        print(self.bark_sound)





class Cat:
    '''
    Here we have the definition for a class of objects named "Cat". I won't be typing as many comments
    here though, since this class mimics the "Dog" object above. You should be able
    to understand this class without my comments.
    '''
    def __init__(self, cat_name_input, cat_age_input):
        self.cat_name = cat_name_input
        self.cat_age = cat_age_input
        self.meow_sound = "maooow!"

    def increment_cat_age(self):
        self.cat_age = self.cat_age + 1

    def change_bark_sound(self, new_sound):
        self.cat_sound = new_sound