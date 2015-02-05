class Utility(object):
    # utility function options: 0-1, hinge, square, exponential
    function = None 
    

    def __init__(self, function):
        
        self.function = Zero_one(5)
        

    def get_utility(self, x):
        print self.function.getUtility(x)


class Zero_one(): 
    # if (x > w) 1
    # else 0

    w = 0   
    def __init__(self, w):
        self.w = w;

    def getUtility(self,x):
        
        if (x <= self.w): 
            return 1
        return 0


class Hinge():
    def __init__(self):
                
    def getUtility(self, x):
        

class Square():
    # (1 - wx)^2

    def __init__(self, w):
        self.w = w;
        
    def getUtility(self, x):
        hinge = 1/self.w
        if ( x > hinge ) 
            return 0;
        else:
            return (1 - self.w * x) * (1 - self.w * x)

class Exponential():
    def __init__(self):

    def getUtility(self, x):

