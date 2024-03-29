import time
import os,sys
from datetime import datetime, timedelta

import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from pageObj.sbed.sbed_page import Sbed
from pageObj.sbed.jjgl.dkjdcx_page import Dkjdcx
from pageObj.sbed.jjgl.fhxxcx_page import Fhxxcx
from pageObj.applyCentor_page import ApplyCentor



import os,sys

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

driver = webdriver.Chrome()
driver.maximize_window()  # 最大化窗口

my_action = webdriver.ActionChains(driver)

applyCentor = ApplyCentor(driver)
Sbed=Sbed(driver)
Dkjdcx=Dkjdcx(driver)
fhxxcx=Fhxxcx(driver)

# 打开网站
url = "http://36.7.144.246:6071/fins-console-sso/index.html#/login"
Sbed.open(url)
WebDriverWait(driver, 10)
#登录
username = Sbed.find_element(By.XPATH,"//input[@placeholder='请输入账号']")
password = Sbed.find_element(By.XPATH,"//input[@placeholder='请输入密码']")
login_button = Sbed.find_element(By.CSS_SELECTOR, "button.el-button.loginBtn")
username.send_keys("67710")
password.send_keys("123456Aa")
login_button.click()

time.sleep(2)
#点击社保e贷
# element = WebDriverWait(Sbed, 10).until(
#     EC.visibility_of_element_located((By.XPATH,"//div[@class='box-item-title' and text()='社宝e贷']"))
# )
# element .click()

applyCentor.to_sbed_apply()
time.sleep(2)
Sbed.change_role('电调管理员')


# #切换角色
# element = WebDriverWait(Sbed, 10).until(
#     EC.visibility_of_element_located((By.CLASS_NAME,"title-card.role-color.el-dropdown-selfdefine "))
# )
#
# # 将鼠标移动到指定的元素
# my_action.move_to_element(element).perform()
#
# # 等待下拉菜单可见
# # dropdown_menu = WebDriverWait(driver, 10).until(
# #     EC.visibility_of_all_elements_located((By.CLASS_NAME, "el-dropdown-menu.el-popper.el-dropdown-menu--small"))
# # )
#
# dropdown_menus = driver.find_elements(By.CLASS_NAME, "el-dropdown-menu.el-popper.el-dropdown-menu--small")
#
# dropdown_menu = dropdown_menus[2].find_element(By.XPATH, ".//div[contains(text(), '电调管理员')]")
# # print(dropdown_menu.text)
# my_action.move_to_element(dropdown_menu).perform()
# dropdown_menu.click()
time.sleep(5)
# 打印所有选项的文本
# for option in options:
#     print(option.text)

# # 遍历所有下拉菜单
# for dropdown_menu in dropdown_menus:
#     # 找到下拉菜单中的所有选项
#     options = dropdown_menu.find_elements(By.CLASS_NAME, "el-dropdown-menu__item")
#
#     # 打印所有选项的文本
#     for option in options:
#         print(option.text)

# # 找到 "修改密码" 链接并点击
# modify_password_link = dropdown_menu[2].find_element(By.t, "电调管理员")
# my_action.move_to_element(modify_password_link).perform()
# modify_password_link.click()
# time.sleep(5)


#点击进见管理
# Sbed.jjgl_Menu_click()
# Dkjdcx.click_dkjdcx_Menu()
# Dkjdcx.input_baseQuery('仲营营')
# Dkjdcx.searchButton_click()
# col_name = Dkjdcx.get_col_first_customer_name()
# print(col_name)
# str1 = '仲营营'
# if(col_name == ("*" + str1[1:])):
#     print('查询结果正确')
# Dkjdcx.click_col_first_customer_name()
# name = Dkjdcx.get_customer_name()
# print(name)
#
# fhxxcx.click_fhxxcx_Menu()
# title = fhxxcx.get_title()
# print('复核信息查询标题为：'+title)
# str1 = fhxxcx.get_baseQuery()
# str2 = fhxxcx.get_baseQuery_value()
# print('复核信息基础查询输入框默认文案为：'+str1+',复核信息基础查询输入框默认值为：'+str2)
# searchStr = fhxxcx.get_advanceQuery()
# print('复核信息高级查询字段为：'+searchStr)
# fhxxcx.searchButton_click()
# time.sleep(1)
# applyStartTime = fhxxcx.get_applyStartTime()
# print('复核信息高级查询-开始时间字段为：'+applyStartTime)
# colNames = fhxxcx.get_tableColName()
# print('复核信息列表字段有：'+colNames)

