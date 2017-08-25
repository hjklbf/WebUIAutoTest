#coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

dr=webdriver.Firefox()
# dr.maximize_window()
# time.sleep(50)
dr.get("http://www.yhd.com")
time.sleep(3)
dr.find_element_by_class_name('hd_login_link').click()
time.sleep(2)
dr.find_element_by_name('credentials.username').send_keys('')
# u'测Ab0'
dr.find_element_by_name('credentials.password').send_keys(u'Ab90@*')
dr.find_element_by_id('login_button').click()
time.sleep(3)
try:
    ActionChains(dr).move_to_element(dr.find_element_by_class_name('hd_login_name')).perform()
    time.sleep(1)
    get_text=dr.find_element_by_class_name("hd_login_name").text
    print get_text
    # dr.find_element_by_link_text(u'退出登陆').click()
    dr.find_element_by_class_name('hd_login_out').click()
    # dr.find_element_by_xpath(".//*[@id='global_login']/div[2]/a").click()
except:
    get_text=dr.find_element_by_class_name('error_tips').text
    print get_text

expect=u'测ab0'

if get_text==expect:
    print "success"
else:
    print "fail"

# dr.quit()