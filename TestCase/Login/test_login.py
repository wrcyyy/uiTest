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
import os
from common.assertion import Assert

current_dir = os.path.dirname(__file__)


class TestLogin:
    @allure.story("Login")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("登录-界面检查")
    @allure.title('使用不存在的用户进行登录')
    def test_login_with_does_not_exist_email(self, login_page, web_driver):
        login_page.open_login_page()
        login_page.send_email("wrcyyy@126.com")
        login_page.send_password("123456")
        login_page.click_login_btn()
        err_info = login_page.get_text(login_page.locator('error_info_by_interface'))
        Assert.assert_equal((err_info, '用户不存在'))

    @allure.story("Login")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("登录-界面检查")
    @allure.title('使用错误的邮箱进行登录')
    def test_login_with_bad_email(self, login_page, web_driver):
        login_page.open_login_page()
        login_page.send_email('wrcyyy')
        login_page.send_password('123456')
        err_info = login_page.get_text(login_page.locator('email_input_box_alert'))
        Assert.assert_equal((err_info, '请输入正确的邮箱!'))