# khqt = fhxxcx.get_khqtQuery_options()
# investStatus = fhxxcx.get_investStatus_options()
# overTimeStatus = fhxxcx.get_overTimeStatus_options()
#
# print('客户群体有：'+khqt)
# print('调查状态有：'+investStatus)
# print('超时状态有：'+overTimeStatus)




#点击贷款进度查询
#//a[@href="#/loan-progress"]








# 定位客户群体下拉选项
# dropdown = driver.find_elements(By.CSS_SELECTOR,".el-select-dropdown__wrap")
# length = len(dropdown)-1
# print(length)
# # 定位所有选项
# options = dropdown[1].find_elements(By.CSS_SELECTOR,".el-select-dropdown__item span")
# # 打印所有下拉选项的文本
# for option in options:
#     print(option.text)
# options[0].click()
# time.sleep(2)

# basequery = Dkjdcx.get_baseQuery()
# print("基础查询默认文字：")
# print(basequery)
# Dkjdcx.baseQuery("张三")
# basequery = Dkjdcx.get_baseQuery_updated()
# print("基础查询文字：")
# print(basequery)
# start = Dkjdcx.get_applyStartTime()
# print("开始时间：")
# print(start)
# end = Dkjdcx.get_applyEndTime()
# print("结束时间：")
# print(end)


# element = WebDriverWait(Sbed, 10).until(
#     EC.visibility_of_element_located((By.CLASS_NAME,"el-button.el-button--primary.el-button--small"))
# )
#
# time.sleep(2)
# element2 = WebDriverWait(Sbed, 10).until(
#     EC.visibility_of_element_located((By.CLASS_NAME,"el-button.el-button--primary.el-button--small.is-plain"))
# )
# time.sleep(2)

# 获取表头元素
#
# elements = WebDriverWait(Sbed, 10).until(
#     EC.visibility_of_all_elements_located((By.CLASS_NAME,"el-table__header"))
# )
# # 打印表头文本
# print("列表字段有：")
# for element in elements:
#     print(element.text)

# names = Dkjdcx.get_tableColName()
# print("列表字段有：")
# print(names)

# Dkjdcx.input_applyStartTime('2023/08/08')
# Dkjdcx.input_applyEndTime('2023/08/09')
# start = Dkjdcx.get_applyStartTime()
# print("开始时间：")
# print(start)
# end = Dkjdcx.get_applyEndTime()
# print("结束时间：")
# print(end)

#日历自动化

#结束时间
# element = WebDriverWait(Sbed, 10).until(
#     EC.visibility_of_all_elements_located((By.CLASS_NAME,"el-input__inner"))
# )[7]
# element.click() #调其日历

# rl = WebDriverWait(driver, 10).until(
#     EC.visibility_of_all_elements_located((By.CLASS_NAME, 'el-picker-panel.el-date-picker.el-popper'))
# )
# length = len(rl)-1
# print(length)
# date_element = rl[length].find_elements(By.XPATH, '//tbody/tr/td[@class="available"]')[0]
# date_element.click()
# print('当前结束时间值为：',element.get_attribute("value"))


