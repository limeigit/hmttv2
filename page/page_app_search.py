import time

import page
from base.base_app import BaseApp


class PageAppSearch(BaseApp):
    # 1.查找频道
    def page_app_search_channel(self, channel_text):
        self.base_swipe_search_channel(page.page_app_search_channel, channel_text)

    # 2.查找文章
    def page_app_search_article(self, title):
        self.base_swipe_search_article(page.page_app_search_article, title)

    # 3.组合查找文章业务方法
    def page_app_search(self, channel_text, title):
        # 1.查找具体的频道
        self.page_app_search_channel(channel_text)
        time.sleep(5)
        # 2.查找具体的文章
        self.page_app_search_article(title)
