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
from pageObj.sbed.jjgl.fhxxcx_page import Fhxxcx
from pageObj.sbed.sbed_page import Sbed
from util.log import Log
from util.GetYaml import getyaml

log = Log()
testData = getyaml(setting.TEST_DATA_YAML + '/sbed/jjgl/' + 'fhxxcx_data.yaml')
applyCentorUrl=setting.applyCentorUrl

@pytest.mark.usefixtures("session_login")
@allure.feature("社保e贷-进件管理-复核信息查询页面")
class Test_fhxxcx():

    def driver(self,request):
        self.driver = request.session.driver

    @pytest.fixture(scope="class", autouse=True)
    def setup(self,request):
        # 进入社保e贷-进件管理-复核信息查询页面
        self.driver(request)
        applyCentor = ApplyCentor(self.driver)
        sbed = Sbed(self.driver)
        fhxxcx = Fhxxcx(self.driver)
        applyCentor.to_sbed_apply()
        sbed.jjgl_Menu_click()
        fhxxcx.click_fhxxcx_Menu()
        yield
        page = Page(self.driver)
        page.open(applyCentorUrl)


    @allure.story("检查复核信息查询也没标题")
    @pytest.mark.parametrize('casedata',testData.get_testcase("test_fhxxcx001"))
    # @pytest.mark.skip(reason='先不测试')
    def test_title(self,casedata,request):

        """
        检查标题
        :return:
        """
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(casedata['id'],casedata['detail']))
        self.driver(request)
        fhxxcx = Fhxxcx(self.driver)
        title = fhxxcx.get_title()
        assert title == casedata['check']['title']

    @allure.story("检查基础查询输入框默认文案")
    @pytest.mark.parametrize('casedata',testData.get_testcase("test_fhxxcx002"))
    def test_baseQuery(self,casedata,request):

        """
        检查基础查询输入框默认文案
        :return:
        """
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(casedata['id'],casedata['detail']))
        self.driver(request)
        fhxxcx = Fhxxcx(self.driver)
        content = fhxxcx.get_baseQuery()
        assert content == casedata['check']['content']

    @allure.story("检查高级查询字段是否完整")
    @pytest.mark.parametrize('casedata',testData.get_testcase("test_fhxxcx003"))
    def test_search(self,casedata,request):

        """
        检查高级查询字段是否完整
        :return:
        """
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(casedata['id'],casedata['detail']))
        self.driver(request)
        fhxxcx = Fhxxcx(self.driver)
        content= fhxxcx.get_advanceQuery()
        assert content.strip(' ') == casedata['check']['content']

    @allure.story("检查客户群体下拉选项是否完整")
    @pytest.mark.parametrize('casedata',testData.get_testcase("test_fhxxcx004"))
    def test_searchCustomerOptions(self,casedata,request):

        """
        检查客户群体下拉选项是否完整
        :return:
        """
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(casedata['id'],casedata['detail']))
        self.driver(request)
        fhxxcx = Fhxxcx(self.driver)
        content= fhxxcx.get_khqtQuery_options()
        assert content == casedata['check']['content']

    @allure.story("检查调查状态下拉选项是否完整")
    @pytest.mark.parametrize('casedata',testData.get_testcase("test_fhxxcx005"))
    def test_searchDqjdOptions(self,casedata,request):

        """
        检查调查状态下拉选项是否完整
        :return:
        """
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(casedata['id'],casedata['detail']))
        self.driver(request)
        fhxxcx = Fhxxcx(self.driver)
        content= fhxxcx.get_investStatus_options()
        assert content.strip(' ') == casedata['check']['content']

    @allure.story("检查超时状态下拉选项是否完整")
    @pytest.mark.parametrize('casedata', testData.get_testcase("test_fhxxcx006"))
    def test_searchOverTimeStatusOptions(self, casedata, request):

        """
        检查超时状态下拉选项是否完整
        :return:
        """
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(casedata['id'], casedata['detail']))
        self.driver(request)
        fhxxcx = Fhxxcx(self.driver)
        content = fhxxcx.get_overTimeStatus_options()
        assert content.strip(' ') == casedata['check']['content']



    @allure.story("检查高级搜索-开始时间和结束时间默认时间是否正确")
    @pytest.mark.parametrize('casedata',testData.get_testcase("test_fhxxcx007"))
    def test_searchApplytime(self,casedata,request):

        """
        检查高级搜索-开始时间和结束时间默认时间是否正确
        :return:
        """
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(casedata['id'],casedata['detail']))
        self.driver(request)
        fhxxcx = Fhxxcx(self.driver)
        fhxxcx.searchButton_click()
        applyStartTime = fhxxcx.get_applyStartTime()
        applyEndTime = fhxxcx.get_applyEndTime()
        today = datetime.now().date()
        past_90_days = today - timedelta(days=90)
        assert str(past_90_days).replace("-", "/") == applyStartTime
        assert str(today).replace("-", "/") == applyEndTime

    @allure.story("检查表头字段是否完整")
    @pytest.mark.parametrize('casedata',testData.get_testcase("test_fhxxcx008"))
    def test_tableHeaders(self,casedata,request):

        """
        检查表头字段是否完整
        :return:
        """
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(casedata['id'],casedata['detail']))
        self.driver(request)
        fhxxcx = Fhxxcx(self.driver)
        content= fhxxcx.get_tableColName()
        assert content == casedata['check']['content']


    @allure.story("检查搜索和重置按钮功能")
    @pytest.mark.parametrize('casedata',testData.get_testcase("test_fhxxcx009"))
    def test_searchReset(self,casedata,request):

        """
        检查搜索功能是否正常，重置后查询输入框是否被清空
        :return:
        """
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(casedata['id'],casedata['detail']))
        self.driver(request)
        fhxxcx = Fhxxcx(self.driver)
        if casedata['screenshot'] == 'search':
            fhxxcx.input_baseQuery(casedata['data']['baseQuery'])
            fhxxcx.searchButton_click()
            time.sleep(5)
            content = fhxxcx.get_col_first_customer_name()
            assert content == "*" + casedata['check']['content'][1:]
        elif casedata['screenshot'] == 'reset':
            # fhxxcx.input_baseQuery("张三")
            # fhxxcx.searchButton_click()
            fhxxcx.resetButton_click()
            content= fhxxcx.get_baseQuery_value()
            assert content == ''



    @allure.story("检查点击客户姓名是否正常进入该客户详情页")
    @pytest.mark.parametrize('casedata',testData.get_testcase("test_fhxxcx010"))
    def test_toCustomerDetail(self,casedata,request):
        """
        检查点击客户姓名是否正常进入该客户详情页
        :return:
        """
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(casedata['id'],casedata['detail']))
        self.driver(request)
        fhxxcx = Fhxxcx(self.driver)
        # fhxxcx.input_baseQuery(casedata['data']['baseQuery'])
        fhxxcx.searchButton_click()
        time.sleep(5)
        col_name = fhxxcx.get_col_first_customer_name()
        fhxxcx.click_col_first_customer_name()
        name1 = fhxxcx.get_customer_name()
        assert col_name == "*" + name1[1:]
        fhxxcx.back()

