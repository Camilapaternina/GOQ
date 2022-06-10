
import string


class Category:

    def __init__(self):
        self.__id: int = 0
        self.__description: string = ""
    
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value
