#coding=UTF-8
__author__ = 'Administrator'

class Student():

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print '%s: %s' % (self.name, self.score)

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_name(self, name):
        self.__name = name

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score =score
        else:
            raise ValueError('bad score')


bart = Student('Bart Simpson', 99)
bart.set_name('Neil')
bart.set_score(88)
print bart.get_name()
print bart.get_score()



