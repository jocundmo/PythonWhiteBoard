
__author__="JimmyMo"
__date__ ="$Aug 31, 2013 8:30:37 PM$"

class Employee(object):
    "This is documentation" #documentation
    count = 0 #static field
    def __new__(cls, who):
        print ("__new__ is called...")
        #return object;
        return object.__new__(Employee)
        #self.who = who
    def __init__(self, who):
        self.who = who
        print ("__init__ is called...")
        Employee.count += 1
        #
    def computeSalary(self, who):
        self.who = who
        
    def __repr__(self):
        return "aaabbbccc" + self.__metadataSet.__repr__();

    def __del__(self):
        print "------------------end of "+__name__+".py------------------"

class ComputerEngineer(Employee):
    
    pass
    