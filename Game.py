from random import choice
from xml.etree.ElementTree import parse
import xml.etree.ElementTree as et

from sqlalchemy import values
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
       
    def save_game(self, player):
        file = 'result_games.xml'
        xml = et.parse(file)
        root = xml.getroot()
        game = et.Element('player')
        id_player = et.SubElement(game, 'id')
        id_player.text = str(player.id)
        nick_name = et.SubElement(game,"nick_name")
        nick_name.text = player.nick_name
        score = et.SubElement(game,"score")
        score.text = str(player.score)
        root.insert(1, game)
        xml.write(file, xml_declaration=True, encoding='utf-8')

    def play_game(self):

        print('Inicciando el Juego de Preguntas')
        print('welcome to the Game {0}, yours level is {1}'.format(self.player.nick_name,self.player.id_category))
        print('answers the questions the correct form,')
        count = 1
        self.round(self.player.id_category)
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
                    self.save_game(self.player)
                    break
            else:
                if self.player.id_category == 5 and count == 25:
                    print("Game Finished - Congratulations")
                    self.save_game(self.player)
                    break
                else:
                    self.player.id_category += 1
                    self.round(self.player.id_category)

if __name__ =='__main__':
    player = Player()
    player.id = 1
    player.nick_name = 'pater'
    game_1 = Game(player)
    game_1.play_game()

    
    
    



    