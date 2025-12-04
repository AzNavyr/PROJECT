import pytest
import allure

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils.loggers import logger
from pages.home_page import HomePage
from pages.contact_page import ContactPage

@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # запускаем в фоне
    chrome_options.add_argument("--disable-gpu")
    #chrome_options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=chrome_options)
    #driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def home_page(driver):
    home_page = HomePage(driver)
    home_page.open()
    return home_page

@pytest.fixture
def contact_page_via_home(driver, home_page):
    home_page.go_to_contact_page()
    page = ContactPage(driver)
    return page

@pytest.fixture
def contact_page(driver):
    contact_page = ContactPage(driver)
    contact_page.open()
    return contact_page

@allure.epic("Contact Page")
@allure.feature("Call Request")
@allure.story("Form Submission")
@allure.tag("e2e", "smoke", "ui")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Submit Call Request Form")
@allure.description("Verifies that the Call Request form can be successfully filled and submitted.")
def test_submit_call_request(home_page):

    with allure.step("Open Home Page and make sure that you are on the right page"):
        assert "Solar PV Energy" in home_page.get_welcome_text()

    with allure.step("Go to the contacts section and make sure that you are on the right page"):
        contact = home_page.go_to_contact_page()
        assert "Our contacts" in contact.get_header_text()

    data = {
        "name": "John Doe",
        "phone": "+7548988988",
        "email": "example@mail.com"
    }

    with allure.step("Fill out the Call Request form"):
        contact.fill_the_form(data)

    contact.click_submit()
    logger.info("Start step: Submit request Form")
    logger.debug("Submit issues")
    with allure.step("Submission filled form"):
        assert contact.is_form_clear() is True

@allure.epic("Contact Page")
@allure.feature("Call Request")
@allure.story("Placeholders")
@allure.tag("ui")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Check placeholders")
@allure.description("Verifies that each field of Call Request form has placeholder.")
@pytest.mark.parametrize(
   "field_name, placeholder",[
        ("name", "Your name"),
        ("phone", "Your phone"),
        ("email", "Your email (optional)")
    ]
)
def test_availability_of_placeholders(contact_page, field_name, placeholder):
    placeholder_text = contact_page.get_placeholder(field_name)
    assert placeholder_text == placeholder

@allure.epic("Contact Page")
@allure.feature("Call Request")
@allure.story("Map")
@allure.tag("ui")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Check visibility of Map")
@allure.description("Verifies that GoogleMap is visible.")
def test_is_map_visible(contact_page):
    logger.info("Starting test: Map visibility check")
    logger.debug("Map representation issue")
    assert contact_page.is_map_visible is True

