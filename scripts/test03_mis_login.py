import sys
import os
sys.path.append(os.getcwd())
import time
import page
from page.page_in import PageIn
from tool.driver import Driver
from  tool.getlog import GetLog

log = GetLog.get_log()


class TestMisLogin:
    # 初始化
    def setup_class(self):
        # 获取浏览器驱动
        self.driver = Driver.get_driver(page.page_mis_url)
        # 实例化统一入口
        self.page_in = PageIn(self.driver)

    # 资源销毁
    def teardown_class(self):
        Driver.quit_driver()

    # 登录测试方法
    def test_page_mis_login(self, username="testid", pwd="testpwd123", tp="管理员"):
        # 调用后台页面的登录方法
        self.page_in.page_get_PageMisLogin.page_mis_login(username, pwd)
        time.sleep(5)
        try:
            # 获取昵称
            nickname = self.page_in.page_get_PageMisLogin.page_mis_get_nickname()
            print(nickname)
            # 断言
            assert tp in nickname
        except Exception as e:
            # 截图
            self.page_in.page_get_PageMisLogin.base_get_image()
            # 日志
            log.error(e)
            # 抛出异常
            raise
