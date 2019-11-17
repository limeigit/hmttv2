import time
from base import Base
import page


class PageMpActicle(Base):
    # 1.点击内容管理
    def page_click_manage_content_btn(self):
        self.base_click(page.mp_manage_content)

    # 2.点击发布文章
    def page_click_public_title_btn(self):
        self.base_click(page.mp_public_article)

    # 3.输入文章标题
    def page_input_title(self, title):
        self.base_input(page.mp_title, title)

    # 4.输入文章内容
    def page_input_content(self, content):
        # 1.切换iframe
        self.base_switch_to_iframe(page.mp_content_frame)
        # 2.输入内容
        self.base_input(page.mp_content, content)
        # 3.回到默认页面
        # self.driver.switch_to.default_content()
        self.driver.switch_to.default_content()

    # 5.选择自动
    def page_select_cover(self):
        self.base_click(page.mp_cover)

    # 6.选择频道
    def page_select_channel(self):
        # 1.点击频道输入框
        self.base_click(page.mp_channel)
        time.sleep(2)
        # 2.选择数据库频道
        self.base_click(page.mp_channel_details)

    # 7.点击发表按钮
    def page_public_btn(self):
        self.base_click(page.mp_public_btn)

    # 8.判断元素是否存在,元素存在则通过
    def page_public_article_is_pass(self):
        if self.base_find_element(page.mp_success_article):
            return True
        else:
            return False

    # 9.组合发布文章业务
    def page_mp_article(self, title, content):
        # 1.点击内容管理
        self.page_click_manage_content_btn()
        time.sleep(2)
        # 2.点击发布文章
        self.page_click_public_title_btn()
        time.sleep(2)
        # 3.输入文章标题
        self.page_input_title(title)
        time.sleep(2)
        # 4.输入文章内容
        self.page_input_content(content)
        time.sleep(5)
        # 5.选择自动
        self.page_select_cover()
        # 6.选择频道
        self.page_select_channel()
        # 7.点击发表按钮
        self.page_public_btn()

