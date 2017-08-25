#coding=utf-8
import  unittest
from testFrame import Search,Login
from Tools.newReport import NewReport
from Tools.SendMail import SendEmail
class Test(unittest.TestCase):
    def testS(self):
        Tsuite=unittest.TestSuite()
        Tsuite.addTest(unittest.makeSuite(Search.Search))
        Tsuite.addTest(unittest.makeSuite(Login.Login))
        unittest.TextTestRunner(verbosity=2).run(Tsuite)
        new=NewReport()
        new.newReport(Tsuite)
        send=SendEmail()
        send.sendEmail('../Report/yhd.html')
if __name__=="__main__":
    unittest.main()




