#!/usr/bin/python3
""" task 1 python almost a circle"""
import json


class Base:
    """Base class

    Raises:
        TypeError: checks for typeerror
        ValueError: checks for valueerror
        TypeError: checks for typerror
        ValueError: checks for valuerror
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ initialization of id"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def integer_validator(self, name, value):
        """ Integer validator, checks whether is
        a int, or is below 0

            Args:
                name (int): name of the instance
                value (int): value

            Raises:
                TypeError: checks typerror
                ValueError: checks valuerror
            """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        self.name = value

    def x_or_y(self, name, value):
        """x_or_y

        Args:
            name (int): name of the instance
            value (int): value

        Raises:
            TypeError: checks typerror
            ValueError: checks valuerror
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value < 0:
            raise ValueError(f"{name} must be >= 0")
        self.name = value

    @staticmethod
    def to_json_string(list_dictionaries):
        """Dictionary to JSON string

        Args:
            list_dictionaries: list to be converted

        Returns:
            _type_: class <list>
        """
        if list_dictionaries is None or list_dictionaries == []:
            return ("[]")
        else:
            json_string = json.dumps(list_dictionaries)
            return (json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save list_objs to a JSON file

        Args:
            list_objs: list of instances to be saved
        """
        if list_objs is None:
            list_objs = []

        json = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
        filename = "{}.json".format(cls.__name__)
        with open(filename, 'w+') as file:
            file.write(json)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == []:
            return []
        else:
            dictData = json.loads(json_string)
            return dictData

    @classmethod
    def create(cls, **dictionary):
        """ Creates a new instance of a class
        and updates it with update method

        Returns:
            instance with all attributes already set:
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(8, 2)
        if cls.__name__ == "Square":
            dummy = cls(2)
        dummy.update(**dictionary)
        return dummy
    
    @classmethod
    def load_from_file(cls):
        """_summary_
        """
        filename = f"{cls.__name__}.json"
        list = []
        try:
            with open(filename, "r") as f:
                list = cls.from_json_string(filename.read())
            for k, v in enumerate(list):
                list[k] = cls.create(**list[k])
        except:
            pass
        return list
