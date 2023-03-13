import allure

from pages.start_page import MainPage


@allure.description('Тест на проверку открытия вопроса и печать ответа,'
                    'ВНИМАНИЕ: тест не проходит на небольших мониторах, требуется скролинг вниз')
def test_accordion_questions(browser):
    page = MainPage(browser)
    page.open()
    page.scroll_to_accordion_section()
    page.click_all_accordion_buttons_and_print_answers()
