#coding=utf-8

from xml.dom import minidom

class Readxml():
    def readXml(self,onenode,twonode):
        root=minidom.parse("../DataShare/yhd.xml")
        firstnode=root.getElementsByTagName(onenode)[0]
        try:
            secondnode=firstnode.getElementsByTagName(twonode)[0].firstChild.data
        except:
            secondnode=""
        return secondnode
#
# p=Readxml()
# print p.readXml()