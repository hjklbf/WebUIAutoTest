#coding=utf-8
from selenium import webdriver
import time

from selenium.webdriver.common.action_chains import ActionChains


class Tools():

    def __init__(self):
        self.driver=webdriver.Firefox()
        self.wait(2)

    def wait(self,number):
        time.sleep(number)

    def openBrower(self,url):
        self.driver.get(url)
        self.wait(2)

    def closeBrower(self):
        self.driver.quit()

    def locationElement(self,type,value):
        if type=='id':
            return self.driver.find_element_by_id(value)
        elif type=='name':
            return self.driver.find_element_by_name(value)
        elif type=='class_name':
            return self.driver.find_element_by_class_name(value)
        elif type=='css':
            return self.driver.find_element_by_css_selector(value)
        elif type=='xpath':
            return self.driver.find_element_by_xpath(value)
        elif type=='link_text':
            return self.driver.find_element_by_link_text(value)
        elif type=='partial':
            return self.driver.find_element_by_partial_link_text(value)

    def clickEvent(self,type,value):
        self.locationElement(type,value).click()

    def inputEvent(self,type,value,sendkeys):
        return self.locationElement(type,value).send_keys(sendkeys)

    def getText(self,type,value):
        return self.locationElement(type,value).text

    def selectWindow(self,window_name):
        all=self.driver.window_handles
        return self.driver.switch_to.window(all[window_name])

    def switchAlert(self,):
        pass

    def switchFrame(self,type,value):
        self.driver.switch_to.frame(self.locationElement(type,value))

    #鼠标悬停弹框
    def moveElement(self,type,value):
        ActionChains(self.driver).move_to_element(self.locationElement(type,value)).perform()






