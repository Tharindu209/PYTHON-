import random
class coin:
    
    def __init__(self):
        self.__state = 'head'
    
    def toss(self):
        if random.randint(0,1) == 0:
            self.__state = 'head'
        else:
            self.__state = 'tails' 
    
    def set_result(self,state):
        self.__state = state
    
    def get_result(self):
        return self.__state
