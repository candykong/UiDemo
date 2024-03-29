import pytest
from selenium import webdriver
from pageObj.login_page import Login
from util.getIni import get_config


def setup_driver():
    """
    初始化driver
    :return:
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver

# def teardown_driver(driver):
#     """退出浏览器"""
#     driver.quit()
#
# def pytest_sessionfinish(session, exitstatus):
#     teardown_driver(session.driver)

@pytest.fixture(scope="class", autouse=False)
def init_driver(request):
    driver = setup_driver()
    request.cls.driver = driver
    yield
    request.cls.driver = None
    driver.quit()

@pytest.fixture(scope="session", autouse=False)
def session_login(request):
    driver = setup_driver()
    request.session.driver = driver
    Login(driver).user_login(get_config('adminUser','account'), get_config('adminUser','password'))
    yield
    driver.quit()


# @pytest.fixture(scope="class", autouse=True)
@pytest.fixture(scope="class")
def class_login(request):
    driver = setup_driver()
    request.cls.driver = driver
    Login(driver).user_login(get_config('adminUser','account'), get_config('adminUser','password'))
    yield
    driver.quit()

# def driver(request):
#     global driver
#     driver = request.session.driver
#     return driver

def pytest_collection_modifyitems(config,items):
    #先执行登录
    ordered_items = []
    for item in items:
        if item.name == "test_login":
            ordered_items.insert(0, item)  # 将"test_case2"用例插入到列表首位
        else:
            ordered_items.append(item)
    items[:] = ordered_items

