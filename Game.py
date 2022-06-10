import random
from xml.etree.ElementTree import parse

from soupsieve import select, select_one
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
        self.num_question = 0
        print('Inicciando el Juego de Preguntas')
        print('welcome to the Game {0}, yours level is {1}'.format(self.player.nick_name,self.player.id_category))
        print('answers the questions the correct form,')
        live = 1
        while live == 1:
            question = self.select_question()
            self.show_question(question)
            structured_question = 
            options = input(que)




        def show_question(question):
            print("{} /n {} /n {}".format(self.player.nick_name,))
    
    
    def load_questions(self):
        xml_questions = parse('questions.xml') 
        for question in xml_questions.iterfind('question'):
            temp_question = Question()
            temp_question.id = int(question.findtext('id'))
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

    def round(self, category):
        for question in self.list_questions:
            if question.id_category == category:
                self.selected_questions.append(question)
        

    def select_question(self):
        num = random.randint(1,len(self.list_questions))
        for item in self.list_questions:
                if item.id == num:
                    if item.id_category == self.player.id_category:
                        return item
                    


    def prueba(self, category):
        num = random.randint(1,len(self.list_questions))
        if self.num_question != 4:
            for item in self.list_questions:
                if item.id == num:
                    if item.id_category == category:
                        print(item.description)
                        self.num_question +=1
        else:
            if self.player.score == 5:
                self.num_question = 0
                self.player.category = 2
            

            

if __name__ =='__main__':
    player = Player()
    player.id = 1
    player.nick_name = 'pater'
    game_1 = Game(player)
    print(game_1.select_question())

    
    
    



    