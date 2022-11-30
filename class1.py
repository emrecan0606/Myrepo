from unicodedata import name


class Person:

    def __init__(self,name):
        self.name=name

    def  pretty_name_print(self):
         print(self._name)
    def prettyNamePrint(self):
        print(self._name)        


class Student(Person):
  
  def __init__(self,name):
      super().__init__(name)
      self.username=username
      print("Constructing student with username{self.default_courses}")
  
  
  default_courses=["OOP","Mathematics"]

  

  def print_default_courses(self):
        print("Default courses of {self._name"} are : {self.print_deault_courses}")
  
   pass



p1=Person("Johnnnes")
s1=Person("adam","adam54")

print(s1)

s1.print_default_courses()
p1.print_default_courses()

print(p1)
print(p1._name)

print(s1)






            