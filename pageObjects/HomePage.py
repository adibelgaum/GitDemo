
from selenium.webdriver.common.by import By
from pageObjects.CheckoutPage import CheckoutPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    Shop_button = (By.CSS_SELECTOR, "a[href*='shop']")
    #####################################################
    name = (By.CSS_SELECTOR, "input[name*='name']")
    email = (By.CSS_SELECTOR, "input[name='email']")
    checkbox = (By.CSS_SELECTOR, "#exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@type='submit']")
    successMessage = (By.CSS_SELECTOR, "div[class*='alert-success']")
    ################################################

    def shopItems(self):
        self.driver.find_element(*HomePage.Shop_button).click()
        checkoutPage = CheckoutPage(self.driver)
        return checkoutPage

    def enter_name(self):
        return self.driver.find_element(*HomePage.name)

    def enter_email(self):
        return self.driver.find_element(*HomePage.email)

    def click_checkbox(self):
        return self.driver.find_element(*HomePage.checkbox).click()

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def click_submit(self):
        return self.driver.find_element(*HomePage.submit).click()

    def grab_successMessage(self):
        return self.driver.find_element(*HomePage.successMessage).text
