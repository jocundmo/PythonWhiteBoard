import sys
import StringTest
import ListTest
import LoopTest
import MethodTest

from ClassTest import Employee, ComputerEngineer
from Webware.MiscUtils import DataTable
#from GenProcessor import GenProcessor
__author__="JimmyMo"
__date__ ="$Aug 11, 2013 12:22:07 PM$"

if __name__ == "__main__":
    #list.append('ni')
#    gen = GenProcessor()
#    object_dir = dir(gen);
#    object_dict = gen.__dict__
#    print 'aaa'
#    print gen.__hash__()
#    print object_dir;
#    print object_dict;
#    print gen;
#    print 'bbb'
    #print gen.__dict__;
    #print gen._metadataSet;
    #print sys.path
    e1 = Employee("employee1");
    #print dir(e1)
    #print e1.__dict__['who']
    print e1.__class__ # <class 'ClassTest.Employee'>
    print e1.__class__.__bases__ # (<type 'object'>,)
    print e1.__class__.__class__ # <type 'type'>
    print dir(e1.__class__)
    print e1.__class__.__bases__.__class__.__bases__.__class__
    print e1.who
    e1.computeSalary("set salary")
    print e1.who;
    del(e1);
    e2 = ComputerEngineer("computerEngineer222")
    print ComputerEngineer.__bases__
    print e2.__class__
    #print e2;
    print "---e2.__class__---"
    #print e2.who
    #e2.__bases__
    del(e2);
    #e1.computeSalary("e2")
#    print Employee.count;
#    print Employee.__module__
#    print Employee.__name__
    #dir(Employee)
    #print Employee.__dict__
    #print NoDefault.__module__
    table = DataTable.DataTable(['name', 'age:int'])
    table.append(['John', 80])
    table.append({'name': 'John', 'age': 80})
    print table

    MethodTest.methodDelegate("myName", 3)