# rl = driver.find_elements(By.CLASS_NAME,'el-picker-panel.el-date-picker.el-popper')
# length = len(rl)-1
# print(length)
# yearmonth= rl[length].find_elements(By.CLASS_NAME, 'el-date-picker__header-label')  #当前年月
# date=''
# for yearormonth in yearmonth:
#     date = date+yearormonth.text
# print('当前年月为：',date)

# date_element1 = rl[length].find_elements(By.XPATH, '//tbody/tr/td[@class="available"]')
# for date in date_element1:
#     if date.text != '':
#         date.click()
#         break

# rl[length].find_element(By.CSS_SELECTOR, 'button[aria-label="前一年"]').click()
# time.sleep(2)
# rl[length].find_element(By.CSS_SELECTOR, 'button[aria-label="后一年"]').click()
# time.sleep(2)
# rl[length].find_element(By.CSS_SELECTOR, 'button[aria-label="上个月"]').click()
# time.sleep(2)
# rl[length].find_element(By.CSS_SELECTOR, 'button[aria-label="下个月"]').click()
# time.sleep(2)

#
#
# day = rl[length].find_element(By.XPATH, '//tbody/tr/td[@class="available"]/div/span[normalize-space()="{}"]'.format(15))
# day.click()
#
# print('当前结束时间值为：',element.get_attribute("value"))
#
# #开始时间
# element1 = WebDriverWait(Sbed, 10).until(
#     EC.visibility_of_all_elements_located((By.CLASS_NAME,"el-input__inner"))
# )[6]
# element1.click() #调其日历
#
# # rl1 = WebDriverWait(driver, 10).until(
# #     EC.visibility_of_all_elements_located((By.CLASS_NAME, 'el-picker-panel.el-date-picker.el-popper'))
# # )
# rl1 = driver.find_elements(By.CLASS_NAME,'el-picker-panel.el-date-picker.el-popper')
# length1 = len(rl1)-1
# # print(length1)
# date_element1 = rl1[length1].find_elements(By.XPATH, '//tbody/tr/td[@class="available"]')
# date_current1 = rl1[length1].find_elements(By.XPATH, '//tbody/tr/td[@class="available.current"]')  #当前日期
# # for date in date_element1:
# #     if date.text != '':
# #         # date.click()
# #         print(date.text)
# #         break
# for date_current in date_current1:
#     print('当前号：',date_current.text)
#     # if date_current.text != '':
#     #     # date_current.click()
#     #     print(date_current.text)
#     #     break
# yearmonth= rl1[length1].find_elements(By.CLASS_NAME, 'el-date-picker__header-label')  #当前年月
# for yearormonth in yearmonth:
#     print('当前年月为：',yearormonth.text)
#
# print('当前开始时间值为：',element1.get_attribute("value"))





# #下拉框选择
# element = WebDriverWait(Sbed, 10).until(
#     EC.visibility_of_all_elements_located((By.CLASS_NAME,"el-input__inner"))
# )[2]
# element.send_keys('公职上班群体')   #方法不行，需要使用选项click()





# 重置和搜索
# element1 = WebDriverWait(Sbed, 10).until(
#     EC.visibility_of_element_located((By.CLASS_NAME,"el-button.el-button--primary.el-button--small"))
# )
# element1.click()
#
# time.sleep(2)
# element2 = WebDriverWait(Sbed, 10).until(
#     EC.visibility_of_element_located((By.CLASS_NAME,"el-button.el-button--primary.el-button--small.is-plain"))
# )
# element2.click()
# time.sleep(2)



# for element in elements:
#     print(element.get_attribute("placeholder"))
#     print(element.get_attribute("value"))
# element = elements[0]
# basequery=element.get_attribute("value")
# print("基础查询框文案：")
# print(basequery)
# # my_action.move_to_element(element).perform()
# # driver.execute_script("arguments[0].style.display = 'block';", element)
# element.send_keys('张三')
# # basequery=element.get_attribute("placeholder")
# basequery=element.get_attribute("value")
# # basequery = Dkjdcx.get_baseQuery()
# print("基础查询框文案：")
# print(basequery)

