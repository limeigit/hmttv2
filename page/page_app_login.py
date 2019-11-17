import time

import page
from base.base_app import BaseApp


class PageAppLogin(BaseApp):
    # 输入手机号
    def page_input_phone(self, phone):
        self.base_input(page.page_app_phone, phone)

    # 输入验证码
    def page_input_verify_code(self, code):
        self.base_input(page.page_app_code, code)

    # 点击登录按钮
    def page_click_login_btn(self):
        self.base_click(page.page_app_login_btn)

    # 组合登录业务
    def page_login(self, phone, code):
        self.page_input_phone(phone)
        self.page_input_verify_code(code)
        time.sleep(2)
        self.page_click_login_btn()

    # 判断是否登录成功
    def page_is_login_success(self):
        # 1.点击我的
        # self.base_click(page.page_app_me_btn)
        # 2.获取登录后的昵称
        # return self.base_get_text(page.page_app_login_nickname)
        return self.base_app_element_exists(page.page_app_me_btn)

    # 组合登录成功业务---依赖成功
    def page_login_success(self, phone="13012345678", code="246810"):
        self.page_input_phone(phone)
        self.page_input_verify_code(code)
        time.sleep(2)
        self.page_click_login_btn()

