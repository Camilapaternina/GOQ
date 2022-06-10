from operator import le
from random import choice
import re
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
        self.question = Question()
        self.load_category()
        self.load_questions()

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
            temp_question.answer = int(question.findtext('answer'))
            self.list_questions.append(temp_question)
    
    def load_category(self):
        xml_categories = parse('categories.xml') 
        for category in xml_categories.iterfind('category'):
            temp_category = Category()
            temp_category.id = int(category.findtext('id'))
            temp_category.description= category.findtext('description')
            self.list_category.append(temp_category)
    
    def show_question(self, question, num_question):
        msg = "{0}.{1} \n 1.{2} \n 2.{3} \n 3.{4} \n 4.{5} \n Type yours answer :".format(num_question, question.description, question.options[0], question.options[1], question.options[2], question.options[3])
        return msg 

    def round(self, category):
        for question in self.list_questions:
            if question.id_category == category:
                self.selected_questions.append(question)

    def select_question(self):
        question = choice(self.selected_questions)
        self.selected_questions.remove(question)
        return question
       
    
    def play_game(self):

        print('Inicciando el Juego de Preguntas')
        print('welcome to the Game {0}, yours level is {1}'.format(self.player.nick_name,self.player.id_category))
        print('answers the questions the correct form,')
        count = 1
        while self.player.id_category != 6:
            print(f"Level {self.player.id_category}  Player {self.player.nick_name} : {self.player.score} points")
            
            if len(self.selected_questions) != 0:
                self.question = self.select_question()
                option = int(input(self.show_question(self.question,count)))
            
                if option == self.question.answer:
                    print("correct answer")
                    self.player.score += 1
                    count += 1
                else:
                    print("incorrect answer \n Game Over")
                    break
            else:
                self.player.id_category += 1
                self.round(self.player.id_category)



if __name__ =='__main__':
    player = Player()
    player.id = 1
    player.nick_name = 'pater'
    game_1 = Game(player)
    game_1.round(1)
    game_1.play_game()

    
    
    



    