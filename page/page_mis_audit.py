import time

import page
from base import Base


class PageMisAudit(Base):
    article_id = None

    # 1.点击信息管理
    def page_mis_click_info_manage(self):
        self.base_click(page.page_mis_info_manage)

    # 2.点击内容审核
    def page_mis_click_content_audit(self):
        self.base_click(page.page_mis_content_audit)

    # 3.输入文章名称
    def page_mis_audit_input_title(self, title):
        self.base_input(page.page_mis_title, title)

    # 4.输入选择的频道
    def page_mis_audit_search_channel(self, channel):
        self.base_input(page.page_mis_channel, channel)

    # 5.选择查询的状态
    def page_mis_audit_search_status(self):
        self.base_audit(page.page_mis_select, page.page_mis_status)

    # 6.点击查询
    def page_mis_click_search(self):
        self.base_click(page.page_mis_search)

    # 7.点击通过
    def page_mis_click_pass(self):
        self.base_click(page.page_mis_pass)

    # 8.确认通过
    def page_mis_confirm_pass(self):
        self.base_click(page.page_mis_confirm_pass)

    # 9.获取审批的id
    def page_mis_article_id(self):
        time.sleep(20)
        return self.base_get_text(page.page_mis_article_id)

    # 10.判断元素是否存在
    def page_mis_is_pass(self, title, channel):
        time.sleep(3)
        # 1.先刷新一下页面
        self.driver.refresh()
        # 2.输入title
        self.page_mis_audit_input_title(title)
        # 3.输入频道
        self.page_mis_audit_search_channel(channel)
        # 4.选择状态
        self.base_audit("请选择状态", "审核通过")
        # 5.点击查询
        self.page_mis_click_search()
        time.sleep(10)
        print("未审批的文章id为：", self.article_id)
        return self.base_elemnt_exits(self.article_id)

    # 11.组合审批业务
    def page_audit(self, title, channel):
        time.sleep(1)
        # 1.点击信息管理
        self.page_mis_click_info_manage()
        time.sleep(1)
        # 2.点击内容审核
        self.page_mis_click_content_audit()
        # 3.输入文章名称
        self.page_mis_audit_input_title(title)
        # 4.输入选择的频道
        self.page_mis_audit_search_channel(channel)
        time.sleep(2)
        # 5.选择查询的状态
        self.page_mis_audit_search_status()
        time.sleep(4)
        # 6.点击查询
        self.page_mis_click_search()
        time.sleep(2)
        # 获取查询文章的id, 将id保存到类变量中
        self.article_id = self.page_mis_article_id()
        # 7.点击通过
        self.page_mis_click_pass()
        time.sleep(1)
        # 8.确认通过
        self.page_mis_confirm_pass()
