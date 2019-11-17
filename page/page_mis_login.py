import page
from base.base import Base


class PageMisLogin(Base):
    # 1.输入用户名
    def page_mis_input_username(self, username):
        # 执行输入
        self.base_input(page.page_mis_username, username)

    # 2.输入密码
    def page_mis_input_pwd(self, pwd):
        self.base_input(page.page_mis_pwd, pwd)

    # 3.点击登录按钮
    def page_mis_click_login_btn(self):
        # 1.利用js修改disabled属性的值
        js = "document.getElementById('inp1').disabled = false"
        self.driver.execute_script(js)
        # 2.点击登录按钮
        self.base_click(page.page_mis_login_btn)

    # 4.获取昵称
    def page_mis_get_nickname(self):
        return self.base_get_text(page.page_mis_nickname)

    # 5.组合登录业务
    def page_mis_login(self, username, pwd):
        self.page_mis_input_username(username)
        self.page_mis_input_pwd(pwd)
        self.page_mis_click_login_btn()
