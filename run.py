# -*- coding: utf-8 -*-

import os
import datetime
import pytest
import subprocess
import shutil
import socket
import time
from util import network
from util.feishu import send_feishu_message
from config import setting
from util.file import delete_dir_file,move_file,get_latest_report
from util.getIni import get_config

#项目信息

projectName = get_config('projectInfo','projectName')
reportType = get_config('projectInfo','reportType')

report_path=setting.TEST_REPORT
backup_path=setting.TEST_REPORTBACKUP
results_path=setting.TEST_RESULTS

def backup_allure_report(report_path, backup_path):
    """
    备份以前的报告
    :param report_path:
    :param backup_path:
    :return:
    """
    # shutil.copytree(report_path, backup_path)
    move_file(report_path,backup_path)


def generate_allure_report(results_path, report_path):
    """
    生成新的报告
    :param results_path:
    :param report_path:
    :return:
    """
    report_path = os.path.join(report_path, datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
    command = ["allure", "generate", results_path, "-o", report_path, "--clean"]
    subprocess.run(command)

def run_tests(results_path):
    # 将之前的结果清楚，再运行测试用例并生成结果
    delete_dir_file(results_path)
    # pytest.main(["testCase/test_login.py", f"--alluredir={results_path}"])
    pytest.main([ f"--alluredir={results_path}"])



def open_allure_report(ip, port, report_path):
    #打开最新的报告
    report_path = get_latest_report(report_path)
    command = ["allure", "open", "-h", ip, "-p", str(port), report_path]
    subprocess.run(command)


if __name__ == "__main__":
    #备份报告
    backup_allure_report(report_path,backup_path)
    #运行用例
    run_tests(results_path)
    #生成报告
    generate_allure_report(results_path,report_path)

    #获取ip地址
    ip= network.get_ip_address()
    port = 8883
    # projectName = setting.projectname
    # reportType = setting.reportType
    #发送查看报告路径--飞书群内机器人
    # webhook_url = 'https://open.feishu.cn/open-apis/bot/v2/hook/3a029b35-396c-46c7-8f53-133efc1ee78f'
    # message = f"请查看{projectName}的{reportType}报告：http://{ip}:{port}/index.html"
    # send_feishu_message(webhook_url, message)
    #打开报告
    open_allure_report(ip, port, report_path)




