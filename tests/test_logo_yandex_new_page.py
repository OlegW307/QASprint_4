import allure

from pages.order_page import OrderPage


@allure.description('Тест на открытие нового окна и перехода на страницу Яндекс'
                    'ВНИМАНИЕ: тест не проходит так как стоит редирект на Дзен')
def test_logo_yandex_to_new_page(browser_fire):
    order_page = OrderPage(browser_fire)
    order_page.open()
    order_page.go_to_yandex()
    assert "yandex.ru" in browser_fire.current_url
