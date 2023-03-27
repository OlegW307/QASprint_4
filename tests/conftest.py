import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators.locators import HomePageLocators, OrderPageLocators


@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

# @pytest.fixture(scope='function')
# def browser(request):
#     browser_driver = webdriver.Chrome(executable_path='./chromedriver')
#     browser_driver.get(request.param)
#     yield browser_driver
#     browser_driver.quit()


@pytest.fixture()
def browser_fire():
    # options = Options()
    # options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    # driver = webdriver.Firefox(executable_path=r'C:\WebDrivers\geckodriver.exe', options=options)
    driver = webdriver.Firefox(executable_path='./geckodriver')
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def num_questions(browser):
    buttons = WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located(HomePageLocators.ACCORDION_BUTTONS))
    return len(buttons)
