=================    practical_task_1    =======================

This program creates a parent class named Course
it has 3 class variables:
> name
> contact_website
> head_office

it also has 2 class methods:
* contact_details()
- This method prints out the contact details that use the contact_website
  variable

* head_office_location()
- This method prints out the head office location using the head_office
  variable

It then creates a subclass OOPCourse that inherits from the main class
Course

this subclass initializes with the 2 attributes
- description
- trainer

it also contains 2 class specific methods:
* trainer_details()
- This method prints out the description of the course as well as the
  trainer details using the 2 attributes in the class
  
* show_course_id()
- This method simply prints out the course ID number

#########    Final code

- The program creates an object course_1 from the subclass passing in
  the description and trainer arguments tp be initialized
- finally the course_1 calls on to the 3 methods to give the desired
  information to the user:
  > contact_details()
  > trainer_details()
  > show_course_id()

=================    method_override.py    =======================
This program creates a parent class Adult which uses 4 arguments

> name
> age
> hair_colour
> eye_colour

It then initializes the object created with the class with attributes
using the 4 arguments provided above

this class has a method
* can_drive()
- It prints out the object age and name attribute and that they can drive

then it creates a subclass Child inheriting from the Adult class.
This class hs the same method 
* can_drive()
- However this class method overrides the parent class method and it
  prints out the  object name and age attributes along with the cant
  drive

#########    Final code

creates a while loop for reusability if the user wants to keep checking
records

Requests user input for

> name
> age
> hair_colour
> eye_colour

checks if the age variable is over 18 in which case it creates an
adult_1 object from the Adult class and calls on to the can_drive method

If the age is below 18 in that case it creates the child_1 object from
the Child class and calls on to the can_drive method

Finally it creates a while loop to request user input if they want
to keep using the registry.
checks if the input is "yes" or "no" and makes a decision to keep
going or to shut the program down.

If the user input is not "yes" or "no" it keeps requesting user
input again until it is a "yes" or "no"