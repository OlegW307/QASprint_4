import allure
from pages.order_page import OrderPage
from selenium.webdriver.common.by import By


@allure.description('Тест заказа Самоката для браузера FireFox ')
def test_order_input(browser_fire):
    order_page = OrderPage(browser_fire)
    order_page.open()
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
    element = order_page.find_element((By.CSS_SELECTOR, "div.Order_ModalHeader__3FDaJ"))
    assert "Заказ оформлен" in element.text
    assert "Номер заказа:" in element.text
    assert "Запишите его" in element.text
