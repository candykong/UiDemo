#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'kongzhibing'

import os,sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from config import setting
from pageObj.base import Page
from util.GetYaml import getyaml


testData = getyaml(setting.TEST_Element_YAML + '/sbed/' + 'sbed.yaml')


class Sbed(Page):

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

    # 1、电核管理元素和校验元素
    dhgl_loc = (testData.get_find_type(1, 2), testData.get_elementinfo(1, 2))
    dhgl_operate_type = testData.get_operate_type(1, 2)
    dhgl_check_loc = (testData.get_CheckFindType(1, 2), testData.get_CheckElementinfo(1, 2))
    dhgl_check_operate_type = testData.get_CheckOperate_type(1, 2)
    # 1、贷后管理元素和校验元素
    dhougl_loc = (testData.get_find_type(2, 2), testData.get_elementinfo(2, 2))
    dhougl_operate_type = testData.get_operate_type(2, 2)
    dhougl_check_loc = (testData.get_CheckFindType(2, 2), testData.get_CheckElementinfo(2, 2))
    dhougl_check_operate_type = testData.get_CheckOperate_type(2, 2)
    # 1、异常管理元素和校验元素
    ycgl_loc = (testData.get_find_type(3, 2), testData.get_elementinfo(3, 2))
    ycgl_operate_type = testData.get_operate_type(3, 2)
    ycgl_check_loc = (testData.get_CheckFindType(3, 2), testData.get_CheckElementinfo(3, 2))
    ycgl_check_operate_type = testData.get_CheckOperate_type(3, 2)
    # 1、业务配置元素和校验元素
    ywpz_loc = (testData.get_find_type(4, 2), testData.get_elementinfo(4, 2))
    ywpz_operate_type = testData.get_operate_type(4, 2)
    ywpz_check_loc = (testData.get_CheckFindType(4, 2), testData.get_CheckElementinfo(4, 2))
    ywpz_check_operate_type = testData.get_CheckOperate_type(4, 2)
    # 1、贷后审批管理元素和校验元素
    dhspgl_loc = (testData.get_find_type(5, 2), testData.get_elementinfo(5, 2))
    dhspgl_operate_type = testData.get_operate_type(5, 2)
    dhspgl_check_loc = (testData.get_CheckFindType(5, 2), testData.get_CheckElementinfo(5, 2))
    dhspgl_check_operate_type = testData.get_CheckOperate_type(5, 2)


    #角色
    roleChange_loc = (testData.get_find_type(0, 3), testData.get_elementinfo(0, 3))
    # roleChange_operate_type = testData.get_operate_type(0, 3)
    roles_loc = (testData.get_find_type(1, 3), testData.get_elementinfo(1, 3))
    # roles_operate_type = testData.get_operate_type(1, 3)
    roles_order = testData.get_order(1,3)
    role_loc = (testData.get_find_type(2, 3), testData.get_elementinfo(2, 3))
    role_operate_type = testData.get_operate_type(2, 3)



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

    def dhgl_Menu_click(self):
        """
        点击电核管理菜单
        :return:
        """
        element = self.find_element(*self.dhgl_loc)
        src = self.dhgl_operate_type
        self.script(src,element)

    def dhougl_Menu_click(self):
        """
        点击贷后管理菜单
        :return:
        """
        element = self.find_element(*self.dhougl_loc)
        src = self.dhougl_operate_type
        self.script(src, element)

    def ycgl_Menu_click(self):
        """
         点击异常管理菜单
        :return:
        """
        element = self.find_element(*self.ycgl_loc)
        src = self.ycgl_operate_type
        self.script(src, element)

    def ywpz_Menu_click(self):
        """
        点击业务配置菜单
        :return:
        """
        element = self.find_element(*self.ywpz_loc)
        src = self.ywpz_operate_type
        self.script(src, element)

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


    def check_dhgl_sbumenus(self):
        """
        获取电核管理子菜单
        :return:
        """
        self.dhgl_Menu_click()
        elements = self.find_elements(*self.dhgl_check_loc)
        menus = []
        for element in elements:
            menu = eval(f"element.{self.dhgl_check_operate_type}")
            menus.append(menu)
        return ' '.join(menus)

    def check_dhougl_sbumenus(self):
        """
        获取贷后管理子菜单
        :return:
        """
        self.dhougl_Menu_click()
        elements = self.find_elements(*self.dhougl_check_loc)
        menus = []
        for element in elements:
            menu = eval(f"element.{self.dhougl_check_operate_type}")
            menus.append(menu)
        return ' '.join(menus)

    def check_ycgl_sbumenus(self):
        """
        获取异常管理子菜单
        :return:
        """
        self.ycgl_Menu_click()
        elements = self.find_elements(*self.ycgl_check_loc)
        menus = []
        for element in elements:
            menu = eval(f"element.{self.ycgl_check_operate_type}")
            menus.append(menu)
        return ' '.join(menus)

    def check_ywpz_sbumenus(self):
        """
        获取业务配置子菜单
        :return:
        """
        self.ywpz_Menu_click()
        elements = self.find_elements(*self.ywpz_check_loc)
        menus = []
        for element in elements:
            menu = eval(f"element.{self.ywpz_check_operate_type}")
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

    def change_role(self,roleName):
        role_change_element = self.find_element(*self.roleChange_loc)
        self.move_to_element(role_change_element)
        roles = self.find_elements2(self.roles_loc[0],self.roles_loc[1],order=self.roles_order)
        new_role_loc=(self.role_loc[0],self.role_loc[1].replace('角色名称', roleName))
        print(new_role_loc)
        role = roles.find_element(*new_role_loc)
        self.move_to_element(role)
        return eval(f"role.{self.role_operate_type}")





