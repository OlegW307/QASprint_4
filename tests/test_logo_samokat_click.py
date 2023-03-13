import allure
from selenium import webdriver

from pages.order_page import OrderPage


@allure.description('Тест на возврат на главную странцу Самоката по клику на логотип')
def test_logo_samokat_to_new_page():
    driver = webdriver.Chrome()
    driver.maximize_window()  # для отображения всех позиций
    driver.get("https://qa-scooter.praktikum-services.ru/order")
    order_page = OrderPage(driver)
    order_page.go_to_scooter_home()
    driver.quit()
