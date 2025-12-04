import allure
from selenium.webdriver.common.by import By
import config.constants as C
from utils.loggers import logger


class ContactPage:

    URL = C.CONTACT_PAGE_URL

    WELCOME_MESSAGE = (By.TAG_NAME, "h1")
    FORM_MESSAGE = (By.CSS_SELECTOR, ".request-form h2")
    MAP = (By.ID, "map")
    FIRST_H3 = (By.CSS_SELECTOR, ".column-info h3:nth-of-type(1)")
    SECOND_H3 = (By.CSS_SELECTOR, ".column-info h3:nth-of-type(2)")

    def __init__(self, driver):
        self.driver = driver
        self.header = (By.CSS_SELECTOR, "h1")
        self.container = (By.CSS_SELECTOR, ".request-form")
        self.fields = {
            "name": (By.CSS_SELECTOR, ".request-form [id='name']"),
            "phone": (By.CSS_SELECTOR, ".request-form [id='phone']"),
            "email": (By.CSS_SELECTOR, ".request-form [id='email']")
        }
        self.submit_button = (By.XPATH, "//button[@type='submit' and normalize-space()='Request call back']")

    @allure.step("Open Contact Page by URL")
    def open(self):
        logger.info("Open ContactPage")
        self.driver.get(self.URL)

    @allure.step("Search for text of header h1")
    def get_header_text(self):
        return self.driver.find_element(*self.WELCOME_MESSAGE).text

    @allure.step("Find the map on the page")
    def is_map_visible(self):
        try:
            return self.driver.find_element(*self.MAP).is_displayed()
        except:
            return False

    @allure.step("Find phone number")
    def get_phone_number(self):
        return self.driver.find_element(By.XPATH, "//a[contains(translate(@href, ' ', ''), '+353873129858')]")

    @allure.step("Find email")
    def get_email(self):
        return self.driver.find_element(By.CSS_SELECTOR, "a[href*='NFO@SAVEENERGY.IE']")

    @allure.step("Find an address")
    def get_company_address(self):
        address = self.driver.find_element(By.XPATH, "//p[span[@class='icon' and text()='🏢']]")
        address_text = address.text.spllitlines()
        return "\n".join(address_text[1:])

    @allure.step("Look for FIRST header h3")
    def get_first_h3(self):
        return self.driver.find_element(*self.FIRST_H3).text

    @allure.step("Look for SECOND header h3")
    def get_second_h3(self):
        return self.driver.find_element(*self.SECOND_H3).text

    @allure.step("Filling in the {field_name} field with the value: {value}")
    def fill_fields(self, field_name, value):
        locator = self.fields[field_name]
        el = self.driver.find_element(*locator)

        el.clear()
        el.send_keys(value)

    @allure.step("Fill the Call Request form")
    def fill_the_form(self, data: dict):
        logger.info("Fill the request Form")
        for key, value in data.items():
            if key not in self.fields:
                continue
            self.fill_fields(key, value)

    @allure.step("Is the form clear?")
    def is_form_clear(self):
        for name, locator in self.fields.items():
            try:
                val = self.driver.find_element(*locator).get_attribute("value")
            except Exception:
                val = None
            if val and val.strip() != "":
                return False
        return True

    @allure.step("Get placeholders")
    def get_placeholder(self, field_name):
        el = self.driver.find_element(*self.fields[field_name])
        return el.get_attribute("placeholder")

    @allure.step("Press the button 'Request call back'")
    def click_submit(self):
        logger.info("Submit request Form")
        self.driver.find_element(*self.submit_button).click()