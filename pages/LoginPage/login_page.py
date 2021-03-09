# -*- coding: utf-8 -*-

"""
------------------------------------
@Project : uiTest
@Time    : 2021/3/9 14:53
@Auth    : wrc
@Email   : wrcyyy@126.com
@File    : login_page.py
@IDE     : PyCharm
------------------------------------
"""
import allure
from common.base import Base
from pages.pages import LoginPageElements


class LoginPage(Base):
    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)
        self.elements = LoginPageElements()

    @allure.step('输入邮箱地址')
    def send_email(self, email_address: str):
        self.send_key(self.elements.locator("email_addr"), email_address)

    @allure.step('输入密码')
    def send_password(self, password: str):
        self.send_key(self.elements.locator("password"), password)

    @allure.step('点击登录按钮')
    def click_login_btn(self):
        self.click(self.elements.locator("login_btn"))
