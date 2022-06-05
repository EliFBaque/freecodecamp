import copy
import random

class Hat:
    '''Initialize a new hat'''
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)
        
    def draw(self, num_balls):
        '''Draw a number of balls from the hat'''
        if num_balls > len(self.contents):
            return self.contents
        balls = []
        for i in range(num_balls):
            random_ball = random.randint(0,(len(self.contents)-1))
            balls.append(self.contents[random_ball])
            self.contents.remove(self.contents[random_ball])
        return balls
    
    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    '''Make x number of experiments with a hat'''
    count = 0
    for i in range(num_experiments):
        expected_copy = copy.deepcopy(expected_balls)
        hat_copy = copy.deepcopy(hat)
        colors_gotten = hat_copy.draw(num_balls_drawn)
        
        for color in colors_gotten:
            if (color in expected_copy):
                expected_copy[color] -= 1
        
        if (all(x <= 0 for x in expected_copy.values())):
            count += 1
            
    return count / num_experiments