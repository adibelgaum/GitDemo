from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        homePage = HomePage(self.driver)

        checkoutPage = homePage.shopItems()

        productNames = checkoutPage.get_productNames()

        for productName in productNames:
            cardText = productName.text
            if productName == "Blackberry":
                checkoutPage = CheckoutPage(self.driver)
                checkoutPage.get_add_button()

        checkoutPage.get_checkout_Button().click()

        confirmPage = checkoutPage.get_checkout_Button2()

        confirmPage.get_dropdown().send_keys("Ind")

        self.verifyLinkPresence("India")

        click_on_INDIA = confirmPage.get_click_on_india()

        i_agree = confirmPage.get_I_agree()

        purchase_Button = confirmPage.get_purchase_Button()

        alert_success = confirmPage.get_alert_success()

        assert "Success!" in alert_success
