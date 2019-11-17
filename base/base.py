import allure
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    # 1.初始化方法
    def __init__(self, driver):
        self.driver = driver

    # 2.查找元素
    def base_find_element(self, loc, timeout=30, poll=0.5):
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 3.输入
    def base_input(self, loc, value):
        # 1.找到元素对象
        element = self.base_find_element(loc)
        # 2.清空
        element.clear()
        # 3.输入
        element.send_keys(value)

    # 4.点击
    def base_click(self, loc):
        # 1.找到元素
        element = self.base_find_element(loc)
        # 2.点击操作
        element.click()

    # 5.获取文本
    def base_get_text(self, loc):
        return self.base_find_element(loc).text

    # 6.截图,并写入allure报告
    def base_get_image(self):
        self.driver.get_screenshot_as_file("./image/err.png")
        # 调用将图片写入测试报告的方法
        self.base_write_image_report()

    # 7.将图片写入测试报告
    def base_write_image_report(self):
        with open("./image/err.png", "rb") as f:
            allure.attach("错误截图", f.read(), allure.attach_type.PNG)

    # 8.切换iframe
    def base_switch_to_iframe(self, loc):
        element = self.base_find_element(loc)
        self.driver.switch_to.frame(element)

    # 9.判断元素是否存在
    def base_elemnt_exits(self, element_text):
        loc = By.XPATH, "//*[contains(text(),'{}')]".format(element_text)
        element = self.base_find_element(loc, timeout=5)
        if element:
            print("元素已经找到！")
            return True
        else:
            print("元素未找到！")
            return False

    # 10.审核元素的封装
    def base_audit(self, placeholder_text, element_text):
        # 1.点击下拉框
        loc1 = By.XPATH, "//*[contains(@placeholder,'{}')]".format(placeholder_text)
        self.base_click(loc1)
        time.sleep(2)
        # 2.选择具体的值----疑惑
        loc2 = By.CSS_SELECTOR, ".el-select-dropdown__list li"
        element_audit = self.base_find_elements(loc2)
        for element in element_audit:
            if element.text == element_text:
                element.click()
                break

    # 11.查找元素
    def base_find_elements(self, loc, timeout=30, poll=0.5):
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(
            lambda x: x.find_elements(*loc))
