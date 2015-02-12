
if __name__ == "__main__":

   total = 0
   for i in xrange(1,11):
       #/Users/tiffany/d-picker/log
       fh = open("/Users/tiffany/d-picker/log/fifo/zerone/" + str(i)) 
       for line in fh:
           if line.find("Total score:") >= 0:
               utility = float([seg.strip() for seg in line.split(":")][1])
               total += utility

       fh.close()
   print total/10.0
