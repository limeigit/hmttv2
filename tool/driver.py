from selenium import webdriver
import appium.webdriver

# 创建一个获取浏览器和关闭浏览器的类
class Driver:
    # web浏览器
    driver = None
    # app浏览器
    driver_app = None
    # 获取浏览器驱动
    @classmethod
    def get_driver(cls,url):
        if cls.driver is None:
            # 获取驱动对象
            cls.driver = webdriver.Chrome()
            # 最大化浏览器
            cls.driver.maximize_window()
            # 打开浏览器
            cls.driver.get(url)
        return cls.driver


    # 关闭驱动对象
    @classmethod
    def quit_driver(cls):
        if cls.driver:
            # 关闭浏览器
            cls.driver.quit()
            # 将驱动对象置空
            cls.driver = None

    # 打开app
    @classmethod
    def get_driver_app(cls):
        desired_caps = dict()
        if cls.driver_app is None:
            desired_caps["platformName"] = "Android"
            desired_caps["platformVersion"] = "5"
            desired_caps["deviceName"] = "emulator-5554"
            desired_caps["appPackage"] = "com.itcast.toutiaoApp"
            desired_caps["appActivity"] = "com.itcast.toutiaoApp.MainActivity"
            desired_caps["unicodeKeyboard"] = True
            desired_caps["resetKeyboard"] = True
            desired_caps["noReset"] = False
            cls.driver_app = appium.webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        return cls.driver_app

    # 关闭app驱动
    @classmethod
    def quit_driver_app(cls):
        if cls.driver_app:
            cls.driver_app.quit()
            cls.driver_app = None

