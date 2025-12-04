import pytest
import allure

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils.loggers import logger
from pages.home_page import HomePage

EXPECTED_FIELDS = ["firstname", "surname", "date", "time", "email", "notes"]

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
def home_page(driver):  # driver передаётся автоматически из другой фикстуры
    home_page = HomePage(driver)
    home_page.open()
    return home_page


@allure.epic("Home Page")
@allure.feature("UI Validation")
@allure.story("Header Visibility")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("ui", "smoke")
@allure.title("Verify Home Page Header")
@allure.description("Validates that the main header is correctly displayed on the Home page.")
def test_home_open(home_page):
    header = home_page.get_welcome_text()
    assert "Solar PV Energy" in header

@allure.epic("Home Page")
@allure.feature("UI Elements")
@allure.story("Media Content")
@allure.tag("ui", "smoke")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Verify Home Page Video Visibility")
@allure.description("Checks that the promotional video element is displayed on the Home page.")
def test_home_video(home_page):
    assert home_page.is_video_present(), "The video is missing from the page."

@allure.epic("Home Page")
@allure.feature("Request Form")
@allure.story("UI Validation")
@allure.tag("ui", "smoke")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Verify Request Form Header Visibility")
@allure.description("Checks that the Request Form has a visible and non-empty header.")
def test_request_form_header(home_page):
    header = home_page.get_form_text()
    assert "Book Your Consultation" in header

@allure.epic("Home Page")
@allure.feature("Request Form")
@allure.story("UI Validation")
@allure.tag("ui", "smoke")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Verify Input Field Names")
@allure.description("Validates that all expected input fields are present within the Request Form.")
def test_input_names_are_presented(home_page):
    assert home_page.is_container_present(), "The form container was not found"
    assert home_page.get_form_text().strip() != "", "The form header is empty"

    # We check the presence of all fields with a single test
    for fid in EXPECTED_FIELDS:
        assert home_page.is_field_presented(fid), f"The {fid} field is missing on the page"

@allure.epic("Home Page")
@allure.feature("Request Form")
@allure.story("Form Interaction")
@allure.tag("ui", "smoke")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Fill the Request Form Fields")
@allure.description("Verifies that each input field in the Request Form can be filled with valid data.")
@pytest.mark.parametrize(
    'field_name, value',
    [
        ("firstname", "John"),
        ("surname", "Doe"),
        ("date", "14-11-2025"),   # Format DD-MM-YYYY for input[type=date]
        ("time", "14:30"),        # Format HH:MM
        ("email", "john.doe@example.com"),
        ("notes", "Some additional info"),
    ]
)
def test_field_input_and_value(home_page, field_name, value):
    logger.info("Fill the form")
    logger.debug("Filled form issue, additional info")
    assert home_page.is_field_presented(field_name), f"{field_name} not found"

    home_page.fill_field(field_name, value)

    # Проверяем, что значение записалось в поле
    val = home_page.get_fieled_value(field_name)
    assert val == value, f"Expected '{value}' in {field_name}, but got '{val}'"

@allure.epic("Home Page")
@allure.feature("Request Form")
@allure.story("Form Submission")
@allure.tag("functional", "e2e")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Submit the Filled Request Form")
@allure.description("Checks that the Request Form can be successfully filled and submitted with valid data.")
def test_fill_entire_form_and_submit_shows_alert(home_page):
    data = {
        "firstname": "Alice",
        "surname": "Smith",
        "date": "2025-11-20",
        "time": "09:00",
        "email": "alice.smith@example.com",
        "notes": "Test submission"
    }
    logger.info("Fill The Form")
    logger.debug("Filled form issue")
    home_page.fill_the_form(data)

    # Нажимаем submit — в твоём HTML это input type="button" с onclick alert(...)
    home_page.submit_form()

    # Обрабатываем JS alert
    alert = home_page.driver.switch_to.alert
    alert_text = alert.text
    assert "submitted" in alert_text.lower() or "submitted successful" in alert_text.lower() or "has been submitted" in alert_text.lower(), \
        f"Unexpected alert text: {alert_text}"
    alert.accept()

@allure.epic("Home Page")
@allure.feature("Request Form")
@allure.story("Input Field Validation")
@allure.tag("ui", "smoke")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Check Availability of Input Placeholders")
@allure.description("Verifies that all required input fields contain correct placeholder text.")
@pytest.mark.parametrize("field_name, placeholder", [
    ("firstname", "Your first name..."),
    ("surname", "Your surname..."),
    ("notes", "Enter any additional information..."),
])
def test_availlability_of_placeholders(home_page, field_name, placeholder):
    placeholder_text = home_page.get_placeholder(field_name)
    assert placeholder_text == placeholder