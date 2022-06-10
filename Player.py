import string


class Player:
    
    def __init__(self):
        self.__id_player: int = 0
        self.__nick_name: string = ""
        self.__score: int = 0
        self.__id_category: int = 0

    @property
    def id_player(self):
        return self.__id_player

    @id_player.setter
    def id_player(self, value):
        self.__id_player = value

    @property
    def nick_name(self):
        return self.__nick_name

    @nick_name.setter
    def nick_name(self, value):
        self.__nick_name = value

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        self.__score = value

    @property
    def id_category(self):
        return self.__id_category

    @id_category.setter
    def id_category(self, value):
        self.__id_category = value
        

