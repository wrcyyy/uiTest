# -*- coding: utf-8 -*-

"""
------------------------------------
@Project : uiTest
@Time    : 2021/3/9 17:10
@Auth    : wrc
@Email   : wrcyyy@126.com
@File    : run.py
@IDE     : PyCharm
------------------------------------
"""
import pytest
import os

current_dir = os.path.dirname(__file__)

pytest.main()
os.system(
    f"allure generate -c {os.path.join(current_dir, 'Report', 'allure-results')} -o \
{os.path.join(current_dir, 'Report', 'allure-report')}")
# os.system(f"allure open {os.path.join(os.path.dirname(__file__), 'Report', 'allure-report')}")
