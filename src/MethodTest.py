
__author__="JimmyMo"
__date__ ="$Sep 1, 2013 12:42:00 AM$"

def testMethod(name, age):
    print name;
    print age;
    print "------------------end of "+__name__+".py------------------"

methodDelegate = testMethod;
methodDelegate("myname_delegate", 3)