import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class HeaderFooterElements():
    
    HOME_PAGE_LOGO_BTTN = ('css selector', '.logo img')
    HEADER_HOME_BTTN = ('xpath', '//a[contains(text(), "Home")]')
    HEADER_PRODUCTS_BTTN = ('xpath', '//a[contains(text(), "Products")]')
    HEADER_CART_BTTN = ('xpath', '//a[contains(text(), "Cart")]')
    HEADER_SIGNUP_LOGIN_BTTN = ('xpath', '//a[contains(text(), " Signup / Login")]') 
    HEADER_CONTACT_US_BTTN = ('xpath', '//a[contains(text(), "Contact us")]')
    HEADER_LOGOUT_BTTN = ('xpath', '//a[contains(text(), " Logout")]')
    HEADER_DELETE_ACC_BTTN = ('xpath', '//a[contains(text(), " Delete Account")]')
    HEADER_TEST_CASE_BTTN = ('xpath', '//a[contains(text(), " Test Cases")]')
    SUBSCRIPTION_EMAIL_FIELD = ('css selector', '#susbscribe_email')
    SUBSCRIPTION_BTTN = ('css selector', '#subscribe')
    SUBSCRIPTION_TEXT = ('css selector', '.single-widget h2')
    SUCCESS_SUBSCRIBE_MSSG = ('css selector', '#success-subscribe')
    HEADER = ("css selector", ".nav.navbar-nav")
    USERNAME_FIELD = ("xpath", "//input[@name='username']")
    USER_STATUS = ('xpath', '//a[contains(text(), "Logged in as")]')

    AD_IFRAME = ('xpath', '//*[@id="ad_iframe"]')
    AD_FULL_IFRAME = ('xpath', '//div[@id="ad_position_box"]')
    AD_CLOSE_BTTN = ('css selector', 'div#dismiss-button')
    ACTIVE_AD = ('css selector', 'ins.adsbygoogle[data-ad-status="filled"][data-vignette-loaded="true"]')
    ACTIVE_AD_IFRAME = ('css selector', 'ins.adsbygoogle[data-ad-status="filled"][data-vignette-loaded="true"] iframe')
    NESTED_ACTIVE_AD_IFRAME = ('css selector', 'iframe#ad_iframe[title="Advertisement"]')


    @allure.step("Click Signup/Login header button")
    def click_signup_login_button(self):
        self.wait.until(EC.element_to_be_clickable(self.HEADER_SIGNUP_LOGIN_BTTN)).click()
        self.check_and_close_ad_if_present()

    @allure.step("Click Home header button")
    def click_home_button(self):
        self.wait.until(EC.element_to_be_clickable(self.HEADER_HOME_BTTN)).click()
        self.check_and_close_ad_if_present()

    @allure.step("Click delete account header button")
    def click_delete_account_button(self):
        self.wait.until(EC.element_to_be_clickable(self.HEADER_DELETE_ACC_BTTN)).click()
        self.check_and_close_ad_if_present()

    @allure.step("Click logout header button")
    def click_logout_button(self):
        self.wait.until(EC.element_to_be_clickable(self.HEADER_LOGOUT_BTTN)).click()
        self.check_and_close_ad_if_present()

    @allure.step("Click 'Test Cases' header button")
    def click_testcases_button(self):
        self.wait.until(EC.element_to_be_clickable(self.HEADER_TEST_CASE_BTTN)).click()
        self.check_and_close_ad_if_present()

    @allure.step("Click 'Contact Us' header button")
    def click_contact_us_button(self):
        self.wait.until(EC.element_to_be_clickable(self.HEADER_CONTACT_US_BTTN)).click()
        self.check_and_close_ad_if_present()

    @allure.step("Click subscribe footer button")
    def click_subscribe_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBSCRIPTION_BTTN)).click()
        self.check_and_close_ad_if_present()

    @allure.step("Click cart header button")
    def click_cart_button(self):
        self.wait.until(EC.element_to_be_clickable(self.HEADER_CART_BTTN)).click()
        self.check_and_close_ad_if_present()

    @allure.step("Click products header button")
    def click_products_button(self):
        self.wait.until(EC.element_to_be_clickable(self.HEADER_PRODUCTS_BTTN)).click()
        self.check_and_close_ad_if_present()

    @allure.step("Click delete account header button")
    def click_delete_account_button(self):
        self.wait.until(EC.visibility_of_element_located(self.HEADER_DELETE_ACC_BTTN))  
        self.wait.until(EC.element_to_be_clickable(self.HEADER_DELETE_ACC_BTTN)).click()
        self.check_and_close_ad_if_present()

    @allure.step("'SUBSCRIPTION' footer block visible")
    def is_subscription_label_visible(self):
        self.wait.until(EC.visibility_of_element_located(self.SUBSCRIPTION_TEXT))
        self.wait.until(EC.visibility_of_element_located(self.SUBSCRIPTION_BTTN))
        self.wait.until(EC.visibility_of_element_located(self.SUBSCRIPTION_EMAIL_FIELD))
       
    @allure.step("Site header visible")
    def is_header_visible(self):
        self.wait.until(EC.visibility_of_element_located(self.HEADER))      

    @allure.step("User name header visible")
    def is_user_name_header_visible(self):
        self.wait.until(EC.visibility_of_element_located(self.HEADER_LOGOUT_BTTN))      
        self.wait.until(EC.visibility_of_element_located(self.HEADER_DELETE_ACC_BTTN))      
        # self.wait.until(EC.visibility_of_element_located(self.USERNAME_FIELD))      
        # self.wait.until(EC.visibility_of_element_located(self.USER_STATUS))      

    @allure.step("Fill email in subscription field")
    def fill_subscription_email(self):
        self.fill_field(self.SUBSCRIPTION_EMAIL_FIELD, self.fake.email())          

    @allure.step("Succes subscription footer message visible")
    def is_succes_subscription_mssg_visible(self):
        self.wait.until(EC.visibility_of_element_located(self.SUCCESS_SUBSCRIBE_MSSG))   
        self.make_screenshot("Success message")

    def check_and_close_ad_if_present(self):
        try:
            ad_iframe = self.browser.find_element(*self.ACTIVE_AD_IFRAME)
            if ad_iframe.is_displayed():
                with allure.step("Close Advertisement"):
                    self.browser.switch_to.frame(ad_iframe)
    
                    # Check if ad close button is present in the current iframe
                    try:
                        ad_close_button = self.browser.find_element(*self.AD_CLOSE_BTTN)
                        ad_close_button.click()
                    except NoSuchElementException:
                        # If ad close button not found in the current iframe, switch to nested iframe
                        nested_ad_iframe = self.browser.find_element(*self.NESTED_ACTIVE_AD_IFRAME)
                        self.browser.switch_to.frame(nested_ad_iframe)
                        ad_close_button_nested = self.browser.find_element(*self.AD_CLOSE_BTTN)
                        ad_close_button_nested.click()
                        self.browser.switch_to.parent_frame()  # Switch back to the parent iframe
    
                    self.browser.switch_to.default_content()
                    allure.attach("Advertisement Closed", name="Advertisement Status", attachment_type=allure.attachment_type.TEXT)
        except NoSuchElementException:
            # Advertisement iframe not found, no need to close
            pass  
