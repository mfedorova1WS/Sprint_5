from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.locators import MainPageLocators, LoginPageLocators, NavigationBar, ProfilePageLocators
from tests.urls import Urls


def test_open_profile(driver):
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

    # Ожидаем, что боковая панель в ЛК отображена
    profile_navigation = driver.find_element(*ProfilePageLocators.PROFILE_TABS)
    assert profile_navigation.is_displayed()
