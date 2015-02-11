from Utility import * 
import matplotlib.pyplot as plt
import random
if __name__ == "__main__":
    a = []
    for i in xrange(10000):
        a += [random.randrange(0, 6000)]    
    
    fn = Utility("0-1", 4000)
    zeroone = [fn.get_utility(i) for i in a]

    fn = Utility("hinge", 1/4000.0)
    hinge = [fn.get_utility(i) for i in a] 
    
    fn = Utility("square", 1/4000.0)
    square = [fn.get_utility(i) for i in a]

    fn = Utility("log", 1/2000.0)
    
    log = [fn.get_utility(i) for i in a]

    zo = plt.scatter(a, zeroone, color='b', s = 70)
    hi = plt.scatter(a, hinge, color = 'c')
    sq = plt.scatter(a, square, color= 'g')
    lo = plt.scatter(a, log, color='r')

    plt.axvline(x = 4000, color = 'k')
    plt.legend((zo, hi, sq, lo), ('zero-one', 'hinge', 'square', 'logistic'), loc='upper right', scatterpoints=1)
    plt.show()
