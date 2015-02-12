import matplotlib.pyplot as plt
import ast

if __name__ == "__main__":

   total = 0
   hist_dist = [0 for i in xrange(10)] 
   for i in xrange(1,11):
       #/Users/tiffany/d-picker/log
       fh = open("/Users/tiffany/d-picker/log/greedy/log/" + str(i)) 
       serve_count = []
       count = 0
       for line in fh:
           if line.find("[") >= 0:
               l = ast.literal_eval(line.strip())           
               serve_count += [(count, len(l))]
               count += 1
       
       serve_count.sort(key = lambda x:x[1])
       
       ct =  map(lambda x: x[1], serve_count)
       hist = [x/(sum(ct)*1.0) for x in ct]

       hist_dist = [hist[i] + hist_dist[i] for i in xrange(10)]   
       fh.close()
   hist_dist = [x/10.0 for x in hist_dist]
   plt.bar([i for i in xrange(10)], hist_dist)
   plt.show()
