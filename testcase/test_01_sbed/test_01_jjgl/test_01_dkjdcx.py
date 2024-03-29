# _*_ coding:utf-8 _*_
__author__ = 'kongzhibing'


import os,sys
import time
from datetime import datetime, timedelta

from pageObj.base import Page
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import pytest
import allure
from config import setting
from pageObj.applyCentor_page import ApplyCentor
from pageObj.sbed.jjgl.dkjdcx_page import Dkjdcx
from pageObj.sbed.sbed_page import Sbed
from util.log import Log
from util.GetYaml import getyaml

log = Log()
testData = getyaml(setting.TEST_DATA_YAML + '/sbed/jjgl/' + 'dkjdcx_data.yaml')
applyCentorUrl=setting.applyCentorUrl

# @pytest.mark.usefixtures("to_sbed")
@pytest.mark.usefixtures("session_login")
@allure.feature("社保e贷-进件管理-贷款进度查询页面")
class Test_dkjdcx():

    def driver(self,request):
        self.driver = request.session.driver

    @pytest.fixture(scope="class", autouse=True)
    def setup(self,request):
        # 进入社保e贷-进件管理-贷款进度查询页面
        self.driver(request)
        applyCentor = ApplyCentor(self.driver)
        sbed = Sbed(self.driver)
        dkjdcx = Dkjdcx(self.driver)
        applyCentor.to_sbed_apply()
        sbed.jjgl_Menu_click()
        dkjdcx.click_dkjdcx_Menu()
        yield
        page = Page(self.driver)
        page.open(applyCentorUrl)


    @allure.story("检查贷款进度查询也没标题")
    @pytest.mark.parametrize('casedata',testData.get_testcase("test_dkjdcx001"))
    # @pytest.mark.skip(reason='先不测试')
    def test_title(self,casedata,request):

        """
        检查标题
        :return:
        """
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(casedata['id'],casedata['detail']))
        self.driver(request)
        dkjdcx = Dkjdcx(self.driver)
        title = dkjdcx.get_title()
        assert title == casedata['check']['title']

    @allure.story("检查基础查询输入框默认文案")
    @pytest.mark.parametrize('casedata',testData.get_testcase("test_dkjdcx002"))
    def test_baseQuery(self,casedata,request):

        """
        检查基础查询输入框默认文案
        :return:
        """
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(casedata['id'],casedata['detail']))
        self.driver(request)
        dkjdcx = Dkjdcx(self.driver)
        content = dkjdcx.get_baseQuery()
        assert content == casedata['check']['content']

    @allure.story("检查高级查询字段是否完整")
    @pytest.mark.parametrize('casedata',testData.get_testcase("test_dkjdcx003"))
    def test_search(self,casedata,request):

        """
        检查高级查询字段是否完整
        :return:
        """
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(casedata['id'],casedata['detail']))
        self.driver(request)
        dkjdcx = Dkjdcx(self.driver)
        content= dkjdcx.get_advanceQuery()
        assert content.strip(' ') == casedata['check']['content']

    @allure.story("检查客户群体下拉选项是否完整")
    @pytest.mark.parametrize('casedata',testData.get_testcase("test_dkjdcx004"))
    def test_searchCustomerOptions(self,casedata,request):

        """
        检查客户群体下拉选项是否完整
        :return:
        """
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(casedata['id'],casedata['detail']))
        self.driver(request)
        dkjdcx = Dkjdcx(self.driver)
        content= dkjdcx.get_khqtQuery_options()
        assert content == casedata['check']['content']

    @allure.story("检查当前进度下拉选项是否完整")
    @pytest.mark.parametrize('casedata',testData.get_testcase("test_dkjdcx005"))
    def test_searchDqjdOptions(self,casedata,request):

        """
        检查当前进度下拉选项是否完整
        :return:
        """
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(casedata['id'],casedata['detail']))
        self.driver(request)
        dkjdcx = Dkjdcx(self.driver)
        content= dkjdcx.get_dqjdQuery_options()
        assert content.strip(' ') == casedata['check']['content']



    @allure.story("检查高级搜索-开始时间和结束时间默认时间是否正确")
    @pytest.mark.parametrize('casedata',testData.get_testcase("test_dkjdcx006"))
    def test_searchApplytime(self,casedata,request):

        """
        检查高级搜索-开始时间和结束时间默认时间是否正确
        :return:
        """
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(casedata['id'],casedata['detail']))
        self.driver(request)
        dkjdcx = Dkjdcx(self.driver)
        dkjdcx.searchButton_click()
        applyStartTime = dkjdcx.get_applyStartTime()
        applyEndTime = dkjdcx.get_applyEndTime()
        today = datetime.now().date()
        past_90_days = today - timedelta(days=90)
        assert str(past_90_days).replace("-", "/") == applyStartTime
        assert str(today).replace("-", "/") == applyEndTime

    @allure.story("检查表头字段是否完整")
    @pytest.mark.parametrize('casedata',testData.get_testcase("test_dkjdcx009"))
    def test_tableHeaders(self,casedata,request):

        """
        检查表头字段是否完整
        :return:
        """
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(casedata['id'],casedata['detail']))
        self.driver(request)
        dkjdcx = Dkjdcx(self.driver)
        content= dkjdcx.get_tableColName()
        assert content == casedata['check']['content']


    @allure.story("检查搜索和重置按钮功能")
    @pytest.mark.parametrize('casedata',testData.get_testcase("test_dkjdcx010"))
    def test_searchReset(self,casedata,request):

        """
        检查搜索功能是否正常，重置后查询输入框是否被清空
        :return:
        """
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(casedata['id'],casedata['detail']))
        self.driver(request)
        dkjdcx = Dkjdcx(self.driver)
        if casedata['screenshot'] == 'search':
            dkjdcx.input_baseQuery(casedata['data']['baseQuery'])
            dkjdcx.searchButton_click()
            time.sleep(5)
            content = dkjdcx.get_col_first_customer_name()
            assert content == "*" + casedata['check']['content'][1:]
        elif casedata['screenshot'] == 'reset':
            # dkjdcx.input_baseQuery("张三")
            # dkjdcx.searchButton_click()
            dkjdcx.resetButton_click()
            content= dkjdcx.get_baseQuery_value()
            assert content == ''



    @allure.story("检查点击客户姓名是否正常进入该客户详情页")
    @pytest.mark.parametrize('casedata',testData.get_testcase("test_dkjdcx012"))
    def test_toCustomerDetail(self,casedata,request):
        """
        检查点击客户姓名是否正常进入该客户详情页
        :return:
        """
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(casedata['id'],casedata['detail']))
        self.driver(request)
        dkjdcx = Dkjdcx(self.driver)
        # dkjdcx.input_baseQuery(casedata['data']['baseQuery'])
        dkjdcx.searchButton_click()
        time.sleep(5)
        col_name = dkjdcx.get_col_first_customer_name()
        dkjdcx.click_col_first_customer_name()
        time.sleep(20)
        name1 = dkjdcx.get_customer_name()
        assert col_name == "*" + name1[1:]
        dkjdcx.back()

