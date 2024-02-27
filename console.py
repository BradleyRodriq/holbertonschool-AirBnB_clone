#!/usr/bin/python3
"""console.py"""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """command interpreter"""

    prompt = "(hbnb) "
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Place": Place,
        "Amenity": Amenity,
        "Review": Review
        }

    def emptyline(self):
        """Do nothing when empty line is received\n"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, arg):
        """EOF signal will exit the program (ctrl+D)\n"""
        print("")
        return True

    def do_create(self, arg):
        """
        Create a new class instance and prints its id.
        """
        if len(arg) == 0:
            print("** class name missing **")
        elif arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            instance = self.classes[arg]()
            instance.save
            print(instance.id)

    def do_show(self, arg):
        """Display string representation of a class instance"""
        objdict = storage.all()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg not in HBNBCommand.classes:
            print("** class doesn't exist")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg[1], arg[2]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(arg[0], arg[1])])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
