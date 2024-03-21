# Please refer to the README.txt file for the program description

# ==================    CODE    ==================================
class Course:
    """Create a Course class with class variables 
    
    > name
    > contact_website
    > head_office
    
    it has a class method contact_details that prints out the contact_website
    variable
    
    it also contains a head_office method that prints out the head office location
    """
    name = "Fundamentals of Software Engineering"
    contact_website = "www.hyperiondev.com"
    head_office = "Cape Town"

    # method to print contact details
    def contact_details(self):
        """This method proints out the contact website variable"""
        print("Please contact us by visiting", self.contact_website)

    # 1. Add another method in the Course class that prints the head
    # office location: Cape Town
    def head_office_location(self):
        """method that prints out the head office location"""
        print(f"The head office is in: {self.head_office}")


# 2. Create a subclass of the Course class named OOPCourse
class OOPCourse(Course):
    """This class is a sub class of the parent Course class and it inherits from it
    it takes 2 arguments when initializing
    
    > description
    > trainer
    
    it has a class method trainer_details that prints out course description and
    trainer information
    
    as well as a show_course_id function that prints out the course ID number
    """

    # 3. Create a constructor that initializes the following attributes and assigns these values:
    #--- "description" with a value "OOP Fundamentals"
    #--- "trainer" with a value "Mr Anon A. Mouse"
    def __init__(self, description, trainer):
        self.description = description
        self.trainer = trainer

    # 4. Create a method in the subclass named "trainer_details" that prints what the 
    # course is about and the name of the trainer by using the description and trainer
    # attributes.
    def trainer_details(self):
        """prints out course description and trainer information"""
        print(f"""\nCourse name : {self.description}
    \nThis course was made to helping students learn everything about OOP:
    > Classes
    > Class inheritance
    > Class methods
    \nThe name of the trainer is {self.trainer}
        """)

    # 5. Create a method in the subclass named "show_course_id" that prints the ID number
    # of the course: #12345
    def show_course_id(self):
        """function that prints out the course ID number"""
        print("Course ID: #OOP24846")



# 6. Create an object of the subclass called course_1 and call the following methods
# contact_details
# trainer_details
# show_course_id

course_1 = OOPCourse(description="OOP Fundamentals", trainer="Mr Anon A. Mouse")
course_1.contact_details()
course_1.trainer_details()
course_1.show_course_id()