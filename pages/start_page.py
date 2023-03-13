import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import HomePageLocators

class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://qa-scooter.praktikum-services.ru/")

    @allure.step('Едем до раздела Вопросы о важном')
    def scroll_to_accordion_section(self):
        accordion_section = self.driver.find_element(*HomePageLocators.ACCORDION_SECTION)
        self.driver.execute_script("arguments[0].scrollIntoView();", accordion_section)

    @allure.step('Проверяем открытие одиного вопроса')
    def click_single_accordion_buttons(self):
        button = self.driver.find_element(*HomePageLocators.SINGLE_BUTTONS)
        button.click()
        answer_id = button.get_attribute("aria-controls")
        answer = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, answer_id)))
        print(answer.text)

    @allure.step('Проверяем открытие всех вопросов')
    def click_all_accordion_buttons_and_print_answers(self):
        buttons = self.driver.find_elements(*HomePageLocators.ACCORDION_BUTTONS)
        for button in buttons:
            button.click()
            answer_id = button.get_attribute("aria-controls")
            answer = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, answer_id)))
            print(answer.text)


    def switch_to_order_page_top(self):
        button_switch = self.driver.find_element(*HomePageLocators.ORDER_TOP_BUTTON)
        button_switch.clic()

    def switch_to_order_page_middle(self):
        button_switch = self.driver.find_element(*HomePageLocators.ORDER_MIDDLE_BUTTON)
        button_switch.clic()