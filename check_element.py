import time

import selenium.webdriver as webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObj.base import Page
from pageObj.sbed.sbed_page import Sbed


driver = webdriver.Chrome()
driver.maximize_window()  # 最大化窗口


# 打开网站
url = "http://36.7.144.246:6071/fins-console-sso/index.html#/login"
driver.get(url)
WebDriverWait(driver, 10)
#登录
username = driver.find_element(By.XPATH,"//input[@placeholder='请输入账号']")
password = driver.find_element(By.XPATH,"//input[@placeholder='请输入密码']")
login_button = driver.find_element(By.CSS_SELECTOR, "button.el-button.loginBtn")
username.send_keys("67710")
password.send_keys("123456Aa")
login_button.click()

time.sleep(2)
#点击社保e贷
element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH,"//div[@class='box-item-title' and text()='社宝e贷']"))
)
element.click()

#点击进件管理
sbed = Sbed(driver)
sbed.jjgl_Menu_click()


#点击贷款进度查询
element = WebDriverWait(driver, 15).until(
    EC.visibility_of_element_located((By.XPATH,"//span[text()='贷款进度查询']"))
)
element.click()

#
# #获取标题
# element = WebDriverWait(driver, 10).until(
#     EC.visibility_of_element_located((By.CLASS_NAME,"menu-header"))
# )
# print(element.text)
#
# #获取基础查询输入框内容
# element = WebDriverWait(driver, 10).until(
#     EC.visibility_of_element_located((By.CLASS_NAME,"el-input.el-input--small.el-input-group.el-input-group--append.el-input--suffix"))
# )
# print(element.text)
#
# #获取高级搜索字段名称
# elements = WebDriverWait(driver, 10).until(
#     EC.visibility_of_all_elements_located((By.CLASS_NAME,"el-form-item__label"))
# )
# contents = []
# for element in elements:
#     content = element.text
#     contents.append(content)
# print(' '.join(contents))

#获取客户群体下拉选项
# customer_group_input = WebDriverWait(driver, 15).until(
#     EC.visibility_of_element_located((By.XPATH, "//div[@class='el-form-item__content']//label[text()='客户群体：']/following-sibling::div//input[@placeholder='请选择']"))
# )

# customer_group_input = WebDriverWait(driver, 10).until(
#     EC.visibility_of_element_located((By.XPATH, '//div[contains(text(), "客户群体:")]/following-sibling::div//input[@class="el-input__inner"]'))
# )

# customer_group_input = WebDriverWait(driver, 10).until(
#     EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.el-form-item__content:contains("客户群体:") input.el-input__inner'))
# )
input_box = WebDriverWait(driver, 10).until(
    EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'input[placeholder="请选择"]'))
)
# text0 = input_box[0].text
text0 = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/section/section/main/section/div/div/div[2]/form/div[2]/div[2]/div/div/div/input'))
).text

print(text0)
input_box[0].click()

# 获取客户群体选项
WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.XPATH,'/html/body/div[2]/div[1]/div[1]/ul/li[1]'))
).click()
text1 = input_box[0].text
print(text1)
# 获取客户群体选项
# span_elements = WebDriverWait(driver,10).until(
#     EC.visibility_of_all_elements_located((By.XPATH,'/html/body/div[2]/div[1]/div[1]/ul/li'))
# )
# # 遍历每个<span>元素并获取文本内容
# print('客户群体选项：'+'\n')
# for span_element in span_elements:
#     content = span_element.text
#     print(content)

# # 获取当前进度选项
# input_box = WebDriverWait(driver, 10).until(
#     EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'input[placeholder="请选择"]'))
# )
# input_box[1].click()
# span_elements = WebDriverWait(driver, 10).until(
#     EC.visibility_of_all_elements_located((By.XPATH, '/html/body/div[3]/div[1]/div[1]/ul/li'))
# )
#
# # 遍历每个<span>元素并获取文本内容
# print('当前进度选项' + '\n')
# for span_element in span_elements:
#     content = span_element.text
#     print(content)

# # 关闭浏览器
# driver.quit()

# elements = WebDriverWait(driver, 10).until(
#     EC.visibility_of_all_elements_located((By.XPATH,"//div[@class='el-select-dropdown__wrap']//ul[@class='el-select-dropdown__list']"))
# )
# contents = []
# for element in elements:
#     content = element.text
#     contents.append(content)
# print(' '.join(contents))


