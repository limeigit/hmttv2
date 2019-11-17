from selenium.webdriver.common.by import By

"""以下是自媒体的配置数据"""

# 自媒体的登录url
mp_url = "http://ttmp.research.itcast.cn/#/login"

# 1.手机号元素对象定位方式和值
mp_phone = By.CSS_SELECTOR, ".el-input__inner"

# 2.验证码元素对象定位方式和值
mp_verify_code = By.CSS_SELECTOR, "[placeholder='验证码']"

# 3.登陆按钮元素对象和定位方式
mp_login = By.CSS_SELECTOR, ".el-button--primary"

# 4.获取昵称
mp_nickname = By.CSS_SELECTOR, ".user-name"

"""一下是发布文章的配置数据"""
# 1.内容管理的元素对象定位方式和值
mp_manage_content = By.CSS_SELECTOR, ".el-submenu__title span"

# 2.发布文章超链接元素定位方式和值
mp_public_article = By.CSS_SELECTOR, ".el-menu--inline .el-menu-item"

# 3.文章标题元素定位方式和值
mp_title = By.CSS_SELECTOR, ".filter-item  input"

# 4.内容的定位方式和值
mp_content = By.CSS_SELECTOR, "#tinymce"

# 5.封面选择自动元素的定位方式和值
mp_cover = By.XPATH, "//*[text()='自动']"

# 6.点击频道输入框元素定位方式和值
mp_channel = By.CSS_SELECTOR, ".el-select .el-input__inner"

# 7.选择具体的频道元素对象和值
mp_channel_details =  By.XPATH, "//*[text()='数据库']"

# 8.发布按钮的元素对象和值
mp_public_btn = By.CSS_SELECTOR, ".el-form-item__content .el-button--primary"

# 9.获取发布文章成功后的弹窗信息
# mp_success_article = By.CSS_SELECTOR, ""
mp_success_article = By.XPATH, "//*[contains(text(),'新增文章成功')]"

# 10.切换iframe,在输入内容时，必须切换iframe
mp_content_frame = By.CSS_SELECTOR, "#publishTinymce_ifr"

"""一下是自媒体后台管理系统登录的配置数据"""
# 后台登录的url
page_mis_url = "http://ttmis.research.itcast.cn/#/"
# 后台账号
page_mis_username = By.CSS_SELECTOR, "[name='username']"
# 后台密码
page_mis_pwd = By.CSS_SELECTOR, "[name='password']"
# 登录按钮
page_mis_login_btn = By.CSS_SELECTOR, "#inp1"
# 获取后台登录后的昵称
page_mis_nickname = By.CSS_SELECTOR, ".user_info span"

"""一下是审批文章的配置"""
# 1.信息管理
page_mis_info_manage = By.CSS_SELECTOR, ".level1 .fa-shopping-basket"
# 2.内容审核
page_mis_content_audit = By.XPATH, "//*[contains(text(),'内容审核')]"
# 3.标题
page_mis_title = By.CSS_SELECTOR, "[placeholder='请输入: 文章名称']"
# 4.频道
page_mis_channel = By.CSS_SELECTOR, "[placeholder='请输入: 频道']"
# 5.选择的状态
page_mis_select = "请选择状态"
# 5.1选择具体的状态
page_mis_status = "待审核"
# 6.查询
page_mis_search = By.CSS_SELECTOR, ".find"
# 7.通过
page_mis_pass = By.XPATH, "//div[@class='cell'] //span [text()='通过']/.."
# 确认通过
page_mis_confirm_pass = By.CSS_SELECTOR, ".el-button--primary"
# 获取文章的id
page_mis_article_id = By.CSS_SELECTOR, ".cell>span"

"""一下是app登录的配置数据"""
# 1.输入手机号
page_app_phone = By.XPATH, "//*[@index='1'and @class='android.widget.EditText']"
# 2.输入验证码
page_app_code = By.XPATH, "//*[@index='2'and @class='android.widget.EditText']"
# 3.登录按钮
page_app_login_btn = By.XPATH, "//*[@index='4'and @class='android.widget.Button']"

# 4.我的
page_app_me_btn = By.XPATH, "//*[@index='3'and @class='android.widget.ImageView']"
# 5.登录后的昵称
page_app_login_nickname = By.XPATH, "//*[@index='0'and @class='android.view.View']"

"""一下是app登录成功后滑动的数据"""
# 1.查找频道
page_app_search_channel = By.XPATH, "//*[@index='1'and @class='android.widget.HorizontalScrollView']"
# 2.查找文章
page_app_search_article = By.XPATH, "//*[@bounds='[0,260][720,1144]']"
