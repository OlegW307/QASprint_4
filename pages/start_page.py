from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from locators.locators import HomePageLocators

class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://qa-scooter.praktikum-services.ru/")

    def scroll_to_accordion_section(self):
        accordion_section = self.driver.find_element(*HomePageLocators.ACCORDION_SECTION)
        self.driver.execute_script("arguments[0].scrollIntoView();", accordion_section)

    def click_all_accordion_buttons_and_print_answers(self):
        buttons = self.driver.find_elements(*HomePageLocators.ACCORDION_BUTTONS)
        for button in buttons:
            button.click()
            answer_id = button.get_attribute("aria-controls")
            answer = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, answer_id)))
            print(answer.text)
            time.sleep(2)

    def switch_to_order_page_top(self):
        button_switch = self.driver.find_element(*HomePageLocators.ORDER_TOP_BUTTON)
        button_switch.clic()

    def switch_to_order_page_middle(self):
        button_switch = self.driver.find_element(*HomePageLocators.ORDER_MIDDLE_BUTTON)
        button_switch.clic()