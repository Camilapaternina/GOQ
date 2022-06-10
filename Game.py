from xml.etree.ElementTree import parse
from Category import Category
from Question import Question
from Player import Player

class Game:
    def __init__(self, player):
        self.list_questions = []
        self.list_category = []
        self.player = player
        self.selected_questions = []
        self.load_category()
        self.load_questions()

    def play_game(self):
        pass
    
    def load_questions(self):
        xml_questions = parse('questions.xml') 
        for question in xml_questions.iterfind('question'):
            temp_question = Question()
            temp_question.id = question.findtext('id')
            temp_question.id_category = question.findtext('category')
            temp_question.description = question.findtext('description')
            temp_question.options.append(question.findtext('option_1'))
            temp_question.options.append(question.findtext('option_2'))
            temp_question.options.append(question.findtext('option_3'))
            temp_question.options.append(question.findtext('option_4'))
            temp_question.answer = question.findtext('answer')
            self.list_questions.append(temp_question)
    
    def load_category(self):
        xml_categories = parse('categories.xml') 
        for category in xml_categories.iterfind('categories.xml'):
            temp_category = Category()
            temp_category.id = category.findtext('id')
            temp_category.category = category.findtext('category')
            self.list_category.append(temp_category)

    def select_questions(self, category):
        temp_questions = self.list_questions
        return temp_questions

if __name__ =='__main__':
    player = Player()
    player.id_player = 1
    player.nick_name = 'pater'
    player.category = 1
    game_1 = Game(player)
    game_1.play_game
    print(game_1.list_category[1].description)
    



    