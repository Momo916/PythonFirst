#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# import os,time,unittest
# from appium import webdriver
#
# PATH=lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))
# desires_caps={}
# desires_caps['platformName']='Android' #设备系统
# desires_caps['platformVersion']='6.0.1' #设备系统版本
# desires_caps['deviceName']='' #设备名称，通过adb devices查看
#
# desires_caps['app']=PATH(r"E\test\**.apk")
# desires_caps['appPackage']='***' #apk包名
# desires_caps['appActivity']='***.activity.***Activity' #apk的launcherActivity
#
# driver=webdriver.Remote("http://localhost:4723/wd/hub",desires_caps)
# time.sleep(5)

# from appium import webdriver
# from selenium.webdriver.common.keys import Keys
# from time import sleep
# import sys
# import HTMLTestRunner
#
# browser =webdriver.Ie()
#
# def setUp(self):
#     self.driver=webdriver.ie()
#     self.driver.implicitly_wait(30)
#     self.base_url=u"http://www.baidu.com"

# Android environment
import unittest
from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.1.1'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['app'] = '/source/weixin_1080.apk'

self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


# iOS environment
# import unittest
# from appium import webdriver
#
# desired_caps = {}
# desired_caps['platformName'] = 'iOS'
# desired_caps['platformVersion'] = '10.3.3'
# desired_caps['deviceName'] = 'iPhone Simulator'
# desired_caps['app'] = PATH('/weixin_1080.apk')
#
# self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)