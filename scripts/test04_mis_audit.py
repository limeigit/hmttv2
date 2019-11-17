import sys
import os
sys.path.append(os.getcwd())
import page
from page.page_in import PageIn
from tool.driver import Driver
from tool.getlog import GetLog

# 获取日志器
log = GetLog.get_log()


class TestMisAudit:
    # 初始化
    def setup_class(self):
        # 1.获取driver
        self.driver = Driver.get_driver(page.page_mis_url)
        # 2.实例化PageIn页面对象
        self.page_in = PageIn(self.driver)
        # 3.调用后台登录的方法
        self.page_in.page_get_PageMisLogin.page_mis_login("testid", "testpwd123")

    # 资源销毁
    def teardown_class(self):
        Driver.quit_driver()

    # 调用审批页面的方法
    def test_page_mis_audit(self):
        # 1.调用审批的方法
        self.page_in.page_get_PageMisAudit.page_audit("test123", "数据库")
        try:
            # 2.判断是否审批通过
            result = self.page_in.page_get_PageMisAudit.page_mis_is_pass("test123", "数据库")
            print("审批通过的文章id为：",result)
            assert result == True
        except Exception as e:
            # 截图
            self.page_in.page_get_PageMisAudit.base_get_image()
            # 写入日志
            log.error(e)
            # 抛出异常
            raise
