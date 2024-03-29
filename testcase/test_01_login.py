# _*_ coding:utf-8 _*_
__author__ = 'kongzhibing'


import os,sys
import time

from util.GetYaml import getyaml

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import pytest
import  yaml
import allure
from config import setting
from pageObj.login_page import Login
from util.log import Log

# try:
#     f =open(setting.TEST_DATA_YAML + '/' + 'login_data.yaml',encoding='utf-8')
#     testData = yaml.safe_load(f)
# except FileNotFoundError as file:
#     log = Log()
#     log.error("文件不存在：{0}".format(file))

testData = getyaml(setting.TEST_DATA_YAML + '/' + 'login_data.yaml')

@pytest.mark.usefixtures("init_driver")
@allure.feature("测试登录页面")
class Test_login():


    """登录测试"""
    def user_login_verify(self,account,password):
        """
        用户登录
        :param phone: 手机号
        :param password: 密码
        :return:
        """
        Login(self.driver).user_login(account,password)




    @allure.story("登录接口")
    @pytest.mark.parametrize('casedata',testData.get_testcase())
    @pytest.mark.dependency(name='test_login')
    def test_login(self,casedata):
        """
        登录测试
        :param datayaml: 加载login_data登录测试数据
        :return:
        """
        log = Log()
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(casedata['id'],casedata['detail']))
        # 调用登录方法
        self.user_login_verify(casedata['data']['account'],casedata['data']['password'])
        time.sleep(3)
        assert Login(self.driver).on_page(casedata['check']['current_url'])
