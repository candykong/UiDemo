# _*_ coding:utf-8 _*_
__author__ = 'kongzhibing'


import os,sys

from pageObj.base import Page
from util.GetYaml import getyaml

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import pytest
import  yaml
import allure
from config import setting
from pageObj.applyCentor_page import ApplyCentor
from util.log import Log

# try:
#     f =open(setting.TEST_DATA_YAML + '/' + 'applyCentor_data.yaml',encoding='utf-8')
#     testData = yaml.safe_load(f)
# except FileNotFoundError as file:
#     log = Log()
#     log.error("文件不存在：{0}".format(file))


testData = getyaml(setting.TEST_DATA_YAML + '/' + 'applyCentor_data.yaml')
applyCentorUrl=setting.applyCentorUrl

@pytest.mark.usefixtures("session_login")
@allure.feature("应用中心页面")
class Test_applyCentor():


    def driver(self,request):
        self.driver = request.session.driver

    @pytest.fixture(scope="class", autouse=True)
    def setup(self,request):
        self.driver(request)
        yield
        page = Page(self.driver)
        page.open(applyCentorUrl)



    @allure.story("点击各个应用中心，检查标题")
    @pytest.mark.parametrize('casedata',testData.get_testcase())
    def test_check_title(self,casedata,request):
        """
        从应用中心进入农e贷，检查标题
        :return:
        """

        log = Log()
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(casedata['id'],casedata['detail']))
        # 调用登录方法
        self.driver(request)
        applyCentor = ApplyCentor(self.driver)
        if casedata['screenshot'] == 'sbed_success':
            applyCentor.to_sbed_apply()
            title = applyCentor.check_sbed_title()
            assert title == casedata['check']['title']
            applyCentor.back()
        elif  casedata['screenshot'] == 'ned_success':
            applyCentor.to_ned_apply()
            title = applyCentor.check_ned_title()
            assert title == casedata['check']['title']
            applyCentor.back()

