import time

from tests.locators import MainPageLocators, RegisterPageLocators, LoginPageLocators
from tests.urls import Urls


def test_registration_with_valid_conditions(driver):
    # Открываем страницу входа
    driver.get(Urls.MAIN_PAGE_URL)

    # Нажимаем кнопку "Вход"
    driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()

    # Нажимает кнопку регистрации
    registration_button = driver.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
    registration_button.click()

    # Вводим имя
    email_field = driver.find_element(*RegisterPageLocators.NAME_FIELD)
    email_field.send_keys('Вася')

    # Вводим email
    email_field = driver.find_element(*RegisterPageLocators.EMAIL_FIELD)
    email_field.send_keys('12sf7f75483@ya.ru')

    # Вводим пароль
    password_field = driver.find_element(*RegisterPageLocators.PASSWORD_FIELD)
    password_field.send_keys('123456789')

    # Нажимаем кнопку "Зарегистрироваться"
    sign_up_button = driver.find_element(*RegisterPageLocators.SUBMIT_BUTTON)
    sign_up_button.click()

    # Ожидаем увидеть форму входа
    element = driver.find_element(*LoginPageLocators.LOGIN_FORM)
    assert element.is_displayed(), "Элемент не виден"

def test_registration_with_invalid_pass(driver):
    # Открываем страницу входа
    driver.get(Urls.MAIN_PAGE_URL)

    # Нажимаем кнопку "Вход"
    driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()

    # Нажимает кнопку регистрации
    registration_button = driver.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
    registration_button.click()

    # Вводим имя
    email_field = driver.find_element(*RegisterPageLocators.NAME_FIELD)
    email_field.send_keys('Вася')

    # Вводим email
    email_field = driver.find_element(*RegisterPageLocators.EMAIL_FIELD)
    email_field.send_keys('12sf4545457f75483@ya.ru')

     # Вводим пароль
    password_field = driver.find_element(*RegisterPageLocators.PASSWORD_FIELD)
    password_field.send_keys('12345')

    # Нажимаем кнопку "Зарегистрироваться"
    sign_up_button = driver.find_element(*RegisterPageLocators.SUBMIT_BUTTON)
    sign_up_button.click()

    # Ожидаем увидеть валидационное сообщение
    element = driver.find_element(*RegisterPageLocators.VALIDATION_MESSAGE)
    assert element.get_attribute('innerText') == 'Некорректный пароль'
