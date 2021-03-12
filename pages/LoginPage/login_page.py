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
import os
from pages.pages import BasePageElements
from common.base import BaseOperation

current_dir = os.path.abspath(os.path.dirname(__file__))


class LoginPage(BaseOperation, BasePageElements):
    def __init__(self, driver):
        BaseOperation.__init__(self, driver)
        BasePageElements.__init__(self, '', 'Login.yml', current_dir)

    @allure.step('输入邮箱地址')
    def send_email(self, email_address: str):
        self.send_key(self.locator("email_addr"), email_address)

    @allure.step("清空邮箱输入框")
    def clear_email_input_box(self):
        self.clear_input_box(self.locator("email_addr"))

    @allure.step('输入密码')
    def send_password(self, password: str):
        self.send_key(self.locator("password"), password)

    @allure.step('点击登录按钮')
    def click_login_btn(self):
        self.click(self.locator("login_btn"))


if __name__ == '__main__':
    from selenium import webdriver
    from selenium.webdriver import ChromeOptions

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    login_page = LoginPage(driver)
    print(login_page.info)
    # print(LoginPage.__mro__)
