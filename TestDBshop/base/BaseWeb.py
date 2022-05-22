from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
from utils.GetConfig import *


class BaseWeb:
    B_name = By.NAME
    B_xpath = By.XPATH
    B_ID = By.ID
    B_CLASS = By.CLASS_NAME
    B_CSS = By.CSS_SELECTOR
    B_tag = By.TAG_NAME
    B_Link = By.LINK_TEXT
    B_Partial = By.PARTIAL_LINK_TEXT
    ForceWaiting = 0
    ImplicitWaiting = 1
    DispalyWait = 2

    def __init__(self):
        self.driver = webdriver.Chrome()
        # print(getconfig(option="sys",key="admin_url"))
        self.driver.get(getconfig(key="admin_url"))

    def __local_element(self, way, str_format):
        return self.driver.find_element(way, str_format)

    def get_local_elements(self, way, str_format):
        return self.driver.find_elements(way, str_format)

    def b_click(self, *args):
        """
        :param args[0]: 定位方式
        :param args[1]: 定位字符串
        """
        print("args:", args)
        self.__local_element(args[0], args[1]).click()

    def b_sendkey(self, *args):
        """
        :param args[0]: 定位方式
        :param args[1]: 定位字符串
        :param args[2]: 值
        """
        print("args:",args)
        self.__local_element(args[0], args[1]).send_keys(args[2])

    def flag_selected(self, *args):
        return self.__local_element(args[0], args[1]).is_selected()

    def flag_enabled(self, *args):
        return self.__local_element(args[0], args[1]).is_enabled()

    def flag_display(self,*args):
        return self.__local_element(args[0], args[1]).is_displayed()

    def b_clears(self,*args):
        print("args:", args)
        self.__local_element(args[0], args[1]).clear()

    def b_move_event(self, *args):
        element = self.__local_element(args[0], args[1])
        ActionChains(self.driver).move_to_element(element).perform()

    def wait_perform(self, second, wait_way):
        if wait_way == 0:
            time.sleep(second)
        elif wait_way == 1:
            self.driver.implicitly_wait(second)
        else:
            pass

    def close_browser(self):
        self.driver.close()


