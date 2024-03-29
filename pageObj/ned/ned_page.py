#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'kongzhibing'

import os,sys


sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from config import setting
from pageObj.base import Page
from util.GetYaml import getyaml

testData = getyaml(setting.TEST_Element_YAML + '/ned/' + 'ned.yaml')


class Ned(Page):

    # 获取账号名称校验元素
    account_check_loc = (testData.get_CheckFindType(0, 0), testData.get_CheckElementinfo(0, 0))
    account_check_operate_type = testData.get_CheckOperate_type(0, 0)

    # # 获取机构名称校验元素
    org_check_loc = (testData.get_CheckFindType(1, 0), testData.get_CheckElementinfo(1, 0))
    org_check_operate_type = testData.get_CheckOperate_type(1, 0)

    # # 获取手机号校验元素
    phone_check_loc = (testData.get_CheckFindType(2, 0), testData.get_CheckElementinfo(2, 0))
    phone_check_operate_type = testData.get_CheckOperate_type(2, 0)

    # # 获取父级菜单校验元素
    parentMenus_check_loc = (testData.get_CheckFindType(0, 1), testData.get_CheckElementinfo(0, 1))
    parentMenus_check_operate_type = testData.get_CheckOperate_type(0, 1)

    #获取各个父菜单元素
    #1、进件管理元素和校验元素
    jjgl_loc = (testData.get_find_type(0,2), testData.get_elementinfo(0,2))
    jjgl_operate_type = testData.get_operate_type(0, 2)
    jjgl_check_loc = (testData.get_CheckFindType(0, 2), testData.get_CheckElementinfo(0, 2))
    jjgl_check_operate_type = testData.get_CheckOperate_type(0, 2)

    # 2、贷后审批管理元素和校验元素
    dhspgl_loc = (testData.get_find_type(1, 2), testData.get_elementinfo(1, 2))
    dhspgl_operate_type = testData.get_operate_type(1, 2)
    dhspgl_check_loc = (testData.get_CheckFindType(1, 2), testData.get_CheckElementinfo(1, 2))
    dhspgl_check_operate_type = testData.get_CheckOperate_type(1, 2)


    def check_account(self):
        """
        获取账号信息
        :return: 账号名称
        """
        element = self.find_element(*self.account_check_loc)
        return eval(f"element.{self.account_check_operate_type}")


    def check_org(self):
        """
        获取所属机构
        :return: 所属机构
        """
        element = self.find_element(*self.org_check_loc)
        return eval(f"element.{self.org_check_operate_type}")

    def check_phone(self):
        """
        获取手机号
        :return: 手机号
        """
        element = self.find_element(*self.phone_check_loc)
        return eval(f"element.{self.phone_check_operate_type}")

    def check_parentMenus(self):
        """
        获取父级菜单
        :return:父级菜单名称
        """
        elements = self.find_elements(*self.parentMenus_check_loc)
        menus = []
        for element in elements:
            menu = eval(f"element.{self.parentMenus_check_operate_type}")
            menus.append(menu)
        return ' '.join(menus)

    def jjgl_Menu_click(self):
        """
        点击进件管理菜单
        :return:
        """
        element = self.find_element(*self.jjgl_loc)
        src = self.jjgl_operate_type
        self.script(src,element)


    def dhspgl_Menu_click(self):
        """
        点击贷后审批管理菜单
        :return:
        """
        element = self.find_element(*self.dhspgl_loc)
        src = self.dhspgl_operate_type
        self.script(src, element)

    def check_jjgl_sbumenus(self):
        """
        获取进件管理子菜单
        :return:
        """
        self.jjgl_Menu_click()
        elements = self.find_elements(*self.jjgl_check_loc)
        menus = []
        for element in elements:
            menu = eval(f"element.{self.jjgl_check_operate_type}")
            menus.append(menu)
        return ' '.join(menus)


    def check_dhspgl_sbumenus(self):
        """
        获取贷后审批管理子菜单
        :return:
        """
        self.dhspgl_Menu_click()
        elements = self.find_elements(*self.dhspgl_check_loc)
        menus = []
        for element in elements:
            menu = eval(f"element.{self.dhspgl_check_operate_type}")
            menus.append(menu)
        return ' '.join(menus)






