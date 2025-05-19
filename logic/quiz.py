import os
from random import randint

from logic.question import Question


class Quiz:
    def __init__(self,path,number_of_questions):
        self.paths = os.listdir(path)
        self.questions = []

        if number_of_questions > len(self.paths):
            raise ValueError("Number of questions greater than the questions count")


        for i in range(number_of_questions):
            index = randint(0,len(self.paths)-1)
            self.questions.append(Question(self.paths[index]))
            self.paths.pop(index)

