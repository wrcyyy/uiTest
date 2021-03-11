# -*- coding: utf-8 -*-

"""
------------------------------------
@Project : uiTest
@Time    : 2021/3/9 9:08
@Auth    : wrc
@Email   : wrcyyy@126.com
@File    : conftest.py
@IDE     : PyCharm
------------------------------------
"""
import allure
import logging
import os
import pytest
from selenium import webdriver
import sys

download_dir = os.path.join(os.path.dirname(__file__), 'asset')
driver = None


def pytest_addoption(parser):
    """
    增加运行参数
    :param parser:
    :return:
    """
    # 传入浏览器类型
    parser.addoption("--browser", action="store", default="chrome", help="browser option:chrome|firefox|ie")
    # 传入是否打开可视化界面参数
    parser.addoption("--ui", action="store", default="open", help="whether use ui:open|close")


@pytest.fixture(scope='session')
def web_driver(request):
    """
    :param request:
    :return:
    """
    global driver
    browser = request.config.getoption("--browser")
    ui = request.config.getoption("--ui")
    chrome_options = webdriver.ChromeOptions()
    firefox_options = webdriver.FirefoxOptions()
    ie_options = webdriver.IeOptions()

    # chrome自定义配置
    # chrome_options.add_argument('--ignore-certificate-errors')
    chrome_prefs = {
        'profile.default_content_settings.popups': 0,
        'download.default_directory': download_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing_for_trusted_sources_enabled": False,
        "safebrowsing.enabled": False
    }
    chrome_options.add_experimental_option('prefs', chrome_prefs)
    # 火狐自定义配置
    firefox_options.accept_insecure_certs = True
    firefox_options.set_preference("browser.download.dir", download_dir)
    firefox_options.set_preference("browser.download.manager.showWhenStarting", False)
    firefox_options.set_preference("browser.download.folderList", 2)
    # 查看请求中的文件类型即可
    firefox_options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
    if ui == 'close':
        chrome_options.add_argument('--headless')
        firefox_options.add_argument('--headless')
        ie_options.add_argument('--headless')
    if browser.upper() == "CHROME":
        driver = webdriver.Chrome(options=chrome_options)
        driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
        params = {'cmd': 'Page.setDownloadBehavior',
                  'params': {'behavior': 'allow', 'downloadPath': download_dir}}
        driver.execute("send_command", params)
    elif browser.upper() == "FIREFOX":
        driver = webdriver.Firefox(options=firefox_options)
    # elif browser.upper() == "IE":
    #     ...
    else:
        logging.error(f"不支持的浏览器{browser}")
        sys.exit()
    driver.maximize_window()
    yield driver
    driver.close()
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport():
    """
    对断言失败的用例进行截图
    :return:
    """
    outcome = yield
    rep = outcome.get_result()
    # 这里只处理实际执行失败的用例，跳过setup/teardown
    if rep.when == "call" and rep.failed:
        if hasattr(driver, "get_screenshot_as_png"):
            allure.attach(driver.get_screenshot_as_png(), '失败截图', allure.attachment_type.PNG)