#基础查询按钮
#
# element = WebDriverWait(Sbed, 10).until(
#     EC.visibility_of_element_located((By.CLASS_NAME,'el-button.el-button--default.el-button--small'))
# )
# element.click()
# time.sleep(3)



# advancequery = Dkjdcx.get_advanceQuery()
# print("高级查询框字段：")
# print(advancequery)
#
# print("群体选项如下：")
# options =Dkjdcx.get_khqtQuery_options()
# print(options)
# time.sleep(2)

# #选择城乡居民
# Dkjdcx.select_khqtQuery_options('城乡居民群体')
# time.sleep(2)
#
# Dkjdcx.select_dqjdQuery_options('已完成')
# time.sleep(2)



# print("当前进度选项如下：")
# options =Dkjdcx.get_dqjdQuery_options()
# print(options)
# #

#
# #点击当前进度
# element = WebDriverWait(Sbed, 10).until(
#     EC.visibility_of_element_located((By.XPATH,'//*[@id="app"]/section/section/main/section/div/div/div[2]/form/div[2]/div[3]/div/div/div/input'))
# )
# element .click()
#
#
#
# # 定位客户群体下拉选项
# dropdown = driver.find_elements(By.CSS_SELECTOR,".el-select-dropdown__wrap")
# print(len(dropdown))
# # 定位所有选项
# options = dropdown[0].find_elements(By.CSS_SELECTOR,".el-select-dropdown__item span")
# # 打印所有下拉选项的文本
# print("0:")
# for option in options:
#     print(option.text)
#
# options = dropdown[1].find_elements(By.CSS_SELECTOR,".el-select-dropdown__item span")
# # 打印所有下拉选项的文本
# print("1:")
# for option in options:
#     print(option.text)
#
# options = dropdown[2].find_elements(By.CSS_SELECTOR,".el-select-dropdown__item span")
# # 打印所有下拉选项的文本
# print("2:")
# for option in options:
#     print(option.text)
#
# options = dropdown[3].find_elements(By.CSS_SELECTOR,".el-select-dropdown__item span")
# # 打印所有下拉选项的文本
# print("3:")
# for option in options:
#     print(option.text)


#
# #点击客户群体
# element = WebDriverWait(Sbed, 10).until(
#     EC.visibility_of_element_located((By.XPATH,'//*[@id="app"]/section/section/main/section/div/div/div[2]/form/div[2]/div[2]/div/div/div/input'))
# )
# element .click()
# # # 获取所有群体名称并打印
# # group_elements = driver.find_elements(By.CSS_SELECTOR,".el-select-dropdown__item span")
#
# # 定位客户群体下拉选项
# dropdown = driver.find_elements(By.CSS_SELECTOR,".el-select-dropdown__wrap")
# print(len(dropdown))
# # 定位所有选项
# options = dropdown[0].find_elements(By.CSS_SELECTOR,".el-select-dropdown__item span")
# # 打印所有下拉选项的文本
# print("0:")
# for option in options:
#     print(option.text)
#
# options = dropdown[1].find_elements(By.CSS_SELECTOR,".el-select-dropdown__item span")
# # 打印所有下拉选项的文本
# print("1:")
# for option in options:
#     print(option.text)
#
# options = dropdown[2].find_elements(By.CSS_SELECTOR,".el-select-dropdown__item span")
# # 打印所有下拉选项的文本
# print("2:")
# for option in options:
#     print(option.text)
#
# options = dropdown[3].find_elements(By.CSS_SELECTOR,".el-select-dropdown__item span")
# # 打印所有下拉选项的文本
# print("3:")
# for option in options:
#     print(option.text)

#
# print("群体选项如下：")
# groupNames=[]
# for group in group_elements:
#     groupname=group.text
#     if groupname !='':
#         groupNames.append(groupname)
# print(' '.join(groupNames))





time.sleep(2)
driver.quit()




