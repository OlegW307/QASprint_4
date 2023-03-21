import allure
import pytest
from pages.start_page import MainPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@allure.description('Отдельный тест на проверку открытия вопроса и печать ответа')
@pytest.mark.parametrize("number", range(8))
def test_accordion_questions(browser, number):
    page = MainPage(browser)
    page.open()
    page.scroll_to_accordion_section()
    button = browser.find_element(By.XPATH, f"//div[contains(@id, 'accordion__heading-{number}')]")
    button.click()
    answer_id = button.get_attribute("aria-controls")
    answer = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, answer_id)))
    print(answer.text)
