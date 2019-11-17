import sys
import os
sys.path.append(os.getcwd())
import time
from page.page_in import PageIn
from tool.driver import Driver
from tool.getlog import GetLog

log = GetLog.get_log()
class TestAppSearch:
    # 1.初始化
    def setup_class(self):
        # 获取driver对象
        self.driver = Driver.get_driver_app()
        # 实例化PageIn对象
        self.page_in = PageIn(self.driver)
        # 调用登录方法
        self.page_in.page_get_PageAppLogin.page_login_success()

    # 2.资源销毁
    def teardown_class(self):
        time.sleep(5)
        Driver.quit_driver_app()

    # 3.搜索频道和文章的测试方法
    def test_search_channel_and_title(self, channel="php", title="PHP"):

        try:
            # 1.调用业务方法,断言
            self.page_in.page_get_PageAppSearch.page_app_search(channel, title)
        except Exception as e:
            # 截图
            self.page_in.page_get_PageAppSearch.base_get_image()
            # 日志
            log.error(e)
            # 抛出异常
            raise
