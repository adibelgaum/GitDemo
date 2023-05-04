
from selenium.webdriver.common.by import By

class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    dropdown = (By.CSS_SELECTOR, "input[id='country']")
    click_on_india = (By.LINK_TEXT, "India")
    I_agree = (By.XPATH, "//label[@for='checkbox2']")
    purchase_Button = (By.CSS_SELECTOR, "input[type='submit']")
    alert_success = (By.XPATH, "//div[contains(@class,'alert-dismissible')]")


    def get_dropdown(self):
        return self.driver.find_element(*ConfirmPage.dropdown)

    def get_click_on_india(self):
        return self.driver.find_element(*ConfirmPage.click_on_india).click()

    def get_I_agree(self):
        return self.driver.find_element(*ConfirmPage.I_agree).click()

    def get_purchase_Button(self):
        return self.driver.find_element(*ConfirmPage.purchase_Button).click()

    def get_alert_success(self):
        return self.driver.find_element(*ConfirmPage.alert_success).text
