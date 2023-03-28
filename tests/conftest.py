import pytest
from locators.locators import HomePageLocators
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def browser_fire():
    driver = webdriver.Firefox(executable_path='./geckodriver')
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def num_questions(browser):
    buttons = WebDriverWait(browser, 10).until(
        EC.visibility_of_all_elements_located(HomePageLocators.ACCORDION_BUTTONS))
    return len(buttons)
