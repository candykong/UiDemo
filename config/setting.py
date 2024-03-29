#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'kongzhibing'


import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
# from util.getIni import get_config


# 配置文件路径
CONFIG_DIR = os.path.join(BASE_DIR,"config","config.ini")
LOAN_CONFIG_DIR = os.path.join(BASE_DIR,"config","loanConfig.ini")
# 测试用例目录
TEST_DIR = os.path.join(BASE_DIR,"testcase")
# 日志目录
LOG_DIR = os.path.join(BASE_DIR,"logs")
# 测试数据文件
TEST_DATA_YAML = os.path.join(BASE_DIR,"testdata")
# 元素控件
TEST_Element_YAML = os.path.join(BASE_DIR,"testyaml")
# 测试结果路径、报告路径和备份路径
TEST_RESULTS = os.path.join(BASE_DIR,"tmp/allure_results")
TEST_REPORT = os.path.join(BASE_DIR,"report")
TEST_REPORTBACKUP = os.path.join(BASE_DIR,"reportBackup")

#流量回放目录
TRAFFIC_PLAYBAN_DIR = os.path.join(BASE_DIR,"trafficPlayback")

# #webdriver超时等待时间
# TIMEOUT=get_config('seleniumWaitTime','timeout')

#应用中心url

loginURL = 'http://36.7.144.246:6071/fins-console-sso/index.html#/login'
applyCentorUrl ='http://36.7.144.246:6071/fins-console-sso/index.html#/startUp'
# applyCentorUrl = get_config('WebURL','applyCentorUrl')
# loginURL = get_config('WebURL','loginURL')
#
# #项目信息
# projectname = get_config('projectInfo','projectName')
# reportType = get_config('projectInfo','reportType')