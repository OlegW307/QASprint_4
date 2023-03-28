import allure

from pages.start_page import MainPage


@allure.description('Проверка открытия одиночного вопроса и получение ответа на него')
def test_accordion_questions(browser):
    page = MainPage(browser)
    page.open()
    page.scroll_to_accordion_section()
    answer = page.click_single_accordion_buttons()
    assert answer.text != '', "Answer text is empty"