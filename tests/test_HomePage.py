import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from TestData.HomePageData import homePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        homepage = HomePage(self.driver)
        homepage.enter_name().send_keys(getData["firstname"])
        homepage.enter_email().send_keys(getData["email_id"])
        homepage.click_checkbox()
        self.selectOptionByText(homepage.getGender(), getData["gender"])
        homepage.click_submit()
        alertText = homepage.grab_successMessage()

        assert ("Success" in alertText)
        self.driver.refresh()

    @pytest.fixture(params=homePageData.test_HomePage_data)
    def getData(self, request):
        return request.param
