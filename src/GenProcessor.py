
__author__="JimmyMo"
__date__ ="$Aug 11, 2013 12:38:18 PM$"

from Webware.MiscUtils.DataTable import DataTable
class GenProcessor(object):
    def __init__(self):
        self.__metadataSet = DataTable(['name', 'age:int'])
        self.__newdataSet = DataTable()
        self.__metadataSet.append(['aaa', 80])
    
