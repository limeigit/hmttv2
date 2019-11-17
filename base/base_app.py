from base import Base
from selenium.webdriver.common.by import By


class BaseApp(Base):
    # 判断元素是否存在
    def base_app_element_exists(self, loc):
        try:
            self.base_find_element(loc)
            return True
        except Exception as e:
            return False

    # 滑动查找频道
    def base_swipe_search_channel(self, loc, channel_text):
        # 1.找到导航条的页面区域
        element = self.base_find_element(loc)
        # 2.获取区域元素的大小
        width = element.size.get("width")
        height = element.size.get("height")
        # 3.获取元素的位置
        x = element.location.get("x")
        y = element.location.get("y")
        # 4.组合滑动元素位置
        start_x = x + width * 0.8
        start_y = y + height * 0.5
        end_x = x + width * 0.2
        end_y = y + height * 0.5
        # 5.获取页面结构
        page_source = self.driver.page_source
        # 6.循环查找频道，未找到滑动
        while True:
            try:
                # 7.查找具体的频道
                loc1 = By.XPATH, "//*[contains(@text,'{}')]".format(channel_text)
                element1 = self.base_find_element(loc1, timeout=10)
                # 8.找到频道，则执行点击
                element1.click()
                break
            except Exception as e:
                # 9.找不到具体的元素则执行滑屏操作
                self.driver.swipe(start_x, start_y, end_x, end_y, duration=3000)
            if page_source == self.driver.page_source:
                print("滑到最后一屏了，还没有找到元素！")
                # 结束循环
                break
            else:
                # 10.更新页面资源
                page_source = self.driver.page_source

    # # 查找文章
    # def base_swipe_search_article(self, loc, title):
    #     # 1.限定查找文章的区域
    #     element = self.base_find_element(loc)
    #     # 2.获取当前屏幕的尺寸,宽和高
    #     size = self.driver.get_window_size()
    #     width = size.get("width")
    #     height = size.get("height")
    #     # 3.设置滑动的范围
    #     start_x = width * 0.5
    #     start_y = height * 0.8
    #     end_x = width * 0.5
    #     end_y = height * 0.2
    #     # 4.获取当前页面结构
    #     page_source = self.driver.page_source
    #     # 5.循环判断是否找到该文章
    #     while True:
    #         try:
    #             # 5.查找文章
    #             loc1 = By.XPATH, "//*[contains(@text,'{}')]".format(title)
    #             element = self.base_find_element(loc1, timeout=10)
    #             element.click()
    #             break
    #         except Exception as e:
    #             # 6.在当前页未找到元素，则滑动屏幕
    #             self.driver.swipe(start_x, start_y, end_x, end_y)
    #         # 7.判断页面是否滑动
    #         if page_source == self.driver.page_source:
    #             print("已经滑到最后一页了，滑不动了！")
    #             break
    #         # 8.更新页面结构
    #         else:
    #             page_source = self.driver.page_source

    # 查找文章,限定范围查找
    def base_swipe_search_article(self, loc, title):
        # 1.限定查找文章的区域
        element = self.base_find_element(loc)
        # 2.获取当前屏幕的尺寸,宽和高
        width = element.size.get("width")
        height = element.size.get("height")
        # 3.设置滑动的范围
        start_x = width * 0.5
        start_y = height * 0.8
        end_x = width * 0.5
        end_y = height * 0.2
        # 4.获取当前页面结构
        page_source = self.driver.page_source
        # 5.循环判断是否找到该文章
        while True:
            try:
                # 5.查找文章
                loc1 = By.XPATH, "//*[contains(@text,'{}')]".format(title)
                element = self.base_find_element(loc1, timeout=10)
                element.click()
                return True
                # break
            except Exception as e:
                # 6.在当前页未找到元素，则滑动屏幕
                self.driver.swipe(start_x, start_y, end_x, end_y)
            # 7.判断页面是否滑动
            if page_source == self.driver.page_source:
                print("已经滑到最后一页了，滑不动了！")
                return False
            # 8.更新页面结构
            else:
                page_source = self.driver.page_source