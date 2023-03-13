import allure
from selenium import webdriver

from pages.order_page import OrderPage


@allure.description('Тест на открытие нового окна и перехода на страницу Яндекс'
                    'ВНИМАНИЕ: тест не проходит так как стоит редирект на Дзен')
def test_logo_yandex_to_new_page():
    driver = webdriver.Chrome()
    driver.maximize_window()  # для отображения всех позиций
    driver.get("https://qa-scooter.praktikum-services.ru/order")
    order_page = OrderPage(driver)
    order_page.go_to_yandex()
    assert "yandex.ru" in driver.current_url
    driver.quit()
