import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.order_page import OrderPage


@allure.description('Тест для браузера FireFox ')
def test_order_input():
    options = Options()
    options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    driver = webdriver.Firefox(executable_path=r'C:\WebDrivers\geckodriver.exe', options=options)
    driver.maximize_window()  # для отображения всех позиций
    driver.get("https://qa-scooter.praktikum-services.ru/order")
    order_page = OrderPage(driver)
    order_page.remove_cookies()
    order_page.enter_name()
    order_page.enter_surname()
    order_page.enter_address()
    order_page.select_random_station()
    order_page.enter_phone_number()
    order_page.click_next_page_button()
    order_page.select_date()
    order_page.select_rental_period()
    order_page.select_colour_black()
    order_page.enter_comment()
    order_page.click_order_button()
    order_page.click_confirm_order_button()
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.Order_ModalHeader__3FDaJ"))
    )
    assert "Заказ оформлен" in element.text
    assert "Номер заказа:" in element.text
    assert "Запишите его" in element.text

    driver.quit()
