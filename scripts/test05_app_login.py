import sys
import os

sys.path.append(os.getcwd())

import time
from page.page_in import PageIn
from tool.driver import Driver
from tool.getlog import GetLog

log = GetLog.get_log()


class TestAppLogin:
    # 初始化
    def setup_class(self):
        # 1.获取驱动
        self.driver = Driver.get_driver_app()
        # 2.获取PageIn对象
        self.page_in = PageIn(self.driver)

    # 结束
    def teardown_class(self):
        Driver.quit_driver()

    # 登录测试业务方法
    def test_app_login(self, phone='13012345678', code="246810"):
        # 调用登录的方法
        self.page_in.page_get_PageAppLogin.page_login(phone, code)
        time.sleep(3)
        try:
            assert self.page_in.page_get_PageAppLogin.page_is_login_success()
        except Exception as e:
            # 截图
            self.page_in.page_get_PageAppLogin.base_get_image()
            # 写入日志
            log.error(e)
            # 抛出异常
            raise
