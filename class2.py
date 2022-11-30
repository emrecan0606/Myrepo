class PowerIterator:
    def __init__(self,max_value): 
        self.max_value=max_value
   
    def __iter__(self):
        self.n=0
        return self
    def __next__(self):
        if self.n<self.max_value:
            result=2**self.n #calculate result
            self.n +=1 #increase counter by one
            return result
        else:
            return StopIteration
        
        for p in PowerIterator(8):
            print(p)

            
            
            
            
iter_obj=iter(self)

while True:
    try:
        element=next(iter_obj)
        print(element)
    except StopIteration:
            print("I am done")
            break
                
    


class CollatzIteraator:
    def __init__(self,starting_number):
        self.starting_number=starting_number

   def __iter__(self):
        self.n=self.starting_number #resetting counter
        return self
   
   def __next__(self):
        if self.n==1:
              raise StopIteration
        else:
              if self.n %2 ==0:
                    #n is even
                    r=self.n
                    self.n=self.n//2
              else:
                    #n is odd
                    self.n=3*self.n+1
               return r     
for n in CollatzIteraator(3):
      print(n)        

def 
          

    
            

        
