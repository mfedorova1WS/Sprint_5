from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import LoginPageLocators
from locators import MainPageLocators
from tests.locators import ForgotPasswordPage, NavigationBar
from tests.urls import Urls


def test_login_with_valid_cred_from_main_page(driver):
    # Открываем страницу входа
    driver.get(Urls.MAIN_PAGE_URL)

    # Нажимаем кнопку "Вход"
    driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()

    # Вводим валидный зарегистрированный email
    email_field = driver.find_element(*LoginPageLocators.EMAIL_FIELD)
    email_field.send_keys('12sfsf3@ya.ru')

     # Вводим пароль
    password_field = driver.find_element(*LoginPageLocators.PASSWORD_FIELD)
    password_field.send_keys('123456789')

    # Нажимаем кнопку "Войти"
    submit_button = driver.find_element(*LoginPageLocators.SUBMIT_BUTTON)
    submit_button.click()

    # Ожидаем появления кнопки "Оформить заказ", чтобы убедиться что мы авторизованы
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            MainPageLocators.MAKE_ORDER_BUTTON))

    # Проверяем, что кнопка "Оформить заказ" отображается
    make_order_button = driver.find_element(*MainPageLocators.MAKE_ORDER_BUTTON)
    assert make_order_button.is_displayed()



def test_login_with_valid_cred_from_profile_page(driver):
     # Открываем страницу входа
    driver.get(Urls.MAIN_PAGE_URL)

    # Нажимаем кнопку "Личный кабинет"
    driver.find_element(*NavigationBar.PROFILE_BUTTON).click()

    # Вводим валидный зарегистрированный email
    email_field = driver.find_element(*LoginPageLocators.EMAIL_FIELD)
    email_field.send_keys('12sfsf3@ya.ru')

     # Вводим пароль
    password_field = driver.find_element(*LoginPageLocators.PASSWORD_FIELD)
    password_field.send_keys('123456789')

    # Нажимаем кнопку "Войти"
    submit_button = driver.find_element(*LoginPageLocators.SUBMIT_BUTTON)
    submit_button.click()

    # Ожидаем появления кнопки "Оформить заказ", чтобы убедиться что мы авторизованы
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            MainPageLocators.MAKE_ORDER_BUTTON))

    # Проверяем, что кнопка "Оформить заказ" отображается
    make_order_button = driver.find_element(*MainPageLocators.MAKE_ORDER_BUTTON)
    assert make_order_button.is_displayed()


def test_login_with_valid_cred_from_restore_password_page(driver):
    # Открываем страницу восстановления пароля
    driver.get(Urls.FORGOT_PASSWORD_URL)

    # Нажимаем кнопку "Войти"
    driver.find_element(*ForgotPasswordPage.LOGIN_BUTTON).click()

    # Вводим валидный зарегистрированный email
    email_field = driver.find_element(*LoginPageLocators.EMAIL_FIELD)
    email_field.send_keys('12sfsf3@ya.ru')

     # Вводим пароль
    password_field = driver.find_element(*LoginPageLocators.PASSWORD_FIELD)
    password_field.send_keys('123456789')

    # Нажимаем кнопку "Войти"
    submit_button = driver.find_element(*LoginPageLocators.SUBMIT_BUTTON)
    submit_button.click()

    # Ожидаем появления кнопки "Оформить заказ", чтобы убедиться что мы авторизованы
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            MainPageLocators.MAKE_ORDER_BUTTON))

    # Проверяем, что кнопка "Оформить заказ" отображается
    make_order_button = driver.find_element(*MainPageLocators.MAKE_ORDER_BUTTON)
    assert make_order_button.is_displayed()

def test_login_with_invalid_pass(driver):
    # Открываем страницу входа
    driver.get(Urls.MAIN_PAGE_URL)

    # Нажимаем кнопку "Вход"
    driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()

    # Вводим валидный зарегистрированный email
    email_field = driver.find_element(*LoginPageLocators.EMAIL_FIELD)
    email_field.send_keys('12sfsf3@ya.ru')

    # Вводим некорректный пароль
    password_field = driver.find_element(*LoginPageLocators.PASSWORD_FIELD)
    password_field.send_keys('123')

    # Нажимаем кнопку "Войти"
    submit_button = driver.find_element(*LoginPageLocators.SUBMIT_BUTTON)
    submit_button.click()

    # Проверяем, что валидационное сообщение отображается
    validation_message = driver.find_element(*LoginPageLocators.VALIDATION_MESSAGE)
    assert validation_message.get_attribute('innerText') == 'Некорректный пароль'

