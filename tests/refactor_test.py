import allure
import pytest
from .base_test import BaseTest


@allure.feature("TEST")
class TestScrollingFeature(BaseTest):
    
    @pytest.mark.skip()
    def test_test_test(self):
        self.home_page.open()
        self.home_page.is_opened()
        # self.cart_page.open()
        # self.cart_page.is_opened()
        # self.products_page.open()
        # self.products_page.is_opened()
        # self.signup_login_page.open()
        # self.signup_login_page.is_opened()
        # self.test_cases_page.open()
        # self.test_cases_page.is_opened()

# import pytest
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException

# @pytest.fixture(autouse=True)
# def check_and_close_ad_if_present(request, browser):
#     try:
#         WebDriverWait(browser, 5).until(
#             EC.frame_to_be_available_and_switch_to_it((By.XPATH, "XPATH_OF_YOUR_AD_IFRAME"))
#         )
#         browser.find_element(By.XPATH, "XPATH_OF_CLOSE_BUTTON").click()
#         browser.switch_to.default_content()
#     except TimeoutException:
#         pass



# AD_IFRAME = ('xpath', '//*[@id="ad_iframe"]')
# AD_CLOSE_BTTN = ('xpath', '//*[@id="dismiss-button"]')


# @pytest.fixture(autouse=True)
# def check_and_close_ad_if_present(self):
#     try:
#         self.wait.until(EC.frame_to_be_available_and_switch_to_it(self.AD_IFRAME))
#         self.wait.until(EC.element_to_be_clickable(self.AD_CLOSE_BTTN)).click()  
#         self.browser.switch_to.default_content()
#     except TimeoutException:
#         pass    