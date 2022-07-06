#https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/probability-calculator


import random
import copy

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)
                
        print(self.contents)
    def draw(self, balls):
        
        self.rtn = []
        count = 0
        rtn = ""
        for x in self.contents:
            count += 1
        if count <= balls:
            balls = count
        
        for x in range(balls):
            
            pick = random.randint(0,count -1)
            count -= 1
            
            self.rtn.insert(1, self.contents[pick])
            self.contents.pop(pick)
        return self.rtn
            
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    
    m = 0
    for x in range(num_experiments):
        found = 1
        new_hat = copy.deepcopy(hat)
        pick = new_hat.draw(num_balls_drawn)
        keys = expected_balls.keys()
                
        for key in keys:
            find = pick.count(key)
            expected = expected_balls[key]
            
            if find < expected:
                found = 0
        if found == 1:
            m +=1

        new_hat = ""
        
    result =  m / num_experiments 

    return result

    

hat = Hat(yellow=5,red=1,green=3,blue=9,test=1)
print(experiment(hat=hat, expected_balls={"yellow":2,"blue":3,"test":1}, num_balls_drawn=20, num_experiments=100))

hat = Hat(blue=3,red=2,green=6)
print(experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=1000))

