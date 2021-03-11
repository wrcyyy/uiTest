# -*- coding: utf-8 -*-

"""
------------------------------------
@Project : uiTest
@Time    : 2021/3/11 14:08
@Auth    : wrc
@Email   : wrcyyy@126.com
@File    : assertion.py
@IDE     : PyCharm
------------------------------------
"""
import pytest


class Assert:

    @staticmethod
    def assert_equal(info: tuple):
        """
        判断tuple中的两个对象相等
        :param info:
        :return:
        """
        __tracebackhide__ = True
        if info[0] != info[1]:
            pytest.fail(f'断言失败！【{info[0]}】和【{info[1]}】不相等')

    @staticmethod
    def assert_gt(info: tuple):
        __tracebackhide__ = True
        if info[0] <= info[1]:
            pytest.fail(f'断言失败！【{info[0]}】小于等于【{info[1]}】')

    @staticmethod
    def assert_gte(info: tuple):
        __tracebackhide__ = True
        if info[0] < info[1]:
            pytest.fail(f'断言失败！【{info[0]}】小于【{info[1]}】')

    @staticmethod
    def assert_lt(info: tuple):
        __tracebackhide__ = True
        if info[0] >= info[1]:
            pytest.fail(f'断言失败！【{info[0]}】大于等于【{info[1]}】')

    @staticmethod
    def assert_lte(info: tuple):
        __tracebackhide__ = True
        if info[0] > info[1]:
            pytest.fail(f'断言失败！【{info[0]}】大于【{info[1]}】')

    @staticmethod
    def assert_contain(info: tuple):
        __tracebackhide__ = True
        if info[0] not in info[1]:
            pytest.fail(f'断言失败！【{info[1]}】不包含【{info[0]}】')
