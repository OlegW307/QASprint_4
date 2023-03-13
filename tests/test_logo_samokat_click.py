import allure

from pages.order_page import OrderPage


@allure.description('Тест на возврат на главную странцу Самоката по клику на логотип')
def test_logo_samokat_to_new_page(browser):
    browser.get("https://qa-scooter.praktikum-services.ru/order")
    order_page = OrderPage(browser)
    order_page.go_to_scooter_home()
