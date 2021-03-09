# -*- coding: utf-8 -*-

"""
------------------------------------
@Project : uiTest
@Time    : 2021/3/9 16:07
@Auth    : wrc
@Email   : wrcyyy@126.com
@File    : conftest.py
@IDE     : PyCharm
------------------------------------
"""
import pytest
from pages.LoginPage.login_page import LoginPage


@pytest.fixture(scope='function')
def login_page(web_driver):
    return LoginPage(web_driver)
