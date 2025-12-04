import allure
from selenium.webdriver.common.by import By
import config.constants as C
from pages.contact_page import ContactPage
from utils.loggers import logger


class HomePage:

    URL = C.HOME_PAGE_URL

    WELCOME_MESSAGE = (By.TAG_NAME, "h1")
    FORM_MESSAGE = (By.CSS_SELECTOR, ".request-form h2")
    CONTACT_PAGE = (By.CSS_SELECTOR, "a[href='contact.html']")

    def __init__(self, driver):
        self.driver = driver
        self.header = (By.CSS_SELECTOR, "h1")
        self.pictures = (By.CSS_SELECTOR, ".image-column img")
        self.container = (By.CSS_SELECTOR, ".request-form")
        self.fields = {
            "firstname": (By.ID, "firstname"),
            "surname": (By.ID, "surname"),
            "date": (By.ID, "date"),
            "time": (By.ID, "time"),
            "email": (By.ID, "email"),
            "notes": (By.ID, "notes"),  # textarea
        }
        self.submit_button = (By.CSS_SELECTOR, ".request-form input[type='button'][value='Submit Form']")

    @allure.step("Go to Contact page")
    def go_to_contact_page(self):
        logger.info("Navigating to Contact Page")
        self.driver.find_element(*self.CONTACT_PAGE).click()
        return ContactPage(self.driver)

    @allure.step("Open the URL")
    def open(self):
        logger.info(f"Open HomePage: '{self.URL}'")
        self.driver.get(self.URL)

    @allure.step("Search for text of header h1")
    def get_welcome_text(self):
        return self.driver.find_element(*self.WELCOME_MESSAGE).text

    @allure.step("Search for video elements on the homepage")
    def is_video_present(self):
        videos = self.driver.find_elements(By.TAG_NAME, "video")
        return len(videos) > 0

    @allure.step("Video playback")
    def is_video_playing(self):
        videos = self.driver.find_elements(By.TAG_NAME, "video")
        if not videos:
            return False
        return not self.driver.execute_script("return arguments[0].paused", videos[0])

    @allure.step("Search for text of header h2")
    def get_form_text(self):
        return self.driver.find_element(*self.FORM_MESSAGE).text

    @allure.step("Checking that the form container is present")
    def is_container_present(self):
        return len(self.driver.find_elements(*self.container)) > 0

    @allure.step("Checking for the presence of the field: '{field_name}'")
    def is_field_presented(self, field_name):
        locator = self.fields.get(field_name)
        if not locator:
            raise ValueError(f"Unknown field: {field_name}")
        return len(self.driver.find_elements(*locator)) > 0

    @allure.step("Filling in the '{field_name}' field with the value: '{value}'")
    def fill_field(self, field_name, value):
        locator = self.fields[field_name]
        el = self.driver.find_element(*locator)

        field_type = el.get_attribute("type")
        if field_type == "date":
            # ставим значение напрямую через JS
            self.driver.execute_script("arguments[0].value = arguments[1];", el, value)
        else:
            el.clear()
            el.send_keys(value)

    @allure.step("Getting a list of all fields (id)")
    def get_field_ids(self):
        return list(self.fields.keys())

    @allure.step("Reading the value of the '{field_name}' field")
    def get_fieled_value(self, field_name):
        el = self.driver.find_element(*self.fields[field_name])
        # для textarea/value обычное значение берём через .get_attribute("value")
        return el.get_attribute("value")

    @allure.step("Click submit button")
    def submit_form(self):
        logger.info("Submit the Form")
        self.driver.find_element(*self.submit_button).click()

    @allure.step("Fill the form")
    def fill_the_form(self, data: dict):
        logger.info("Fill the Form")
        for key, value in data.items():
            if key not in self.fields:
                continue
            self.fill_field(key, value)

    @allure.step("Get placeholder for field '{field_name}'")
    def get_placeholder(self, field_name):
        el = self.driver.find_element(*self.fields[field_name])
        return el.get_attribute('placeholder')