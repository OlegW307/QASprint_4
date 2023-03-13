import random


from generators import generate_name, generate_adress, generate_phone_number, date_to_order
from locators.locators import OrderPageLocators


class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://qa-scooter.praktikum-services.ru/order")

    def remove_cookies(self):
        cookie_button_element = self.driver.find_element(*OrderPageLocators.COOKIES_BUTTON)
        cookie_button_element.click()

    def enter_name(self):
        name_input = self.driver.find_element(*OrderPageLocators.FIRST_NAME_INPUT)
        name_input.send_keys(generate_name())

    def enter_surname(self):
        surname_input = self.driver.find_element(*OrderPageLocators.SECOND_NAME_INPUT)
        surname_input.send_keys(generate_name())

    def enter_address(self):
        address_input = self.driver.find_element(*OrderPageLocators.ADDRESS_INPUT)
        address_input.send_keys(generate_adress())

    def select_random_station(self):
        input_elem = self.driver.find_element(*OrderPageLocators.METRO_INPUT)
        input_elem.click()
        options = self.driver.find_elements(*OrderPageLocators.METRO_STATION_LIST)
        random_station = random.choice(options)
        random_station.click()

    def enter_phone_number(self):
        phone_input = self.driver.find_element(*OrderPageLocators.PHONE_INPUT)
        phone_input.send_keys(generate_phone_number())

    def click_next_page_button(self):
        next_page_button = self.driver.find_element(*OrderPageLocators.NEXT_BUTTON)
        next_page_button.click()

    def select_date(self):
        date_picker = self.driver.find_element(*OrderPageLocators.DATE_INPUT)
        date_picker.send_keys(date_to_order())
        self.driver.find_element(*OrderPageLocators.BODY).click()

    def select_rental_period(self):
        rental_period_dropdown = self.driver.find_element(*OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        rental_period_dropdown.click()
        rental_period_option = self.driver.find_element(*OrderPageLocators.RENTAL_PERIOD_OPTION)
        rental_period_option.click()

    def select_colour_grey(self):
        scooter_colour = self.driver.find_element(*OrderPageLocators.GREY_CHECKBOX)
        scooter_colour.click()

    def select_colour_black(self):
        scooter_colour = self.driver.find_element(*OrderPageLocators.BLACK_CHECKBOX)
        scooter_colour.click()

    def enter_comment(self):
        comment_input = self.driver.find_element(*OrderPageLocators.COMMENT_INPUT)
        comment_input.send_keys(7 * generate_name())

    def click_order_button(self):
        order_button = self.driver.find_element(*OrderPageLocators.ORDER_BUTTON)
        order_button.click()

    def click_confirm_order_button(self):
        confirm_order_button = self.driver.find_element(*OrderPageLocators.CONFIRM_BUTTON)
        confirm_order_button.click()

    def go_to_yandex(self):
        logo_link = self.driver.find_element(*OrderPageLocators.YANDEX_LOGO)
        logo_link.click()
        self.driver.switch_to.window(self.driver.window_handles[1])

    def go_to_scooter_home(self):
        logo_link = self.driver.find_element(*OrderPageLocators.SAMOKAT_LOGO)
        logo_link.click()
        assert self.driver.current_url == "https://qa-scooter.praktikum-services.ru/"
