# Please read the README.txt for program description

# =======================    Classes/Methods    =======================

# Creates Adult class
class Adult():
    """This class initialise and requires these 4 argument inputs
    > name
    > age
    > hair_colour
    > eye_colour

    it initialise the arguments in to attributes of the same name for a 
    new object it creates

    It also contains a class method that prints out the name and age attributes
    and that they object(person) can drive
    """

    # Initializes the object in the class by using these arguments
    def __init__(self, name, age, hair_colour, eye_colour):
        self.name = name
        self.age = age
        self.hair_colour = hair_colour
        self.eye_colour = eye_colour

    # Creates a class method to say the person is old enough to drive
    def can_drive(self):
        """Prints out the object name and age attribute and that they can drive"""
        print(f"\n{name} is {age} and they are old enough to drive.")

# Creates a subclass Child
class Child(Adult):
    """This class inherits from the parent Adult class and requires these 
    same 4 argument inputs:
    > name
    > age
    > hair_colour
    > eye_colour

    it initializes the arguments in to attributes of the same name for a 
    new object it creates

    It also contains a class method that prints out the name and age attributes
    and that the object(person) can't drive"""

    # Initializes the object in the class by using these arguments
    def __init__(self, name, age, hair_colour, eye_colour):
        super().__init__(name, age, hair_colour, eye_colour)

    # Creates a class method to say the person is not old enough to drive
    def can_drive(self):
        """Prints out the name and age attributes of the object and that
        they can't drive"""
        print(f"\n{name} is {age} and they are to young to drive.")

# =======================    Program code    =======================

# Creates a while loop for person registry process
new_person = True
while new_person:
    print("\nPlease answer a few question so we can create a profile for the person.")

    # Requests input for all the arguments that the class will need
    name = input("\nPlease provide a name?: ")
    age = int(input("Please provide the age?: "))
    hair_colour = input("What the hair colour?: ")
    eye_colour = input("What is the eye colour?: ")

    # checks the age of the person if 18 or over it creates an adult class object
    # and if under 18 it creates a child object
    # which ever object it creates it calls the can_drove method
    if age >= 18:
        adult_1 = Adult(name, age, hair_colour, eye_colour)
        adult_1.can_drive()
    else:
        child_1 = Child(name, age, hair_colour, eye_colour)
        child_1.can_drive()

    # creates a loop to ask if user wants to continue with a new entry
    # if the answer is not a "yes" or "no" it doesn't accept input and keeps asking
    # until the answer is a yes or a no
    wrong_input = True
    while wrong_input:
        user_choice = input("\nWould you like to enter another person? (yes/no): ").lower()
        if user_choice == "yes":
            wrong_input = False
        elif user_choice == "no":
            new_person = False
            wrong_input = False
            print("Thank you for using the registry \nYou have closed the app")
        else:
            print("Invalid input please try again")
