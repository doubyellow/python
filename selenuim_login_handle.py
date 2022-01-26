# coding=utf-8
import time
from selenium import webdriver
from selenium.common.exceptions import *
from io import BytesIO
from PIL import Image
import ddddocr

# chrome driver 路径
CHROME_DRIVER_ABSPATH = r"C:\Users\ASUS\AppData\Local\Microsoft\WindowsApps\chromedriver.exe"
# edge driver 路径
EDGE_DRIVER_ABSPATH = r"C:\Users\ASUS\AppData\Local\Microsoft\WindowsApps\msedgedriver.exe"


class SignIn:
    def __init__(self, driver_path=None, url=None):
        """
        driver_path: driver.exe  文件路径
        ulr：网址
        xpath_iterable:输入框的xpath [user_xpath,password_xpath,...]
        info_iterable:多组用户数据 ，如 [[user1,password1,...],[user2,password2,...]]
        """
        if driver_path == CHROME_DRIVER_ABSPATH:
            self._driver = webdriver.Chrome(driver_path)
        elif driver_path == EDGE_DRIVER_ABSPATH:
            self._driver = webdriver.Edge(driver_path)
        else:
            self._driver = webdriver.Chrome()
        self._driver.maximize_window()
        self._url = url
        self.js = "window.open('{}');"

    def _switch_to_next_window(self):
        # 当前窗口句柄
        handle = self._driver.current_window_handle
        # 所有窗口句柄
        handles = self._driver.window_handles
        if len(handles) > self._driver.window_handles.index(handle) + 1:
            self._driver.switch_to.window(self._driver.window_handles[handles.index(handle) + 1])
        else:
            raise Exception("当前窗口是最后一个!")

    @property
    def driver(self):
        return self._driver

    # 输入网址
    def input_url(self, url=None):
        """
        url:网址
        """
        url = self._url if self._url and not url else url
        current_url = self._driver.current_url
        if current_url == "data:,":
            self._driver.get(url)
        else:
            self._driver.execute_script(self.js.format(url))
            self._switch_to_next_window()

    # 输入用户信息
    def input_info(self, keys_xpath: list, values: list):
        """
        keys_xpath:输入框的xpath 如：[user_xpath,password_xpath,...]
        values:用户信息 如：[user,password]
        """
        for xpath, value in zip(keys_xpath, values):
            if isinstance(value, float):
                value = int(value)
            try:
                self._driver.find_element_by_xpath(xpath).clear()
                self._driver.find_element_by_xpath(xpath).send_keys(value)
                time.sleep(0.1)
            except Exception as e:
                print(e)
                self._driver.close()

    # 输入验证码
    def input_yzm(self, input_yzm_xpath: str, yzm_xpath: str, len_value: int = 5):

        """
        input_yzm_xpath: 验证码输入框xpath
        yzm_xpath: 验证码xpath
        len_value: 验证码长度
        """
        code = None
        while not code:
            self._driver.find_element_by_xpath(yzm_xpath).click()
            time.sleep(1)
           
            # 截取全图,bytes 转 PIL
            image = BytesIO(self._driver.get_screenshot_as_png())
            login_img = Image.open(image)

            # 获取验证码位置
            element = self._driver.find_element_by_xpath(yzm_xpath)
            left = int(element.location['x'])
            top = int(element.location['y'])
            right = int(element.location['x'] + element.size['width'])
            bottom = int(element.location['y'] + element.size['height'])

            # PIL获取验证码图片
            img = login_img.crop((left, top, right, bottom))

            # PIL 转 bytes
            img_buffer = BytesIO()
            img.save(img_buffer, format='PNG')
            img_bytes = img_buffer.getvalue()

            # 识别验证码
            ocr = ddddocr.DdddOcr(old=False, show_ad=False)
            code = ocr.classification(img_bytes)
            # 输入验证码
            code = code if len(code) == len_value else print(code, "验证码错误")

        self._driver.find_element_by_xpath(input_yzm_xpath).clear()
        self._driver.find_element_by_xpath(input_yzm_xpath).send_keys(code)

    # 登录提交
    def submit(self, submit_xpath):
        """
        submit_xpath:登录按钮xpath
        """
        self._driver.find_element_by_xpath(submit_xpath).click()

    def aut_single_login(self, xpath, info, input_yzm_xpath, yzm_xpath, submit_xpath, url=None):
        """
        xpath: 输入框的xpath 如 [user_xpath,password_xpath,...]
        info: 单个用户数据 ，如 [user1,password1,...]
        input_yzm_xpath: 验证码输入框的xpath
        yzm_xpath: 验证码的xpath
        ulr：网址
        """
        # 输入url
        url = self._url if self._url and not url else url
        self.input_url(url)
        # 输入用户信息
        self.input_info(keys_xpath=xpath, values=info)
        try_times = 0
        while True:
            try_times += 1
            try:
                # 输入验证码
                self.input_yzm(input_yzm_xpath, yzm_xpath)
                # 点击登录
                self.submit(submit_xpath)
                time.sleep(1)
                print(f"第{try_times}次尝试登录{url}")
            except NoSuchElementException:
                print("登录成功")
                break


