import allure

from pages.order_page import OrderPage


@allure.description('Тест на возврат на главную странцу Самоката по клику на логотип')
def test_logo_samokat_to_new_page(browser_fire):
    order_page = OrderPage(browser_fire)
    order_page.open()
    order_page.go_to_scooter_home()
    assert browser_fire.current_url == 'https://qa-scooter.praktikum-services.ru/'
