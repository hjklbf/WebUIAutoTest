#coding=utf-8
from Tools.Tools import Tools

class Yhdlogin():
    def __init__(self):
        self.instance=Tools()

    def login(self,username,password):
        # self.instance.openBrower("http://www.yhd.com/")
        # self.instance.wait(3)
        self.instance.clickEvent("class_name","hd_login_link")
        self.instance.wait(3)
        self.instance.inputEvent("name","credentials.username",username)
        self.instance.inputEvent("name","credentials.password",password)
        self.instance.clickEvent("id","login_button")
        self.instance.wait(2)
        try:
            get_text=self.instance.getText("class_name","hd_login_name")
            self.instance.moveElement("class_name","hd_login_name")
            self.instance.clickEvent("class_name","hd_login_out")
        except:
            get_text=self.instance.getText("class_name","error_tips")

        return get_text

        # if get_text==expect:
        #     print "success"
        #
        # else:
        #     print "fail"


        # self.instance.wait(3)
        # self.instance.closeBrower()
