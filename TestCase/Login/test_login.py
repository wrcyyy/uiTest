# -*- coding: utf-8 -*-

"""
------------------------------------
@Project : uiTest
@Time    : 2021/3/9 9:37
@Auth    : wrc
@Email   : wrcyyy@126.com
@File    : test_login.py
@IDE     : PyCharm
------------------------------------
"""
import allure
import time
import os

current_dir = os.path.dirname(__file__)


class TestLogin:
    @allure.story("Login")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("登录-界面检查")
    @allure.title('登录成功')
    def test_login_with_email_password(self, login_page, web_driver, tmp_path):
        login_page.open_login_page()
        login_page.send_email("wrcyyy@126.com")
        login_page.send_password("123456")
        login_page.click_login_btn()
        time.sleep(2)
        file_path = os.path.join(tmp_path, 'test.png')
        login_page.save_screenshot(file_path)
        allure.attach.file(file_path, attachment_type=allure.attachment_type.PNG)

    # def test_download(self, login_page):
    #     login_page.open_url('https://dldir1.qq.com/invc/tt/QQBrowser_Setup_qb10.exe')
    #     time.sleep(10)
