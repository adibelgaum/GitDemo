
from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    Shop_button = (By.CSS_SELECTOR, "a[href*='shop']")
    productNames = (By.XPATH, "//div[@class='card h-100']/div/h4/a")
    add_button = (By.XPATH, "div/button")
    checkout_Button = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    checkout_Button2 = (By.XPATH, "//button[@class='btn btn-success']")



    def get_shopItems(self):
        return self.driver.find_element(*CheckoutPage.Shop_button)

    def get_productNames(self):
        return self.driver.find_elements(*CheckoutPage.productNames)

    def get_add_button(self):
        return self.driver.find_element(*CheckoutPage.add_button).click()

    def get_checkout_Button(self):
        return self.driver.find_element(*CheckoutPage.checkout_Button)

    def get_checkout_Button2(self):
        self.driver.find_element(*CheckoutPage.checkout_Button2).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage
