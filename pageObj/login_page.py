#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'kongzhibing'

import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from config import setting
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from pageObj.base import Page
from time import sleep
from util.GetYaml import getyaml
from config import setting

testData = getyaml(setting.TEST_Element_YAML + '/' + 'login.yaml')

login_url=setting.loginURL


class Login(Page):

    # 定位器，通过元素属性定位元素对象
    # 账号输入框
    login_account_loc = (testData.get_find_type(0),testData.get_elementinfo(0))
    account_operate_type = testData.get_operate_type(0)
    # 密码输入框
    login_password_loc = (testData.get_find_type(1),testData.get_elementinfo(1))
    password_operate_type = testData.get_operate_type(1)
    # 登录按钮
    login_button_loc = (testData.get_find_type(2),testData.get_elementinfo(2))
    login_button_operate_type = testData.get_operate_type(2)


    def login_account(self,account):
        """
        输入账号
        :param username:
        :return:
        """
        element=self.find_element(*self.login_account_loc)
        eval(f"element.{self.account_operate_type}('{account}')")

    def login_password(self,password):
        """
        登录密码
        :param password:
        :return:
        """
        element = self.find_element(*self.login_password_loc)
        eval(f"element.{self.password_operate_type}('{password}')")

    def login_button(self):
        """
        登录按钮
        :return:
        """
        element = self.find_element(*self.login_button_loc)
        eval(f"element.{self.login_button_operate_type}()")


    def user_login(self,account,password):
        """
        登录入口
        :param username: 用户名
        :param password: 密码
        :return:
        """
        self.open(login_url)
        self.login_account(account)
        self.login_password(password)
        sleep(1)
        self.login_button()
        sleep(1)

    def check_page(self,url):
        self.on_page(url)


#
# if __name__ == '__main__':
#     Login=login(login_url)
#     Login.user_login('','kgly1','123456Aa')

