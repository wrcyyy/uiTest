# -*- coding: utf-8 -*-

"""
------------------------------------
@Project : uiTest
@Time    : 2021/3/9 14:58
@Auth    : wrc
@Email   : wrcyyy@126.com
@File    : pages.py
@IDE     : PyCharm
------------------------------------
"""
from itertools import takewhile
import logging
import os

from utils.fileoperate import FileOperate
from selenium.webdriver.common.by import By

current_dir = os.path.abspath(os.path.dirname(__file__))


class BasePageElements:
    def __init__(self, dir_name, file_name, root_dir=current_dir):
        self.names, self.desc, self.data, self.info = [], [], [], []
        self.__run(dir_name, root_dir, file_name)

    def __run(self, dir_name, root_dir, filename):
        file_path = os.path.join(root_dir, dir_name, filename)
        try:
            self.info = FileOperate.read_yaml(file_path)['parameters']
            self.names = [x['name'] for x in self.info]
            self.desc = [x['desc'] for x in self.info]
            self.data = [x['data'] for x in self.info]
        except Exception as e:
            logging.error(f'文件解析失败：{e}')

    def locator(self, element_name: str) -> tuple:
        """
        元素转换
        :param element_name:
        :return:
        """
        locator_dic = {
            "ID": By.ID,
            "XPATH": By.XPATH,
            "LINK_TEXT": By.LINK_TEXT,
            "PARTIAL_LINK_TEXT": By.PARTIAL_LINK_TEXT,
            "NAME": By.NAME,
            "TAG_NAME": By.TAG_NAME,
            "CLASS_NAME": By.CLASS_NAME,
            "CSS_SELECTOR": By.CSS_SELECTOR
        }
        element_info = list(filter(lambda x: x['name'] == element_name, self.info))
        if element_info and element_info[0]['data']['method'].upper() in locator_dic:
            return (locator_dic[element_info[0]['data']['method'].upper()], element_info[0]['data']['value'])
        logging.error(f'元素定位异常{element_name}')
        return ()


class LoginPageElements(BasePageElements):
    def __init__(self):
        super(LoginPageElements, self).__init__('LoginPage', 'Login.yml')


if __name__ == '__main__':
    login_page_elements = LoginPageElements()
    for x in login_page_elements.names:
        print(login_page_elements.locator(x))
