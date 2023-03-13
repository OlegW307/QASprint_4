from selenium.webdriver.common.by import By

# локаторы главной страницы
class HomePageLocators:
    # вопросы о важном
    ACCORDION_SECTION = (By.XPATH, "//div[contains(text(), 'Вопросы о важном')]")
    ACCORDION_BUTTONS = (By.XPATH, "//div[contains(@id, 'accordion__heading-')]")
    # кнопки заказать
    ORDER_TOP_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and text()='Заказать']")
    ORDER_MIDDLE_BUTTON = (By.CLASS_NAME, "Button_Button__ra12g.Button_UltraBig__UU3Lp")

# локаторы страницы оформления заказа
class OrderPageLocators:
    COOKIES_BUTTON = (By.ID, "rcc-confirm-button")

    # первый экран формы
    FIRST_NAME_INPUT = (By.XPATH, ".//input[@placeholder='* Имя']")
    SECOND_NAME_INPUT = (By.XPATH, ".//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")

    METRO_INPUT = (By.CLASS_NAME, "select-search__input")
    METRO_STATION_LIST = (By.CLASS_NAME, "select-search__option")

    PHONE_INPUT = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.CLASS_NAME, 'Button_Button__ra12g.Button_Middle__1CSJM')

    # второй экран формы
    DATE_INPUT = (By.CSS_SELECTOR, "div.react-datepicker__input-container > input")
    BODY = (By.XPATH, '//body')
    RENTAL_PERIOD_DROPDOWN = (By.CLASS_NAME, "Dropdown-placeholder")
    RENTAL_PERIOD_OPTION = (By.XPATH, '//div[@class="Dropdown-option" and @role="option" and @aria-selected="false" and contains(text(), "четверо суток")]')
    BLACK_CHECKBOX = (By.XPATH, '//label[@for="black"]/input[@type="checkbox"]')
    GREY_CHECKBOX = (By.XPATH, '//label[@for="grey"]/input[@type="checkbox"]')
    COMMENT_INPUT = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "/html/body/div/div/div[2]/div[3]/button[2]")
    CONFIRM_BUTTON = (By.XPATH, "/html/body/div/div/div[2]/div[5]/div[2]/button[2]")
    ORDER_SUCCESS_MESSAGE = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")

    # логотипы
    YANDEX_LOGO = (By.CSS_SELECTOR, "a.Header_LogoYandex__3TSOI")
    SAMOKAT_LOGO = (By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']")


