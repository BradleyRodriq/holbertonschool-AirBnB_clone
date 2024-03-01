## AirBnB Project: The Console 


![1_lqEaA1-6gGQhdLS3k8X0xw](https://user-images.githubusercontent.com/31927278/182706961-e087c64e-9d7b-40db-a931-67009dc34089.gif)


## General
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using wc
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

## BaseModel Class

- The BaseModel class serves as the foundation for other classes in the project. It provides basic functionality such as generating unique identifiers, tracking creation and modification times, and converting instances to dictionaries.

## Attributes
- id: A unique identifier generated using the uuid4() function.
- created_at: A datetime object representing the time when the instance was created.
- updated_at: A datetime object representing the time when the instance was last updated.

## Methods

- __init__(*args, **kwargs): Initializes a new instance of the BaseModel class. Accepts optional keyword arguments to set instance attributes.
- save(): Updates the updated_at attribute with the current datetime and saves the instance using the storage mechanism.
to_dict(): Returns a dictionary representation of the BaseModel instance, including its attributes and class name.
- __str__(): Returns a string representation of the BaseModel instance, displaying its class name, unique identifier, and attributes.






## HBNB Command Line Interface

- This is a command-line interface (CLI) for managing objects in the HBNB project. It allows users to interact with and manipulate instances of different classes such as BaseModel, User, State, City, Place, Amenity, and Review.


## Installation
- Clone the repository:

     git clone https://github.com/your_username/your_repository.git


- Navigate to the project directory:

         cd your_repository
- Run the console:

         ./console.py

## Object Manipulation Commands
create <class_name>: Create a new instance of the specified class.
show <class_name> <instance_id>: Display information about the specified instance.
destroy <class_name> <instance_id>: Delete the specified instance.
all [class_name]: Display information about all instances or instances of a specific class.
update <class_name> <instance_id> <attribute_name> "<new_value>": Update the specified attribute of the specified instance.
## Supported Classes
BaseModel: The base class for all other classes.
User: Represents a user.
State: Represents a state.
City: Represents a city.
Place: Represents a place.
Amenity: Represents an amenity.
Review: Represents a review.#Supported Classes

## Authors

- Bradley Rodriguez
- Christian Lopez