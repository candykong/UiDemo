#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'kongzhibing'

import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from config import setting
import configparser


def get_config(section,option_key):
    # --------- 读取config.ini配置文件 ---------------
    con = configparser.ConfigParser(interpolation=None)
    con.read(setting.CONFIG_DIR, encoding='utf-8')
    return con.get(section, option_key)

def get_loan_config(section,option_key):
    # --------- 读取loanConfig.ini配置文件 ---------------
    con = configparser.ConfigParser(interpolation=None)
    con.read(setting.LOAN_CONFIG_DIR, encoding='utf-8')
    return con.get(section, option_key)

