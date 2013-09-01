
__author__="JimmyMo"
__date__ ="$Aug 31, 2013 8:33:23 PM$"

list = [123, "abc", 1.23]
list.append('ni')
p = list.pop(0)
list.sort()
print list;
list.reverse()
list.insert(0, 'aaa')
print list.count('aaa')
print list;
print p;
print range(len(list))
for i in list:
    print i
for i in range(len(list)):
    print i
print "------------------end of "+__name__+".py------------------"
