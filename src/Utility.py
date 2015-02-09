import math

class Utility(object):
    # utility function options: 0-1, hinge, square, exponential, logistic
    function = None 
    fn_type =  "0-1"

    def __init__(self, fun_type, para):
        if fun_type.find("0-1") >= 0:
            self.fn_type = "0-1"
            self.function = Zero_one(para)

        elif fun_type.find("hinge") >= 0:
            self.fn_type = "hinge"
            self.function = Hinge(para)

        elif fun_type.find("square") >= 0:
            self.fn_type = "square"
            self.function = Square(para)

        elif fun_type.find("exp") >= 0:
            self.fn_type = "exp"
            self.function = Exponential(para)
    
        elif fun_type.find("log") >= 0:
            self.fn_type = "log"
            self.function = Logistic(para)
                
        else:
            print "Undefined utility function", fun_type
            exit(-5)

    def get_utility(self, x):
        print self.function.getUtility(x)
        return self.function.getUtility(x)

class Zero_one(): 
    # if (x > w) 1
    # else 0
    w = 0   
    def __init__(self, w):
        self.w = w;

    def getUtility(self,x):
        
        if (x <= self.w): 
            return 1
        else:
            return 0


class Hinge():
    # max {1 - wx, 0}
    w = 0
    def __init__(self, w):
        self.w = w
                    
    def getUtility(self, x):
        hinge = 1/self.w * 1.0
        if ( x > hinge ):
            return 0
        else:
            return (1 - self.w * x)

class Square():
    # (1 - wx)^2
    w = 0
    def __init__(self, w):
        self.w = w
        
    def getUtility(self, x):
        hinge = 1/self.w * 1.0
        if ( x > hinge ): 
            return 0;
        else:
            return (1 - self.w * x) * (1 - self.w * x)

class Logistic():
    # (ln 2)^(-1) ln(1 + e^(-wx))
    w = 0
    def __init__(self, w):
        self.w = w

    def getUtility(self, x):
        return math.log(1 + math.exp(-self.w * x), 2)

class Exponential():
    
    def __init__(self, w):
        self.w = w

#    def getUtility(self, x):

