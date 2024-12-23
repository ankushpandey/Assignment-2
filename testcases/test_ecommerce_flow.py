import time

import pytest

from pages.purchase_locators import PurchaseItemLocators
from pages.checkout_page import CheckOut
from pages.login_locators import LoginLocators
from pages.registration_Locators import RegistrationLocators
from packageutilities.BaseClass import BaseClass

class TestCompleteFlow(BaseClass):

    # @pytest.mark.skip
    def test_valid_reg(self):
        rg = RegistrationLocators(self.driver)
        rg.registration("ankush", "pandey", "ankush.pandey5@example.com", "Winter@123", "Winter@123")

    def test_log_in(self):
        lg = LoginLocators(self.driver)
        lg.log_in("ankush.pandey5@example.com", "Winter@123")
        time.sleep(5)
    def test_item_buy(self):
        bi = PurchaseItemLocators(self.driver)
        bi.buy_item("Build your own cheap computer")

    def test_checkout(self):
        co = CheckOut(self.driver)
        co.check_out("India", "indore","66sudamanagar", "opp pnb","452009","1234567890")



