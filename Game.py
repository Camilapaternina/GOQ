import random
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
        print('Inicciando el Juego de Preguntas')
        print('welcome to the Game {0}, yours level is {1}'.format(self.player.nick_name,self.player.id_category))
        print('answers the questions the correct form,')
        print("preunta 1 ", self.select_question(1))
        print("preunta 2 ",self.select_question(2))
        #print(self.select_questions(self.player.id_category).id)
        
    
    
    def load_questions(self):
        xml_questions = parse('questions.xml') 
        for question in xml_questions.iterfind('question'):
            temp_question = Question()
            temp_question.id = question.findtext('id')
            temp_question.id_category = int(question.findtext('category'))
            temp_question.description = question.findtext('description')
            temp_question.options.append(question.findtext('option_1'))
            temp_question.options.append(question.findtext('option_2'))
            temp_question.options.append(question.findtext('option_3'))
            temp_question.options.append(question.findtext('option_4'))
            temp_question.answer = question.findtext('answer')
            self.list_questions.append(temp_question)
    
    def load_category(self):
        xml_categories = parse('categories.xml') 
        for category in xml_categories.iterfind('category'):
            temp_category = Category()
            temp_category.id = int(category.findtext('id'))
            temp_category.description= category.findtext('description')
            self.list_category.append(temp_category)

    def select_question(self, category):
        num = random.randint(0,len(self.list_questions)-1)
        question = self.list_questions[num]
        if question.id_category == category:
            if len(self.selected_questions) != 0:
                for item in self.selected_questions:
                    print(type(item.id))
            else:
                self.selected_questions.append(question)
                
        
        return question
            #
           # print(item)
               # if question.id == item.id:
               #     self.select_questions(category)
        
    

if __name__ =='__main__':
    player = Player()
    player.id = 1
    player.nick_name = 'pater'
    game_1 = Game(player)
    game_1.play_game()
    
    



    