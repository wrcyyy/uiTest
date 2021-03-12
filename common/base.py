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
from selenium.webdriver.common.keys import Keys
from utils.fileoperate import FileOperate


class BaseOperation:

    def __init__(self, driver):
        self.__config_info = FileOperate.read_yaml(
            os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config', 'config.yml'))
        self.__driver = driver
        self.__timeout = 10
        self.__poll_frequency = 0.5

    def clear_input_box(self, locator: tuple):
        """
        清空输入框内容
        :param locator:
        :return:
        """
        element = self.find_elem(locator)
        try:
            element.send_keys(Keys.CONTROL, 'a')
            element.send_keys(Keys.BACKSPACE)
            logging.info(f'输入框内容已清空')
        except Exception as e:
            logging.error(f'清除输入框失败！{locator}，{e}')

    def open_url(self, url: str):
        try:
            self.__driver.get(url)
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
                elem = WebDriverWait(self.__driver, self.__timeout, self.__poll_frequency).until(
                    lambda driver: driver.find_element(*locator))
                return elem
            except Exception as e:
                logging.error(f"元素定位失败！{locator}，{e}")
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
                elements = WebDriverWait(self.__driver, self.__timeout, self.__poll_frequency).until(
                    lambda driver: driver.find_elements(*locator))
                return elements
            except Exception as e:
                logging.error(f"元素定位失败！{locator}，{e}")
                return None
        else:
            logging.error('locator参数类型错误，示例：("css_selector","****")')

    def get_text(self, locator: tuple):
        """
        获取元素的text
        :param locator:
        :return:
        """
        element = self.find_elem(locator)
        try:
            logging.info(f'获取元素text成功：{element.text}')
            return element.text
        except Exception as e:
            logging.error(f'获取元素text失败！{locator}，{e}')
            return None

    def get_placeholder_info(self, locator: tuple):
        element = self.find_elem(locator)
        try:
            logging.info(f'获取placeholder成功：{element.get_attribute("placeholder")}')
            return element.get_attribute("placeholder")
        except Exception as e:
            logging.error(f'获取placeholder失败,{locator}，{e}')
            return None

    def open_login_page(self):
        """
        打开配置文件中的登录url
        :return:
        """
        self.open_url(self.__config_info['test_server_info']['url'])

    def send_key(self, locator: tuple, info: str):
        """
        向页面元素输入内容
        :param locator: 传入元素定位信息，例如：("css_selector","#username")
        :param info: 要输入的字符串
        :return:
        """
        element = self.find_elem(locator)
        try:
            element.send_keys(info)
            logging.info(f'向{locator}输入{info}成功')
        except Exception as e:
            logging.error(f'向{locator}输入{info}失败，{e}')

    def click(self, locator: tuple):
        """
        点击元素
        :param locator: 传入元素定位信息，例如：("css_selector","#username")
        :return:
        """
        element = self.find_elem(locator)
        try:
            element.click()
            logging.info(f'点击元素成功：{locator}')
        except Exception as e:
            logging.error(f'点击元素失败！{locator}，{e}')

    def save_screenshot(self, file_path: str):
        """
        保存截图
        :param file_path:
        :return:
        """
        try:
            self.__driver.save_screenshot(file_path)
            logging.info(f'截图已保存至：{file_path}')
        except Exception as e:
            logging.error(f'截图保存失败！{file_path}，{e}')

    def switch_frame(self, locator: tuple):
        """
        切换frame
        :param locator:
        :return:
        """
        element = self.find_elem(locator)
        try:
            self.__driver.switch_to.frame(element)
            logging.info(f'切换Frame成功{locator}')
        except Exception as e:
            logging.error(f'切换Frame失败！{locator}，{e}')

    def switch_handler(self, index: int):
        """
        切换窗口
        :param index: 窗口序号，从0开始
        :return:
        """
        all_handlers = self.__driver.window_handles
        try:
            self.__driver.switch_to.windows(all_handlers[index])
        except Exception as e:
            logging.error(f'切换至窗口{index}失败，{e}')
