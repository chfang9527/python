import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure


@allure.feature("账号登录")
class TestLogin:

    @allure.story("登录成功")
    def test_login(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
        self.driver.get("http://121.5.102.46:7920/")
        self.driver.find_element(By.XPATH,
                                 "//*[@id='app']/div/section/div[2]/div/div/div/div[2]/div/label[2]/span").click()
        self.driver.find_element(By.XPATH, "//input[@type='text']").send_keys("13018967619")
        self.driver.find_element(By.XPATH, "//input[@type='password']").send_keys("111111")
        code = self.driver.find_element(By.XPATH, "(//input[@type='text'])[2]")  # 验证码输入框位置
        img = self.driver.find_element(By.CSS_SELECTOR, ".el-col img")  # 验证码图片位置
        img.screenshot("code.png")  # 将验证码截图，保存为code.png
        time.sleep(1)
        # 以下为识别验证码的代码
        import ddddocr
        ocr = ddddocr.DdddOcr()
        with open("code.png", "rb") as fp:
            image = fp.read()
        catch = ocr.classification(image)  # 验证码返回给catch
        code.send_keys(catch)  # 将识别到的验证码输入到框内
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//button/span").click()  # 登录
        time.sleep(2)
        message = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/section/header/div/div[3]/div["
                                                     "4]/div/div/div")
        print(message.text)
        assert "您好" in message.text

    @allure.story("密码错误登录失败")
    def test_pwd(self):
        self.driver = webdriver.Edge()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
        self.driver.get("http://121.5.102.46:7920/")
        self.driver.find_element(By.XPATH,
                                 "//*[@id='app']/div/section/div[2]/div/div/div/div[2]/div/label[2]/span").click()
        self.driver.find_element(By.XPATH, "//input[@type='text']").send_keys("13018967619")
        self.driver.find_element(By.XPATH, "//input[@type='password']").send_keys("1111111")
        code = self.driver.find_element(By.XPATH, "(//input[@type='text'])[2]")  # 验证码输入框位置
        img = self.driver.find_element(By.CSS_SELECTOR, ".el-col img")  # 验证码图片位置
        img.screenshot("code.png")  # 将验证码截图，保存为code.png
        time.sleep(1)
        # 以下为识别验证码的代码
        import ddddocr
        ocr = ddddocr.DdddOcr()
        with open("code.png", "rb") as fp:
            image = fp.read()
        catch = ocr.classification(image)  # 验证码返回给catch
        code.send_keys(catch)  # 将识别到的验证码输入到框内
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//button/span").click()  # 登录
        time.sleep(2)
        message = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[1]")
        print(message.text)
        assert "账号或密码错误" in message.text

    @allure.story("账号错误登录失败")
    def test_user(self):
        self.driver = webdriver.Edge()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
        self.driver.get("http://121.5.102.46:7920/")
        self.driver.find_element(By.XPATH,
                                 "//*[@id='app']/div/section/div[2]/div/div/div/div[2]/div/label[2]/span").click()
        self.driver.find_element(By.XPATH, "//input[@type='text']").send_keys("13018967633")
        self.driver.find_element(By.XPATH, "//input[@type='password']").send_keys("111111")
        code = self.driver.find_element(By.XPATH, "(//input[@type='text'])[2]")  # 验证码输入框位置
        img = self.driver.find_element(By.CSS_SELECTOR, ".el-col img")  # 验证码图片位置
        img.screenshot("code.png")  # 将验证码截图，保存为code.png
        time.sleep(1)
        # 以下为识别验证码的代码
        import ddddocr
        ocr = ddddocr.DdddOcr()
        with open("code.png", "rb") as fp:
            image = fp.read()
        catch = ocr.classification(image)  # 验证码返回给catch
        code.send_keys(catch)  # 将识别到的验证码输入到框内
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//button/span").click()  # 登录
        time.sleep(2)
        message = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[1]")
        print(message.text)
        assert "账号或密码错误" in message.text

    def teardown(self):
        self.driver.close()

