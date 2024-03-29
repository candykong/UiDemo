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


testData = getyaml(setting.TEST_Element_YAML + '/' + 'applyCentor.yaml')


class ApplyCentor(Page):

    # 社保e贷应用
    sbed_loc = (testData.get_find_type(0),testData.get_elementinfo(0))
    sbed_operate_type = testData.get_operate_type(0)
    sbed_check_loc = (testData.get_CheckFindType(0), testData.get_CheckElementinfo(0))
    sbed_check_operate_type = testData.get_CheckOperate_type(0)

    # 农e贷应用
    ned_loc = (testData.get_find_type(1), testData.get_elementinfo(1))
    ned_operate_type = testData.get_operate_type(1)
    ned_check_loc = (testData.get_CheckFindType(1), testData.get_CheckElementinfo(1))
    ned_check_operate_type = testData.get_CheckOperate_type(1)




    def to_ned_apply(self):
        """
        点击农e贷
        :return:
        """
        element = self.find_element(*self.ned_loc)
        eval(f"element.{self.ned_operate_type}()")

    def check_ned_title(self):
        """
        进入社保e贷获取标题
        :return: 标题名称
        """
        element = self.find_element(*self.ned_check_loc)
        return eval(f"element.{self.ned_check_operate_type}")


    def to_sbed_apply(self):
        """
        点击社保e贷
        :return:
        """
        element = self.find_element(*self.sbed_loc)
        eval(f"element.{self.sbed_operate_type}()")

    def check_sbed_title(self):
        """
        进入社保e贷获取标题
        :return: 标题名称
        """
        element = self.find_element(*self.sbed_check_loc)
        return eval(f"element.{self.sbed_check_operate_type}")



