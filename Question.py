
import string


class Question:

    def __init__(self):
        self.__id: int = 0
        self.__description: string = ""
        self.__options = []
        self.__answer: int = 0
        self.__id_category: int = 0

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

    @property
    def answer(self):
        return self.__answer

    @answer.setter
    def answer(self, value):
        self.__answer = value

    @property
    def id_category(self):
        return self.__id_category

    @id_category.setter
    def id_category(self, value):
        self.__id_category = value

    @property
    def options(self):
        return self.__options

    @options.setter
    def options(self, value):
        self.__options = value



        


