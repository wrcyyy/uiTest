# -*- coding: utf-8 -*-

"""
------------------------------------
@Project : uiTest
@Time    : 2021/3/9 14:17
@Auth    : wrc
@Email   : wrcyyy@126.com
@File    : base.py
@IDE     : PyCharm
------------------------------------
"""
import logging
import os
from selenium.webdriver.support.wait import WebDriverWait
import time
from utils.fileoperate import FileOperate


class Base:

    def __init__(self, driver):
        self.config_info = FileOperate.read_yaml(
            os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config', 'config.yml'))
        self.driver = driver
        self.timeout = 10
        self.poll_frequency = 0.5

    def open_url(self, url: str):
        try:
            self.driver.get(url)
            logging.info(f'成功打开：{url}')
        except Exception as e:
            logging.error(f'打开：{url}失败，错误信息：{e}')

    def find_elem(self, locator):
        """
        定位单个元素
        :param locator:
        :return:
        """
        if isinstance(locator, tuple):
            logging.info(f'正在使用{locator[0]}定位元素：{locator[1]}')
            try:
                elem = WebDriverWait(self.driver, self.timeout, self.poll_frequency).until(
                    lambda driver: driver.find_element(*locator))
                return elem
            except Exception as e:
                logging.error(f"元素定位失败：{e}")
                return None
        else:
            logging.error('locator参数类型错误，示例：(By.xpath,"****")')

    def find_elements(self, locator):
        """
        定位一组元素
        :param locator:
        :return:
        """
        if isinstance(locator, tuple):
            logging.info(f'正在使用{locator[0]}定位元素：{locator[1]}')
            try:
                elements = WebDriverWait(self.driver, self.timeout, self.poll_frequency).until(
                    lambda driver: driver.find_elements(*locator))
                return elements
            except Exception as e:
                logging.error(f"元素定位失败：{e}")
                return None
        else:
            logging.error('locator参数类型错误，示例：("css_selector","****")')

    def open_login_page(self):
        self.open_url(self.config_info['test_server_info']['url'])

    def send_key(self, locator: tuple, info: str):
        element = self.find_elem(locator)
        try:
            element.send_keys(info)
            logging.info(f'向{locator}输入{info}成功')
        except Exception as e:
            logging.error(f'向{locator}输入{info}失败')

    def click(self, locator):
        element = self.find_elem(locator)
        try:
            element.click()
            logging.info(f'点击元素成功：{locator}')
        except Exception as e:
            logging.error(f'点击元素失败！{locator}')
