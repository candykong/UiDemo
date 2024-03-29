# _*_ coding:utf-8 _*_
__author__ = 'kongzhibing'


import os,sys

from pageObj.base import Page

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import pytest
import allure
from config import setting
from pageObj.applyCentor_page import ApplyCentor
from pageObj.sbed.sbed_page import Sbed
from util.log import Log
from util.GetYaml import getyaml

log = Log()
testData = getyaml(setting.TEST_DATA_YAML + '/sbed/' + 'sbed_data.yaml')
applyCentorUrl=setting.applyCentorUrl

# @pytest.mark.usefixtures("to_sbed")
@pytest.mark.usefixtures("session_login")
@allure.feature("社保e贷页面")
class Test_sbed():

    def driver(self,request):
        self.driver = request.session.driver

    @pytest.fixture(scope="class", autouse=True)
    def setup(self,request):
        # 进入社宝e贷
        self.driver(request)
        applyCentor = ApplyCentor(self.driver)
        applyCentor.to_sbed_apply()
        yield
        page = Page(self.driver)
        page.open(applyCentorUrl)

    @allure.story("检查社保e贷首页个人信息")
    @pytest.mark.parametrize('casedata',testData.get_testcase("test_sbed001"))
    # @pytest.mark.skip(reason='先不测试')
    def test_accountInfo(self,casedata,request):

        """
        从应用中心进入社保e贷，检查标题
        :return:
        """
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(casedata['id'],casedata['detail']))
        self.driver(request)
        sbed = Sbed(self.driver)
        account=sbed.check_account()
        org = sbed.check_org()
        phone = sbed.check_phone()
        assert account == casedata['check']['account']
        assert org == casedata['check']['org']
        assert phone == casedata['check']['phone']

    @allure.story("检查社保e贷父级菜单")
    @pytest.mark.parametrize('casedata',testData.get_testcase("test_sbed002"))
    def test_parentMenus(self,casedata,request):
        """
        进入社保e贷检查父级菜单
        :param casedata:
        :return:
        """
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(casedata['id'], casedata['detail']))
        self.driver(request)
        sbed = Sbed(self.driver)
        parentMenus=sbed.check_parentMenus()
        assert parentMenus== casedata['check']['menus']


    # @pytest.mark.skip(reason='先不测试')
    @allure.story("检查社保e贷各个父级菜单的子菜单")
    @pytest.mark.parametrize('casedata',testData.get_testcase("test_sbed003"))
    def test_subMenus(self,casedata,request):
        self.driver(request)
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(casedata['id'], casedata['detail']))
        sbed = Sbed(self.driver)
        if casedata['screenshot'] == 'jjgl_submemus':
            jjgl_submenus = sbed.check_jjgl_sbumenus()
            assert jjgl_submenus == casedata['check']['submenus']
        elif casedata['screenshot'] == 'dhgl_submemus':
            dhgl_submenus = sbed.check_dhgl_sbumenus()
            assert dhgl_submenus == casedata['check']['submenus']
        elif casedata['screenshot'] == 'dhougl_submemus':
            dhougl_submenus = sbed.check_dhougl_sbumenus()
            assert dhougl_submenus == casedata['check']['submenus']
        elif casedata['screenshot'] == 'ycgl_submemus':
            ycgl_submenus = sbed.check_ycgl_sbumenus()
            assert ycgl_submenus == casedata['check']['submenus']
        elif casedata['screenshot'] == 'ywpz_submemus':
            ywpz_submenus = sbed.check_ywpz_sbumenus()
            assert ywpz_submenus == casedata['check']['submenus']
        elif casedata['screenshot'] == 'dhspgl_submemus':
            dhspgl_submenus = sbed.check_dhspgl_sbumenus()
            assert dhspgl_submenus == casedata['check']['submenus']



