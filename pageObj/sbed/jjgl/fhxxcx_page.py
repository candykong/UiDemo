#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'kongzhibing'

import os
import sys
from config import setting
from pageObj.base import Page
from util.GetYaml import getyaml
from util.getIni import get_loan_config


sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
testData = getyaml(setting.TEST_Element_YAML + '/sbed/jjgl/' + 'fhxxcx.yaml')


class Fhxxcx(Page):

    # 获取复核信息查询菜单
    fhxxcx_loc = (testData.get_find_type(0, 0), testData.get_elementinfo(0, 0))
    fhxxcx_operate_type = testData.get_operate_type(0, 0)

    # 获取列表标题
    title_check_loc = (testData.get_CheckFindType(0, 0), testData.get_CheckElementinfo(0, 0))
    title_check_operate_type = testData.get_CheckOperate_type(0, 0)

    # 获取基础查询字段
    baseQuery_loc = (testData.get_find_type(0, 1), testData.get_elementinfo(0, 1))
    baseQuery_operate_type = testData.get_operate_type(0, 1)
    baseQuery_loc_order = testData.get_order(0, 1)

    baseQueryButton_loc = (testData.get_find_type(1, 1), testData.get_elementinfo(1, 1))
    baseQueryButton_operate_type = testData.get_operate_type(1, 1)


    baseQuery_check_loc = (testData.get_CheckFindType(0, 1), testData.get_CheckElementinfo(0, 1))
    baseQuery_check_operate_type = testData.get_CheckOperate_type(0, 1)
    baseQuery_check_loc_order = testData.get_Check_order(0, 1)

    baseQuery_updated_check_loc = (testData.get_CheckFindType(1, 1), testData.get_CheckElementinfo(1, 1))
    baseQuery_updated_check_operate_type = testData.get_CheckOperate_type(1, 1)
    baseQuery_updated_check_loc_order = testData.get_Check_order(1, 1)

    # 获取全部的高级搜索字段名称
    advanceQuery_check_loc = (testData.get_CheckFindType(0, 2), testData.get_CheckElementinfo(0, 2))
    advanceQuery_check_operate_type = testData.get_CheckOperate_type(0, 2)

    # 获取客户群体下拉框选项
    khqtQuery_loc = (testData.get_find_type(0, 3), testData.get_elementinfo(0, 3))
    khqtQuery_operate_type = testData.get_operate_type(0, 3)

    khqtQuery_check_loc = (testData.get_CheckFindType(1, 3), testData.get_CheckElementinfo(1, 3))
    khqtceQuery_check_operate_type = testData.get_CheckOperate_type(1, 3)

    # 获取调查状态下拉框选项
    investStatus_loc = (testData.get_find_type(0, 4), testData.get_elementinfo(0, 4))
    investStatus_operate_type = testData.get_operate_type(0, 4)

    investStatus_check_loc = (testData.get_CheckFindType(1, 4), testData.get_CheckElementinfo(1, 4))
    investStatus_check_operate_type = testData.get_CheckOperate_type(1, 4)

    # 获取超时状态下拉框选项
    overTimeStatus_loc = (testData.get_find_type(0, 5), testData.get_elementinfo(0, 5))
    overTimeStatus_operate_type = testData.get_operate_type(0, 5)

    overTimeStatus_check_loc = (testData.get_CheckFindType(1, 5), testData.get_CheckElementinfo(1, 5))
    overTimeStatus_check_operate_type = testData.get_CheckOperate_type(1, 5)

    #高级查询-申请时间-开始时间
    applyStartTimeQuery_loc = (testData.get_find_type(0, 6), testData.get_elementinfo(0, 6))
    applyStartTimeQuery_operate_type = testData.get_operate_type(0, 6)
    applyStartTimeQuery_loc_order = testData.get_order(0, 6)

    applyStartTimeQuery_check_loc = (testData.get_CheckFindType(0, 6), testData.get_CheckElementinfo(0, 6))
    applyStartTimeQuery_check_operate_type = testData.get_CheckOperate_type(0, 6)
    applyStartTimeQuery_check_loc_order = testData.get_Check_order(0, 6)

    # 高级查询-申请时间-结束时间
    applyEndTimeQuery_loc = (testData.get_find_type(1, 6), testData.get_elementinfo(1, 6))
    applyEndTimeQuery_operate_type = testData.get_operate_type(1, 6)
    applyEndTimeQuery_loc_order = testData.get_order(1, 6)

    applyEndTimeQuery_check_loc = (testData.get_CheckFindType(1, 6), testData.get_CheckElementinfo(1, 6))
    applyEndTimeQuery_check_operate_type = testData.get_CheckOperate_type(1, 6)
    applyEndTimeQuery_check_loc_order = testData.get_Check_order(1, 6)

    # 高级查询-手机号
    phoneQuery_loc = (testData.get_find_type(0, 7), testData.get_elementinfo(0, 7))
    phoneQuery_operate_type = testData.get_operate_type(0, 7)

    phoneQuery_check_loc = (testData.get_CheckFindType(0, 7), testData.get_CheckElementinfo(0, 7))
    phoneQuery_check_operate_type = testData.get_CheckOperate_type(0, 7) #取placeholeder
    phoneQuery_check_operate_type2 = testData.get_CheckOperate_type(0, 7) #取value
    phoneQuery_check_loc_order = testData.get_Check_order(0, 7)


    # 列表表头
    tableColName_check_loc = (testData.get_CheckFindType(0, 8), testData.get_CheckElementinfo(0, 8))
    tableColName_check_operate_type = testData.get_CheckOperate_type(0, 8)

    # 重置和搜索
    reset_loc = (testData.get_find_type(0, 9), testData.get_elementinfo(0, 9))
    reset_operate_type = testData.get_operate_type(0, 9)
    search_loc = (testData.get_find_type(1, 9), testData.get_elementinfo(1, 9))
    search_operate_type = testData.get_operate_type(1, 9)

    allQuery_check_loc = (testData.get_CheckFindType(1, 9), testData.get_CheckElementinfo(1, 9))
    allQuery_check_operate_type = testData.get_CheckOperate_type(1, 9) #输入框为多个，需要循环判断

    totalNum_check_loc = (testData.get_CheckFindType(0, 9), testData.get_CheckElementinfo(0, 9)) #列表右下角总数元素
    totalNum_check_operate_type = testData.get_CheckOperate_type(0, 9)



    # 列表中第一个客户
    col_first_customer_loc = (testData.get_find_type(0, 10), testData.get_elementinfo(0, 10))
    col_first_customer_operate_type = testData.get_operate_type(0, 10)
    col_first_customer_check_lock = col_first_customer_loc
    col_first_customer_check_type = testData.get_CheckOperate_type(0, 10)
    customer_check_lock = (testData.get_CheckFindType(1, 10), testData.get_CheckElementinfo(1, 10))
    customer_check_type = testData.get_CheckOperate_type(1, 10)


    def click_fhxxcx_Menu(self):
        """
        点击复核信息查询菜单
        :return:
        """
        element = self.find_element(*self.fhxxcx_loc)
        return eval(f"element.{self.fhxxcx_operate_type}")



    def get_title(self):
        """
        获取标题
        :return: 标题
        """
        element = self.find_element(*self.title_check_loc)
        return eval(f"element.{self.title_check_operate_type}")

    def click_baseQueryButton(self):
        """
        点击贷款进度查询菜单
        :return:
        """
        element = self.find_element(*self.baseQueryButton_loc)
        return eval(f"element.{self.baseQueryButton_operate_type}")

    def get_baseQuery(self):
        """
        获取基础查询文本框默认文案
        :return:
        """
        element = self.find_elements(*self.baseQuery_check_loc,order=self.baseQuery_check_loc_order)
        return eval(f"element.{self.baseQuery_check_operate_type}")

    def input_baseQuery(self,nameOrIdcard):
        """
        基础查询文本框输入姓名或者身份证
        :return:
        """
        """
           输入账号
           :param username:
           :return:
           """
        element = self.find_elements(*self.baseQuery_loc,order=self.baseQuery_loc_order)
        eval(f"element.{self.baseQuery_operate_type}('{nameOrIdcard}')")

    def get_baseQuery_value(self):
        """
        获取基础查询文本框的值
        :return:
        """
        element = self.find_elements(*self.baseQuery_updated_check_loc,order=self.baseQuery_updated_check_loc_order)
        return eval(f"element.{self.baseQuery_updated_check_operate_type}")

    def get_advanceQuery(self):
        """
        获取所有高级查询字段
        :return:
        """
        elements = self.find_elements(*self.advanceQuery_check_loc)
        options = []
        for element in elements:
            option = eval(f"element.{self.advanceQuery_check_operate_type}")
            options.append(option)
        return ' '.join(options)



    def click_khqtQuery(self):
        """
        点击高级查询-客户群体
        :return:
        """
        element = self.find_element(*self.khqtQuery_loc)
        return eval(f"element.{self.khqtQuery_operate_type}")

    def location_khqtQuery_options(self):
        """
        先点击客户群体，再定位到选项框
        :return:
        """
        self.click_khqtQuery()
        # elements = self.find_elements(*self.khqtQuery_check_loc)
        parElements = self.find_elements2(testData.get_CheckFindType(0, 3), testData.get_CheckElementinfo(0, 3))
        length = len(parElements) - 1
        elements = parElements[length].find_elements(testData.get_CheckFindType(1, 3),
                                                     testData.get_CheckElementinfo(1, 3))
        return elements

    def get_khqtQuery_options(self):

        """
        获取高级查询-获取客户群体下拉选项值
        :return:
        """
        # self.khqtQuery_click()
        # # elements = self.find_elements(*self.khqtQuery_check_loc)
        # parElements = self.find_elements2(testData.get_CheckFindType(0, 3), testData.get_CheckElementinfo(0, 3))
        # length = len(parElements)-1
        # elements = parElements[length].find_elements(testData.get_CheckFindType(1, 3), testData.get_CheckElementinfo(1, 3))
        elements = self.location_khqtQuery_options()
        groupNames = []
        for group in elements:
            groupname = group.text
            if groupname != '':
                groupNames.append(groupname)
        self.click_khqtQuery()
        return ' '.join(groupNames)

    def select_khqtQuery_options(self,khqtName):
        """
        khqtId：0-贵宾名单q群体，1-公职上班群体，2-个体工商户群体，3-私企上班群体，4-行内客户群体，5-城乡居民群体，由字典配置
        :param khqtName:
        :return:
        """
        elements = self.location_khqtQuery_options()
        elements[int(get_loan_config('sbedKhqt',khqtName))].click()



    def click_investStatus(self):
        """
        点击高级查询-调查状态
        :return:
        """
        element = self.find_element(*self.investStatus_loc)
        return eval(f"element.{self.investStatus_operate_type}")

    def location_investStatus_options(self):
        """
        先点击调查状态，在定位到高级查询-调查状态下拉选项值
        :return:
         """
        self.click_investStatus()
        # elements = self.find_elements(*self.dqjdQuery_check_loc)
        parElements = self.find_elements2(testData.get_CheckFindType(0, 4), testData.get_CheckElementinfo(0, 4))
        length = len(parElements) - 1
        elements = parElements[length].find_elements(testData.get_CheckFindType(1, 4),
                                                     testData.get_CheckElementinfo(1, 4))
        return elements

    def get_investStatus_options(self):

        """
        获取高级查询-获取调查状态下拉选项值
        :return:
        """
        # self.dqjdQuery_click()
        # # elements = self.find_elements(*self.dqjdQuery_check_loc)
        # parElements = self.find_elements2(testData.get_CheckFindType(0, 4), testData.get_CheckElementinfo(0, 4))
        # length = len(parElements) - 1
        # elements = parElements[length].find_elements(testData.get_CheckFindType(1, 4), testData.get_CheckElementinfo(1, 4))
        elements = self.location_investStatus_options()
        jdNames = []
        for jd in elements:
            jdname = jd.text
            if jdname != '':
                jdNames.append(jdname)
        self.click_investStatus()
        return ' '.join(jdNames)

    def select_investStatus_options(self,investStatus):
        """
         investStatus：0-待调查，1-调查通过，2-调查拒绝，由字典配置
         :param investStatus:
         :return:
         """
        elements = self.location_investStatus_options()
        elements[int(get_loan_config('sbedDczt',investStatus))].click()

    def click_overTimeStatus(self):
        """
        点击高级查询-超时状态
        :return:
        """
        element = self.find_element(*self.overTimeStatus_loc)
        return eval(f"element.{self.overTimeStatus_operate_type}")

    def location_overTimeStatus_options(self):
        """
        先点击超时状态，在定位到高级查询-超时状态下拉选项值
        :return:
         """
        self.click_overTimeStatus()
        # elements = self.find_elements(*self.dqjdQuery_check_loc)
        parElements = self.find_elements2(testData.get_CheckFindType(0, 5), testData.get_CheckElementinfo(0, 5))
        length = len(parElements) - 1
        elements = parElements[length].find_elements(testData.get_CheckFindType(1, 5),
                                                     testData.get_CheckElementinfo(1, 5))
        return elements

    def get_overTimeStatus_options(self):

        """
        获取高级查询-获取超时状态下拉选项值
        :return:
        """
        elements = self.location_overTimeStatus_options()
        jdNames = []
        for jd in elements:
            jdname = jd.text
            if jdname != '':
                jdNames.append(jdname)
        self.click_overTimeStatus()
        return ' '.join(jdNames)

    def select_overTimeStatus_options(self,overTimeStatus):
        """
         overTimeStatus：0-未超时，1-已超时
         :param overTimeStatus:
         :return:
         """
        elements = self.location_overTimeStatus_options()
        elements[int(get_loan_config('sbedDqjd',overTimeStatus))].click()

    def get_applyStartTime(self):
        """
        获取高级查询-申请时间-开始时间
        :return:
        """
        element = self.find_elements(*self.applyStartTimeQuery_check_loc, order=self.applyStartTimeQuery_check_loc_order)
        return eval(f"element.{self.applyStartTimeQuery_check_operate_type}")


    def get_applyEndTime(self):
        """
        获取高级查询-申请时间-结束时间
        :return:
        """
        element = self.find_elements(*self.applyEndTimeQuery_check_loc,
                                     order=self.applyEndTimeQuery_check_loc_order)
        return eval(f"element.{self.applyEndTimeQuery_check_operate_type}")

    def click_applyStartTime(self):
        """
        点击开始时间输入框
        :return:
        """
        element = self.find_elements(*self.applyStartTimeQuery_loc, order=self.applyStartTimeQuery_loc_order)
        eval(f"element.{self.applyStartTimeQuery_operate_type}")


    def click_applyEndTime(self):
        """
        点击结束时间输入框
        :return:
        """
        element = self.find_elements(*self.applyEndTimeQuery_loc, order=self.applyEndTimeQuery_loc_order)
        eval(f"element.{self.applyEndTimeQuery_operate_type}")


    def input_phone(self,phone):
        """
        输入手机号
        :param phone:
        :return:
        """
        element = self.find_elements(*self.phoneQuery_loc, order=self.phoneQuery_check_loc_order)
        eval(f"element.{self.phoneQuery_operate_type}('{phone}')")



    def get_phoneQuery_value(self):
        """
        获取手机号输入框的值
        :return:
        """
        element = self.find_elements(*self.phoneQuery_check_loc,order=self.baseQuery_updated_check_loc_order)
        return eval(f"element.{self.phoneQuery_check_operate_type2}")


    def get_tableColName(self):
        """

        :return:
        """
        elements = self.find_elements(*self.tableColName_check_loc)
        names = []
        for element in elements:
            name = eval(f"element.{self.tableColName_check_operate_type}")
            names.append(name)
        return ' '.join(names)


    def baseQuery(self,nameOrIdcard):
        """
        先输入基础查询内容，再点击基础查询按钮
        :param nameOrIdcard:
        :return:
        """
        self.input_baseQuery(nameOrIdcard)
        self.click_baseQueryButton()

    def resetButton_click(self):
        """
        点击重置按钮
        :return:
        """
        element = self.find_element(*self.reset_loc)
        return eval(f"element.{self.reset_operate_type}")

    def searchButton_click(self):
        """
        点击搜索按钮
        :return:
        """
        element = self.find_element(*self.search_loc)
        return eval(f"element.{self.search_operate_type}")

    def get_totalNum(self):
        """
        获取列表所有总数
        :return:
        """
        element = self.find_element(*self.totalNum_check_loc)
        return eval(f"element.{self.totalNum_check_operate_type}")

    def get_allquery_value(self):
        """
        获取所有查询输入框的值
        :return:
        """
        elements = self.find_elements(*self.allQuery_check_loc)
        values=[]
        for element in elements:
            value =  eval(f"element.{self.totalNum_check_operate_type}")
            values.append(value)
        return values


    def get_col_first_customer_name(self):
        """
        获取列表中第一个客户姓名
        :return:
        """
        element = self.find_element(*self.col_first_customer_check_lock)
        return eval(f"element.{self.col_first_customer_check_type}")

    def click_col_first_customer_name(self):
        """
        获取列表中第一个客户姓名
        :return:
        """
        element = self.find_element(*self.col_first_customer_loc)
        return eval(f"element.{self.col_first_customer_operate_type}")

    def get_customer_name(self):
        """
        获取详情页中的客户姓名
        :return:
        """
        element = self.find_element(*self.customer_check_lock)
        return eval(f"element.{self.customer_check_type}")







