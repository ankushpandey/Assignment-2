import pytest

from pages.purchase_item_locators import PurchaseItemLocators
from pages.checkout_item import CheckOut
from pages.login_locators import LoginLocators
from pages.registration_Locators import RegistrationLocators
from packageutilities.BaseClass import BaseClass

class TestCompleteFlow(BaseClass):

    # @pytest.mark.skip
    def test_valid_reg(self):
        rg = RegistrationLocators(self.driver)
        rg.registration("amit", "sharma", "amit21@example.com", "amit@123", "amit@123")

    def test_log_in(self):
        lg = LoginLocators(self.driver)
        lg.log_in("amit21@example.com", "amit@123")

    def test_item_buy(self):
        bi = PurchaseItemLocators(self.driver)
        bi.buy_item("Build your own cheap computer")

    def test_checkout(self):
        co = CheckOut(self.driver)
        co.check_out("India", "Bhopal","add0001", "addd002","34556","1234567890")



