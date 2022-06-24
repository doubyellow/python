from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class WebDriver:
    def __init__(self, browser):  # 初始化浏览器
        if browser == 'firefox' or browser == 'Firefox' or browser == 'f' or browser == 'F':
            self.driver = webdriver.Firefox()
        elif browser == 'Ie' or browser == 'ie' or browser == 'i' or browser == 'I':
            self.driver = webdriver.Ie()
        elif browser == 'Chrome' or browser == 'chrome' or browser == 'Ch' or browser == 'ch':
            self.driver = webdriver.Chrome()
        elif browser == 'PhantomJS' or browser == 'phantomjs' or browser == 'ph' or browser == 'phjs':
            self.driver = webdriver.PhantomJS()
        elif browser == 'Edge' or browser == 'edge' or browser == 'Ed' or browser == 'ed':
            self.driver = webdriver.Edge()
        elif browser == 'Opera' or browser == 'opera' or browser == 'op' or browser == 'OP':
            self.driver = webdriver.Opera()
        elif browser == 'Safari' or browser == 'safari' or browser == 'sa' or browser == 'saf':
            self.driver = webdriver.Safari()
        else:
            raise NameError('只能输入firefox,Ie,Chrome,PhantomJS,Edge,Opera,Safari')

    def element(self, value, key='xpath'):  # 定位
        if key == 'resource_id.txt':
            element = self.driver.find_element_by_id(value)
        elif key == "name":
            element = self.driver.find_element_by_name(value)
        elif key == "class":
            element = self.driver.find_element_by_class_name(value)
        elif key == "link_text":
            element = self.driver.find_element_by_link_text(value)
        elif key == "xpath":
            element = self.driver.find_element_by_xpath(value)
        elif key == "tag":
            element = self.driver.find_element_by_tag_name(value)
        elif key == "css":
            element = self.driver.find_element_by_css_selector(value)
        else:
            raise NameError("Please enter the  elements,'resource_id.txt','name','class','link_text','xpath','css','tag'.")
        return element

    def elements(self, value, key="xpath"):  # 组定位
        if key == 'resource_id.txt':
            elements = self.driver.find_elements_by_id(value)
        elif key == "name":
            elements = self.driver.find_elements_by_name(value)
        elif key == "class":
            elements = self.driver.find_elements_by_class_name(value)
        elif key == "link_text":
            elements = self.driver.find_elements_by_link_text(value)
        elif key == "xpath":
            elements = self.driver.find_elements_by_xpath(value)
        elif key == "tag":
            elements = self.driver.find_elements_by_tag_name(value)
        elif key == "css":
            elements = self.driver.find_elements_by_css_selector(value)
        else:
            raise NameError("Please enter the  elements,'resource_id.txt','name','class','link_text','xpath','css','tag'.")
        return elements

    def element_wait(self, value, timeout=15, key="xpath"):  # 等待
        if key == "xpath":
            element = WebDriverWait(self.driver, timeout, 5).until(EC.presence_of_element_located((By.XPATH, value)))
        elif key == "resource_id.txt":
            element = WebDriverWait(self.driver, timeout, 0.5).until(EC.presence_of_element_located((By.ID, value)))
        elif key == "name":
            element = WebDriverWait(self.driver, timeout, 0.5).until(EC.presence_of_element_located((By.NAME, value)))
        elif key == "class":
            element = WebDriverWait(self.driver, timeout, 0.5).until(
                EC.presence_of_element_located((By.CLASS_NAME, value)))
        elif key == "link_text":
            element = WebDriverWait(self.driver, timeout, 0.5).until(
                EC.presence_of_element_located((By.LINK_TEXT, value)))
        elif key == "css":
            element = WebDriverWait(self.driver, timeout, 0.5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, value)))
        else:
            raise NameError("Please enter the  elements,'resource_id.txt','name','class','link_text','xpath','css'.")
        return element

    def open(self, url):  # 打开网页
        self.driver.get(url)

    def close(self):
        self.driver.close()

    def make_max_window(self):  # 最大化浏览器
        self.driver.maximize_window()

    def set_window_size(self, width, height):  # 设置窗口
        self.driver.set_window_size(width, height)

    def send_key(self, value, text, key="xpath"):  # 发送内容
        e1 = self.element(value, key=key)
        e1.clear()
        e1.send_keys(text)

    def control_keyboard(self, value, button='ENTER', key='xpath'):
        element = self.element(value, key=key)
        element.send_keys(Keys.CONTROL, button)

    def clear(self, value, key="xpath"):  # 清空
        self.element(value, key=key).clear()

    def click(self, value, key="xpath"):  # 单击
        self.element(value, key=key).click()

    def wait_click(self, value, key="xpath"):
        self.element_wait(value, key=key).click()

    def left_click(self, element):
        ActionChains(self.driver).click(element).perform()

    def right_click(self, element):  # 右击
        ActionChains(self.driver).context_click(element).perform()

    def move_to_element(self, element):  # 移动到
        ActionChains(self.driver).move_to_element(element).perform()

    def double_click(self, element):  # 双击
        ActionChains(self.driver).double_click(element).perform()

    def drag_and_drop(self, value1, value2, key1="xpath", key2="xpath"):  # 从e1到e2
        eme1 = self.element(value1, key=key1)
        eme2 = self.element(value2, key=key2)
        ActionChains(self.driver).drag_and_drop(eme1, eme2).perform()

    def click_text(self, text):  # 点击文字
        self.driver.find_element_by_link_text(text).click()

    def kill(self):  # 退出
        self.driver.quit()

    def submit(self, value, key='xpath'):  # 提交
        self.element(value, key=key).submit()

    def f5(self):  # 刷新
        self.driver.refresh()

    def js(self, script):  # 执行js
        self.driver.execute_script(script)

    def get_attribute(self, value, attribute, key='xpath'):
        return self.element(value, key=key).get_attribute(attribute)

    def get_text(self, value, key='xpath'):
        return self.element(value, key=key).text

    def get_is_dis(self, value, key='xpath'):
        return self.element(value, key).is_displayed()

    def get_title(self):  # 获取title
        return self.driver.title

    def get_screen(self, file_path):  # 截屏
        self.driver.get_screenshot_as_file(file_path)

    def wait(self, time):  # 等待
        self.driver.implicitly_wait(time)

    def accept_alert(self):  # 允许
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        self.driver.switch_to.alert.dismiss()

    def switch_to_frame(self, key, value):  # 切换
        if1 = self.element(key, value)
        self.driver.switch_to.frame(if1)
