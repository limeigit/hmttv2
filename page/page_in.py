from page.page_app_login import PageAppLogin
from page.page_app_search import PageAppSearch
from page.page_mis_audit import PageMisAudit
from page.page_mis_login import PageMisLogin
from page.page_mp_article import PageMpActicle
from page.page_mp_login import PageMpLogin


class PageIn:
    # 实例化浏览器对象
    def __init__(self, driver):
        self.driver = driver

    # 实例化自媒体的登录页面对象
    @property
    def page_get_PageMpLogin(self):
        return PageMpLogin(self.driver)

    # 实例化自媒体的发布文章页面对象
    @property
    def page_get_PageMpArticle(self):
        return PageMpActicle(self.driver)

    # 实例化后台登录的对象
    @property
    def page_get_PageMisLogin(self):
        return PageMisLogin(self.driver)

    # 实例化审批页面对象
    @property
    def page_get_PageMisAudit(self):
        return PageMisAudit(self.driver)

    # 实例化PageAppLogin对象
    @property
    def page_get_PageAppLogin(self):
        return PageAppLogin(self.driver)

    # 实例化PageAppSearch对象
    @property
    def page_get_PageAppSearch(self):
        return PageAppSearch(self.driver)
