import allure

from pages.order_page import OrderPage


@allure.description('Тест на открытие нового окна и перехода на страницу Яндекс'
                    'ВНИМАНИЕ: тест не проходит так как стоит редирект на Дзен')
def test_logo_yandex_to_new_page(browser):
    browser.get("https://qa-scooter.praktikum-services.ru/order")
    order_page = OrderPage(browser)
    order_page.go_to_yandex()
    assert "yandex.ru" in browser.current_url
