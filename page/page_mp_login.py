import base
import page



class PageMpLogin(base.Base):
    # 1.输入手机号
    def page_input_phone(self, value):
        self.base_input(page.mp_phone, value)

    # 2.输入验证码
    def page_input_code(self, code):
        self.base_input(page.mp_verify_code, code)

    # 3.点击登陆
    def page_click_login_btn(self):
        self.base_click(page.mp_login)

    # 4.获取昵称
    def page_get_nickname(self):
        return self.base_get_text(page.mp_nickname)

    # 5.登陆业务的组合
    def page_mp_login(self, phone_number,code):
        # 1.输入用户名
        self.page_input_phone(phone_number)
        # 2.输入密码
        self.page_input_code(code)
        # 3.点击登录
        self.page_click_login_btn()