import sys
import os

import time
sys.path.append(os.getcwd())
import page
from page.page_in import PageIn
from tool.driver import Driver
from tool.getlog import GetLog

log = GetLog.get_log()


class TestMpArticle:
    # 初始化方法
    def setup_class(self):
        # 1.获取驱动对象
        self.driver = Driver.get_driver(page.mp_url)
        # 2.获取pageIn对象
        self.page_in = PageIn(self.driver)
        # 3.调用登录方法
        self.page_in.page_get_PageMpLogin.page_mp_login("13012345678", "246810")
        time.sleep(5)

    # 资源销毁
    def teardown_class(self):
        # 关闭驱动对象
        time.sleep(1)
        Driver.quit_driver()

    # 发布文章
    def test_public_article(self, title="test123", content="你好，今天心情不错！py"):
        # 调用发布文章的组合业务
        self.page_in.page_get_PageMpArticle.page_mp_article(title, content)
        try:
            result = self.page_in.page_get_PageMpArticle.page_public_article_is_pass()
            print(result)
            # 断言
            assert result
        except Exception as e:
            # 截图并写入allure报告
            self.page_in.page_get_PageMpArticle.base_get_image()
            # 写入日志
            log.error(e)
            # 抛出异常
            raise
