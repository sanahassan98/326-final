#! /usr/bin/env python
"""This program is designed to parse through a set of flash cards for the user studying.
    
    INST326 Final Project
    """
import re
import sys
from argparse import ArgumentParser
from pprint import PrettyPrinter
pp = PrettyPrinter()
class Flash:
    
    """This class stores the individual questions and answers for each flash card and gets user input.
    
    Attr:
    cards (list): all the flash cards
    individ_cards (list): each individual card
    """
    def __init__(self, path):
        self.cards = []
        self.path = path
        
        
    def get_text(self):
        text = ''
        with open(self.path, "r", encoding = "utf-8") as f:
            text = f.read()
        return text
    def split_text_into_cards(self, text):
        individ_cards = text.split('End"')
       
        for maybe_card in individ_cards:
            question_re = re.compile(r'Question:\s(.+)')
            answer_re = re.compile(r'Answer:\s(.+)')
            
            maybe_question = question_re.search(maybe_card)
            maybe_answer = answer_re.search(maybe_card)
           
            if maybe_question and maybe_answer: 
                question = maybe_question.group(1)
                answer =     maybe_answer.group(1)
                card = Card(question, answer)
                self.cards.append(card)
              
        return self.cards
    '''
    +------------------------------+
    |  question: bla bla           |
    |  what is your answer:        |
    |            some answer       |
    '''
    def go_thru(self, cards):
        for card in cards:
            print('+' + ('-'*60) + '+')
            question_text = f'question; "{card.question}"'
            print(f'| {question_text:<59}|')
            answer_prompt = "Enter your answer:"
            user_answer = input(f'| {answer_prompt:<59}|\n| ')
            
            
            
            if user_answer == "cheat":
                print(f'answer: "{card.answer}"')
                user_answer = input("Enter your answer:\n")
                
            print(f'you answered "{user_answer}"')
            if user_answer == card.answer:
                print('Correct answer')

            else:
                print('Wrong answer')
                print(f'correct answer:"{card.answer}"')
                
    def go_thru_old_n_busted(self):
  
        """This function goes through each card, displays the question, gets user input, and lets them know if it is correct.
        Args:
        individ_cards (list): each individual card
        
        Prints:
        Each question
        User answer
        """
        with open(path, "r", encoding = "utf-8") as f:
            text = f.read()
            individ_cards = text.split('End"')
            for each_card in individ_cards:
                question = re.compile(r'Question:\s(.+)').search(each_card).group(1)
                print('Question: ', question)
                answer = re.compile(r'Answer:\s(.+)').search(each_card).group(1)
                user_answer = input("Enter your answer: ")
                print(user_answer)
                if user_answer == answer:
                    print('Correct answer')
                    break
                else:
                    print('Wrong answer')

class Card:
    """This class stores each question and answer.
    """
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

def main(f):
    """Calls other functions.
    Parameters:
    Path (str): the path of the text file that will be parsed.
    
    """
    
    flash = Flash(f)
    text = flash.get_text()
    
    cards = flash.split_text_into_cards(text)
    flash.go_thru(cards)
    
    return f

    
    

def parse_args(arglist):
    """ Parse command-line arguments. 
    Attr:
    parser
    parser.add_argument
    Returns:
    arglist"""
    parser = ArgumentParser(arglist)
    parser.add_argument("path")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    """Runs function.
    Attr:
    args
    Prints:
    Main function
    """

    args = parse_args(sys.argv[1:])
    print(main(args.path))
                    
