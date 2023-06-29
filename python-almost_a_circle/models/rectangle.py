#!/usr/bin/python3
"""Another class, rectangle this time"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from Base
    class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes attributes

        Args:
            width (int): Rectangle width
            height (int): Rectangle height
            x (int, optional): Width number. Defaults to 0.
            y (int, optional): Height number. Defaults to 0.
            id inherited from super().

        Return: nothing.
        """
        super().__init__(id)
        self.__width = width
        self.integer_validator("width", width)
        self.__height = height
        self.integer_validator("height", height)
        self.__x = x
        self.x_or_y("x", x)
        self.__y = y
        self.x_or_y("y", y)

    def area(self):
        """
        Area of the rectangle

        Return: area of the rectangle(width * height)"""
        return (self.__width * self.__height)

    def display(self):
        """
        Prints in stdout the Rectangle

        Returns: None
        """
        for y in range(self.__y):
            print()
        for h in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for w in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Returns a string representation of the
        self class

        Returns:
            Rectangle and its attributes
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height
        )

    def update(self, *args, **kwargs):
        """updates and assigns attributes to a
        variable number of arguments
        """
        if args:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for arg, attr in zip(args, attrs):
                setattr(self, attr, arg)
        elif kwargs:
            for k, v in kwargs.items():
                setattr(self, k, v)

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        self.integer_validator("width", value)
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        self.integer_validator("height", value)
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        self.x_or_y("x", value)
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        self.x_or_y("y", value)
        self.__y = value
