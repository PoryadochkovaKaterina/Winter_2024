'''Docstring for module'''
import sys
# from datetime import datetime
class CarClass:
    '''Docstring for CarClass'''
    def __init__(self, color, make, ctype):
        self.color = color
        self.make = make
        # self.model = model
        # self.year = year
        if 'Linux' == sys.platform:
            print('You are using Linux!')
        self.weight = self.get_weight(ctype)
    def get_weight(self, ctype):
        '''Docstring for get_weight'''
        if ctype == 1:
            return 2000
        return None
