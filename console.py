#!/usr/bin/python3
"""console.py"""
import cmd
import re


class HBNBCommand(cmd.Cmd):
    """command interpreter"""

    prompt = "(hbnb) "
    """classes = {}"""

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
