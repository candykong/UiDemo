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
testData = getyaml(setting.TEST_Element_YAML + '/sbed/jjgl/' + 'dkjdcx.yaml')


class Dkjdcx(Page):

    # 获取贷款进度查询菜单
    dkjdcx_loc = (testData.get_find_type(0, 0), testData.get_elementinfo(0, 0))
    dkjdcx_operate_type = testData.get_operate_type(0, 0)

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

    # 获取当前进度下拉框选项
    dqjdQuery_loc = (testData.get_find_type(0, 4), testData.get_elementinfo(0, 4))
    dqjdQuery_operate_type = testData.get_operate_type(0, 4)

    dqjdQuery_check_loc = (testData.get_CheckFindType(1, 4), testData.get_CheckElementinfo(1, 4))
    dqjdQuery_check_operate_type = testData.get_CheckOperate_type(1, 4)


    #高级查询-申请时间-开始时间
    applyStartTimeQuery_loc = (testData.get_find_type(0, 5), testData.get_elementinfo(0, 5))
    applyStartTimeQuery_operate_type = testData.get_operate_type(0, 5)
    applyStartTimeQuery_loc_order = testData.get_order(0, 5)

    applyStartTimeQuery_check_loc = (testData.get_CheckFindType(0, 5), testData.get_CheckElementinfo(0, 5))
    applyStartTimeQuery_check_operate_type = testData.get_CheckOperate_type(0, 5)
    applyStartTimeQuery_check_loc_order = testData.get_Check_order(0, 5)

    # 高级查询-申请时间-结束时间
    applyEndTimeQuery_loc = (testData.get_find_type(1, 5), testData.get_elementinfo(1, 5))
    applyEndTimeQuery_operate_type = testData.get_operate_type(1, 5)
    applyEndTimeQuery_loc_order = testData.get_order(1, 5)

    applyEndTimeQuery_check_loc = (testData.get_CheckFindType(1, 5), testData.get_CheckElementinfo(1, 5))
    applyEndTimeQuery_check_operate_type = testData.get_CheckOperate_type(1, 5)
    applyEndTimeQuery_check_loc_order = testData.get_Check_order(1, 5)

    # 高级查询-手机号
    phoneQuery_loc = (testData.get_find_type(0, 6), testData.get_elementinfo(0, 6))
    phoneQuery_operate_type = testData.get_operate_type(0, 6)

    phoneQuery_check_loc = (testData.get_CheckFindType(0, 6), testData.get_CheckElementinfo(0, 6))
    phoneQuery_check_operate_type = testData.get_CheckOperate_type(0, 6) #取placeholeder
    phoneQuery_check_operate_type2 = testData.get_CheckOperate_type(0, 6) #取value
    phoneQuery_check_loc_order = testData.get_Check_order(0, 6)


    # 高级查询-营销人
    mktUserQuery_loc = (testData.get_find_type(0, 7), testData.get_elementinfo(0, 7))
    mktUserQuery_operate_type = testData.get_operate_type(0, 7)

    mktUserQuery_check_loc = (testData.get_CheckFindType(0, 7), testData.get_CheckElementinfo(0, 7))
    mktUserQuery_check_operate_type = testData.get_CheckOperate_type(0, 7)  # 取placeholeder
    mktUserQuery_check_operate_type2 = testData.get_CheckOperate_type(0, 7)  # 取value
    mktUserQuery_check_loc_order = testData.get_Check_order(0, 7)

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

    #日历
    #历日选择框
    rl_elements= testData.get_elementinfo(0, 10)
    rl_find_type = testData.get_find_type(0, 10)
    #选择某个具体可点击的号
    rl_day_elements = testData.get_elementinfo(1, 10)
    rl_day_find_type = testData.get_find_type(1, 10)
    rl_day_operate_type = testData.get_operate_type(1, 10)
    #前一年按钮
    rl_lastYear_elements = testData.get_elementinfo(2, 10)
    rl_lastYear_find_type = testData.get_find_type(2, 10)
    rl_lastYear_operate_type = testData.get_operate_type(2, 10)
    #后一年按钮
    rl_nextYear_elements = testData.get_elementinfo(3, 10)
    rl_nextYear_find_type = testData.get_find_type(3, 10)
    rl_nextYear_operate_type = testData.get_operate_type(3, 10)
    #上个月按钮
    rl_lastMonth_elements = testData.get_elementinfo(4, 10)
    rl_lastMonth_find_type = testData.get_find_type(4, 10)
    rl_lastMonth_operate_type = testData.get_operate_type(4, 10)
    #下个月按钮
    rl_nextMonth_elements = testData.get_elementinfo(5, 10)
    rl_nextMonth_find_type = testData.get_find_type(5, 10)
    rl_nextMonth_operate_type = testData.get_operate_type(5, 10)
    #当前年
    rl_currentYear_check_element = testData.get_CheckFindType(0, 10)
    rl_currentYear_check_find_type = testData.get_CheckElementinfo(0, 10)
    rl_currentYear_check_operate_type = testData.get_CheckOperate_type(0, 10)
    #当前月
    rl_currentMonth_echeck_element = testData.get_CheckFindType(1, 10)
    rl_currentMonth_check_find_type = testData.get_CheckElementinfo(1, 10)
    rl_currentMonth_check_operate_type = testData.get_CheckOperate_type(1, 10)
    #可选择的所有号
    rl_allday_check_element = testData.get_CheckFindType(2, 10)
    rl_allday_check_find_type = testData.get_CheckElementinfo(2, 10)
    rl_allday_check_operate_type = testData.get_CheckOperate_type(2, 10)



    # 列表中第一个客户
    col_first_customer_loc = (testData.get_find_type(0, 11), testData.get_elementinfo(0, 11))
    col_first_customer_operate_type = testData.get_operate_type(0, 11)
    col_first_customer_check_lock = col_first_customer_loc
    col_first_customer_check_type = testData.get_CheckOperate_type(0, 11)
    customer_check_lock = (testData.get_CheckFindType(1, 11), testData.get_CheckElementinfo(1, 11))
    customer_check_type = testData.get_CheckOperate_type(1, 11)


    def click_dkjdcx_Menu(self):
        """
        点击贷款进度查询菜单
        :return:
        """
        element = self.find_element(*self.dkjdcx_loc)
        return eval(f"element.{self.dkjdcx_operate_type}")



    def get_title(self):
        """
        获取标题
        :return: 所属机构
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



    def click_dqjdQuery(self):
        """
        点击高级查询-当前进度
        :return:
        """
        element = self.find_element(*self.dqjdQuery_loc)
        return eval(f"element.{self.dqjdQuery_operate_type}")

    def location_dqjdQuery_options(self):
        """
        先点击当前进度，在定位到高级查询-当前进度下拉选项值
        :return:
         """
        self.click_dqjdQuery()
        # elements = self.find_elements(*self.dqjdQuery_check_loc)
        parElements = self.find_elements2(testData.get_CheckFindType(0, 4), testData.get_CheckElementinfo(0, 4))
        length = len(parElements) - 1
        elements = parElements[length].find_elements(testData.get_CheckFindType(1, 4),
                                                     testData.get_CheckElementinfo(1, 4))
        return elements

    def get_dqjdQuery_options(self):

        """
        获取高级查询-获取当前进度下拉选项值
        :return:
        """
        # self.dqjdQuery_click()
        # # elements = self.find_elements(*self.dqjdQuery_check_loc)
        # parElements = self.find_elements2(testData.get_CheckFindType(0, 4), testData.get_CheckElementinfo(0, 4))
        # length = len(parElements) - 1
        # elements = parElements[length].find_elements(testData.get_CheckFindType(1, 4), testData.get_CheckElementinfo(1, 4))
        elements = self.location_dqjdQuery_options()
        jdNames = []
        for jd in elements:
            jdname = jd.text
            if jdname != '':
                jdNames.append(jdname)
        self.click_dqjdQuery()
        return ' '.join(jdNames)

    def select_dqjdQuery_options(self,dqjd):
        """
         jdId：0-待受理，1-待调查，2-待电核，3-待签约，4-已完成，5-已拒绝，6-提额中，7-待审批，8-审批拒绝，由字典配置
         :param dqjd:
         :return:
         """
        elements = self.location_dqjdQuery_options()
        elements[int(get_loan_config('sbedDqjd',dqjd))].click()

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


    def input_mktUser(self,mktUserName):
        """
        输入营销人姓名
        :param mktUserName:
        :return:
        """
        element = self.find_elements(*self.mktUserQuery_loc, order=self.mktUserQuery_check_loc_order)
        eval(f"element.{self.mktUserQuery_operate_type}('{mktUserName}')")


    def get_phoneQuery_value(self):
        """
        获取手机号输入框的值
        :return:
        """
        element = self.find_elements(*self.phoneQuery_check_loc,order=self.baseQuery_updated_check_loc_order)
        return eval(f"element.{self.phoneQuery_check_operate_type2}")

    def get_mktuserQuery_value(self):
        """
        获取营销人输入框的值
        :return:
        """
        element = self.find_elements(*self.mktUserQuery_check_loc, order=self.baseQuery_updated_check_loc_order)
        return eval(f"element.{self.mktUserQuery_check_operate_type2}")


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

    def find_rl(self):
        """
        找到日历
        :return:
        """
        rlElements = self.find_elements2(self.rl_find_type, self.rl_elements)
        length = len(rlElements) - 1
        return rlElements[length]

        # elements = parElements[length].find_elements(testData.get_CheckFindType(1, 4),
        #                                              testData.get_CheckElementinfo(1, 4))
        # return elements

    def click_lastYear(self):
        """
        点击日历中前一年按钮
        :return:
        """
        rlElement = self.find_rl()
        element = rlElement.find_element(self.rl_lastYear_find_type,self.rl_lastYear_elements)
        eval(f"element.{self.rl_lastYear_operate_type}")

    def click_nextYear(self):
        """
        点击日历中后一年按钮
        :return:
        """
        rlElement = self.find_rl()
        element = rlElement.find_element(self.rl_nextYear_find_type,self.rl_nextYear_elements)
        eval(f"element.{self.rl_nextYear_operate_type}")

    def click_lastMonth(self):
        """
        点击日历中上个月按钮
        :return:
        """
        rlElement = self.find_rl()
        element = rlElement.find_element(self.rl_lastMonth_find_type, self.rl_lastMonth_elements)
        eval(f"element.{self.rl_lastMonth_operate_type}")

    def click_nextMonth(self):
        """
        点击日历中下个月按钮
        :return:
        """
        rlElement = self.find_rl()
        element = rlElement.find_element(self.rl_nextMonth_find_type, self.rl_nextMonth_elements)
        eval(f"element.{self.rl_nextMonth_operate_type}")

    def click_oneDay(self,day):
        """
        选择某天
        :return:
        """
        rlElement = self.find_rl()
        element = rlElement.find_element(self.rl_day_find_type, self.rl_day_elements.format(day))
        eval(f"element.{self.rl_day_operate_type}")

    def get_currentMonth(self):
        """
        获取当前年份
        :return:
        """
        rlElement = self.find_rl()
        element = rlElement.find_element(self.rl_currentMonth_check_find_type, self.rl_currentMonth_echeck_element)
        return eval(f"element.{self.rl_currentMonth_check_operate_type}")


    def get_currentYear(self):
        """
        获取当前年份
        :return:
        """
        rlElement = self.find_rl()
        element = rlElement.find_element(self.rl_currentYear_check_find_type, self.rl_currentYear_check_element)
        return eval(f"element.{self.rl_currentYear_check_operate_type}")

    def get_allAvailableDay(self):
        """
        获取所有可点击的日期
        :return:
        """
        rlElement = self.find_rl()
        element = rlElement.find_element(self.rl_allday_check_find_type, self.rl_allday_check_element)
        return eval(f"element.{self.rl_currentYear_check_operate_type}")


    def input_applyStartTime(self, day):
        """
        高级查询-申请时间,选择开始时间,这里就简单点，输入具体哪一号，复杂的后续更新
        :return:
        """
        self.click_applyStartTime()
        self.click_oneDay(day)


    def input_applyEndTime(self, day):
        """
        高级查询-申请时间,选择结束时间,这里就简单点，输入具体哪一号，复杂的后续更新
        :return:
        """
        self.click_applyEndTime()
        self.click_oneDay(day)






