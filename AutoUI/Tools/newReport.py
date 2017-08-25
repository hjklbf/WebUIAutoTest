#coding=utf-8
import HTMLTestRunner

class NewReport():
    def newReport(self,suite):
        filepath="../Report/yhd.html"
        with open(filepath,"wb")as f:
            HTMLTestRunner.HTMLTestRunner(
                stream=f,
                verbosity=2,
                title=u"一号店测试报告"

            ).run(suite)
