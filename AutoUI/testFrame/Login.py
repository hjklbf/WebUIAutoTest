#coding=utf-8
import unittest
from Bussiness.yihaodian_login import Yhdlogin
from Tools.Readxml import Readxml
class Login(unittest.TestCase):
    def setUp(self):
        # print 'begin'
        self.instance=Yhdlogin()
        self.instance.instance.openBrower("http://www.yhd.com/")

        self.rx=Readxml()
        return self.rx
    def tearDown(self):
        # print 'end'
        self.instance.instance.closeBrower()

    def test01(self):
        # print 'test1'
        self.assertEqual(self.instance.login(
        self.rx.readXml("login","username1"),
        self.rx.readXml("login","password1"),),
        self.rx.readXml("login","expect1"))

    # def test02(self):
    #     print 'test2'

    if __name__=="__main__":
        unittest.main()