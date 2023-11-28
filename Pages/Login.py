
import os
from Locators import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# import pytesseract
# from PIL import Image


def wait_until_element_has_an_attribute(self, element_selector, element_locator):
    wait = WebDriverWait(self.driver, 20)
    element = wait.until(EC.element_to_be_clickable((element_selector, element_locator)))
    sleep(0.5)
    element.click()
    sleep(0.5)


def wait_until_element_has_an_attribute_and_send_keys(self, element_selector, element_locator, text):
    wait = WebDriverWait(self.driver, 20)
    element = wait.until(EC.element_to_be_clickable((element_selector, element_locator)))
    sleep(0.5)
    element.clear()
    sleep(0.5)
    element.send_keys(text)
    sleep(0.5)


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_login_username(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', login_username, text)
        # self.driver.find_element('xpath', login_username).send_keys(mobile)

    def enter_login_username_with_password(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', login_username_with_password, text)
        # self.driver.find_element('xpath', login_username_with_password).send_keys(code)

    def enter_login_username_with_password_click(self):
        wait_until_element_has_an_attribute(self, 'xpath', login_username_with_password_click)

    def enter_login_btn_submit_next(self):
        wait_until_element_has_an_attribute(self, 'xpath', login_btn_submit_next)
        # self.driver.find_element('xpath', login_btn_submit_next).click()

    # def enter_login_password(self, code, a=1):
    #     for i in range(a):
    #         try:
    #             self.driver.find_element('xpath', login_username_with_code).click()
    #             self.driver.find_element('xpath', login_password).send_keys(code)
    #             return
    #         except:
    #             self.driver.find_element('xpath', login_password).send_keys(code)
    #     # self.driver.find_element('xpath', login_password).send_keys(code)

    def enter_login_password(self, code, a=1):
        for i in range(a):
            try:
                self.driver.find_element('xpath', login_password).send_keys(code)
                return
            except:
                self.driver.find_element('xpath', login_username_with_code).click()
                self.driver.find_element('xpath', login_password).send_keys(code)
                # self.driver.find_element('xpath', login_password).send_keys(code)

    def enter_login_btn_submit(self):
        wait_until_element_has_an_attribute(self, 'xpath', login_btn_submit)
        # self.driver.find_element('xpath', login_btn_submit).click()

    # def enter_login_btn_submit_next_captcha(self):
    #     sleep(1)
    #     captcha_element = self.driver.find_element('xpath', "//*[@id='loginform']/div[1]/div/div/div[1]/img")
    #     sleep(1)
    #     captcha_image_url = captcha_element.get_attribute("src")
    #
    #     self.driver.save_screenshot('screenshot.png')
    #     captcha_image = Image.open('screenshot.png')
    #     left, top, right, bottom = captcha_element.location['x'], captcha_element.location['y'], \
    #     captcha_element.location['x'] + captcha_element.size['width'], captcha_element.location['y'] + \
    #     captcha_element.size['height']
    #     captcha_image = captcha_image.crop((left, top, right, bottom))
    #     # تشخیص متن کپچا با استفاده از pytesseract
    #     captcha_text = pytesseract.image_to_string(captcha_image)
    #     # وارد کردن متن کپچا در فیلد مناسب
    #     captcha_input = self.driver.find_element_by_xpath("//*[@id='loginform']/div[1]/div/div/div[2]/input")
    #     captcha_input.send_keys(captcha_text)
    #     self.driver.find_element('xpath', "//*[@id='loginform']/div[2]/button").click()



    def enter_login_btn_submit_next_captcha(self):

        captcha_img = self.driver.find_element('xpath', "//*[@id='loginform']/div[1]/div/div/div[1]/img")

        captcha_img.screenshot('captchas/captcha.png')

        api_key = os.getenv('APIKEY_2CAPTCHA', "80c4b1e61829151ed18748dfefba01ad")

        solver = TwoCaptcha(api_key)

        try:
            result = solver.normal('captchas/captcha.png')

        except Exception as e:
            print(e)

        else:
            code = result['code']
            print(code)

            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(('xpath', "//*[@id='loginform']/div[1]/div/div/div[2]/input")))
            self.driver.find_element('xpath', "//*[@id='loginform']/div[1]/div/div/div[2]/input").send_keys(code)

            self.driver.find_element('xpath', "//*[@id='loginform']/div[2]/button").click()

            # self.driver.find_element('xpath', '//*[@id="root"]/div/main/div/section/form/button[1]').click()

        sleep(10)






