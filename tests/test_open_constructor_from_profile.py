from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.locators import MainPageLocators, LoginPageLocators, ProfilePageLocators, NavigationBar
from tests.urls import Urls


def test_open_constructor_from_profile(driver):
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

    # Переходим в ЛК
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
        NavigationBar.PROFILE_BUTTON))
    driver.find_element(*NavigationBar.PROFILE_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
        ProfilePageLocators.PROFILE_TABS))

    # Переход в конструктор
    driver.find_element(*NavigationBar.CONSTRUCTOR_BUTTON).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(MainPageLocators.CONSTRUCTOR_BUNS_TAB))

    # Ожидаем увидеть раздел конструктора
    element = driver.find_element(*MainPageLocators.CONSTRUCTOR_BUNS_TAB)
    assert element.is_displayed(), "Элемент не виден"
