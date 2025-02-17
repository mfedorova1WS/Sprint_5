from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.locators import MainPageLocators, LoginPageLocators, ProfilePageLocators, NavigationBar
from tests.urls import Urls


def test_logout(driver):
    # Открываем страницу входа
    driver.get(Urls.MAIN_PAGE_URL)

    # Нажимаем кнопку "Вход"
    register_button = driver.find_element(*MainPageLocators.LOGIN_BUTTON)
    register_button.click()

    # Вводим email
    email_field = driver.find_element(*LoginPageLocators.EMAIL_FIELD)
    email_field.send_keys('12sfsf3@ya.ru')

     # Вводим пароль
    password_field = driver.find_element(*LoginPageLocators.PASSWORD_FIELD)
    password_field.send_keys('123456789')

    # Нажимаем кнопку "Войти"
    driver.find_element(*LoginPageLocators.SUBMIT_BUTTON).click()

    # Переходим в ЛК
    driver.find_element(*NavigationBar.PROFILE_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
        ProfilePageLocators.PROFILE_TABS))

    # Нажимаем выход
    driver.find_element(*ProfilePageLocators.LOGOUT_BUTTON).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(LoginPageLocators.EMAIL_FIELD))
    element = driver.find_element(*LoginPageLocators.EMAIL_FIELD)
    assert element.is_displayed(), "Элемент не виден"

