from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from locators import LoginPageLocators
from locators import MainPageLocators
from urls import Urls

@pytest.mark.parametrize("constructor_tab, expected_tab_title, message",
                         [(MainPageLocators.CONSTRUCTOR_FILLING_TAB, MainPageLocators.CONSTRUCTOR_FILLING_TAB_TITLE, "Элемент 'Начинки' не виден"),
                          (MainPageLocators.CONSTRUCTOR_SAUCE_TAB, MainPageLocators.CONSTRUCTOR_SAUCE_TAB_TITLE, "Элемент 'Соусы' не виден"),
                          (MainPageLocators.CONSTRUCTOR_BUNS_TAB, MainPageLocators.CONSTRUCTOR_BUNS_TAB_TITLE, "Элемент 'Булки' не виден")])
def test_open_constructor_tabs(driver, constructor_tab,expected_tab_title, message):

    # Открываем страницу входа
    driver.get(Urls.MAIN_PAGE_URL)

    # Нажимаем кнопку "Вход"
    driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()

    # Вводим email
    email_field = driver.find_element(*LoginPageLocators.EMAIL_FIELD)
    email_field.send_keys('12sfsf3@ya.ru')

    # Вводим пароль
    password_field = driver.find_element(*LoginPageLocators.PASSWORD_FIELD)
    password_field.send_keys('123456789')

    # Нажимаем кнопку "Войти"
    submit_button = driver.find_element(*LoginPageLocators.SUBMIT_BUTTON)
    submit_button.click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(constructor_tab))

    # Получаем элемент вкладки
    tab_element = driver.find_element(*constructor_tab)

    # Проверяем, является ли элемент доступным для клика
    if "tab_tab_type_current__2BEPc" not in tab_element.get_attribute("class"):
        # Кликнем на вкладку, если она доступна
        tab_element.click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(expected_tab_title))
    else:
        # Если вкладка неактивная, значит она уже выбрана, переходим к проверке
        pass

    # Проверяем наличие заголовка
    element = driver.find_element(*expected_tab_title)
    assert element.is_displayed(), message
