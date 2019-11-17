import sys
import os
sys.path.append(os.getcwd())
import time
import page
import pytest
from tool.driver import Driver
from tool.getlog import GetLog
from tool.read_data import ReadData
from page.page_mp_login import PageMpLogin


log = GetLog.get_log()


# 登录测试用例的编写
class TestMpLogin:
    # 初始化方法
    def setup_class(self):
        # 实例化浏览器驱动
        self.driver = Driver.get_driver(page.mp_url)
        # 实例化自媒体对象
        self.login_pm_page = PageMpLogin(self.driver)

    # 销毁资源方法
    def teardown_class(self):
        Driver.quit_driver()

    # 登陆的测试方法
    @pytest.mark.parametrize("info", ReadData().get_data("mp_login.yaml"))
    def test_login(self, info):
        # 调用自媒体的登陆业务方法
        self.login_pm_page.page_mp_login(info[0], info[1])
        try:
            # 获取登录后的昵称
            nickname = self.login_pm_page.page_get_nickname()
            assert nickname == "test123"
        except Exception as e:
            # 1.截图，将图片写入测试报告
            self.login_pm_page.base_get_image()
            # 2.将异常写入日志
            log.error(e)
            # 3.抛出异常
            raise
