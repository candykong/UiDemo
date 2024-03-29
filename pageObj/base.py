#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'kongzhibing'

import os,sys
import time

from selenium.webdriver.common.by import By

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchFrameException,NoSuchWindowException,NoAlertPresentException,NoSuchElementException
from util.log import Log
from config import setting
from util.getIni import get_config
from selenium.webdriver.common.action_chains import ActionChains


# timeout=setting.TIMEOUT
timeout=get_config('seleniumWaitTime','timeout')

log = Log()


class Page():
    """
    基础类，用于页面对象类的继承
    """

    def __init__(self,driver):
        self.driver = driver
        self.timeout = timeout



    def on_page(self,url):
        """
        URL地址断言
        :return: URL地址
        """
        return self.driver.current_url == (url)


    def open(self,url):
        """
        打开浏览器URL访问
        :param url: URL地址
        :return:
        """
        self.driver.get(url)
        time.sleep(2)
        # assert self.on_page(),'Did not land on %s' % url

    def back(self):
        """
        浏览器后退
        :return:
        """
        self.driver.back()
        time.sleep(2)


    def find_element(self,*loc):
        """
        单个元素定位
        :param loc: 传入元素属性
        :return: 定位到的元素
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(loc))
            # return self.driver.find_element(*loc)
            return element
        except:
            log.error("{0}页面中未能找到{1}元素".format(self,loc))

    def find_elements(self,*loc,order=None):
        """
        多个元素定位
        :param loc: 传入元素属性
        :return: 定位到的元素
        """
        if order==None:
            try:
                elements=WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(loc))
                return elements
            except:
                log.error("{0}页面中未能找到{1}元素".format(self,loc))
        else:
            try:
                elements = WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(loc))
                return elements[order]
            except:
                log.error("{0}页面中未能找到{1}元素".format(self, loc))

    def find_elements2(self,type,element,order=None):
        """

        :return:
        """
        if order == None:
            elements = self.driver.find_elements(type,element)
            return elements
        else:
            elements = self.driver.find_elements(type, element)
            return elements[order]



    def get_element_text(self,element):

        try:
            return element.text
        except:
            log.error("未获取{0}元素内容".format(element))


    def script(self,src,element=None):
        """
        提供调用JavaScript方法
        :param src: 脚本文件
        :return: JavaScript脚本
        """
        if(element==None):
            return self.driver.execute_script(src)
        else:
            return self.driver.execute_script(src,element)



    # 重写定义send_keys方法
    def send_key(self, loc, vaule, clear_first=True, click_first=True):
        try:
            loc = getattr(self, "_%s" % loc)  # getattr相当于实现self.loc
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(vaule)
        except AttributeError:
            log.error("%s 页面中未能找到 %s 元素" % (self, loc))

    def switch_frame(self, loc):
        """
        多表单嵌套切换
        :param loc: 传元素的属性值
        :return: 定位到的元素
        """
        try:
            return self.driver.switch_to_frame(loc)
        except NoSuchFrameException as msg:
            log.error("查找iframe异常-> {0}".format(msg))

    def switch_windows(self,loc):
        """
        多窗口切换
        :param loc:
        :return:
        """
        try:
            return self.driver.switch_to_window(loc)
        except NoSuchWindowException as msg:
            log.error("查找窗口句柄handle异常-> {0}".format(msg))

    def switch_alert(self):
        """
        警告框处理
        :return:
        """
        try:
            return self.driver.switch_to_alert()
        except NoAlertPresentException as msg:
            log.error("查找alert弹出框异常-> {0}".format(msg))


    def move_to_element(self,element):
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()



    def close_driver(self):
        self.driver.close()








