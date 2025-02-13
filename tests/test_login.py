from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver


def test_login_with_valid_cred_from_main_page():
    # Создаем драйвер
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Открываем страницу входа
    driver.get('https://stellarburgers.nomoreparties.site/')

    # Нажимаем кнопку "Вход"
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button').click()

    # Вводим валидный зарегистрированный email
    email_field = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input')
    email_field.send_keys('12sfsf3@ya.ru')

     # Вводим пароль
    password_field = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input')
    password_field.send_keys('123456789')

    # Нажимаем кнопку "Войти"
    submit_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button')
    submit_button.click()

    # Ожидаем появления кнопки "Оформить заказ", чтобы убедиться что мы авторизованы
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button')))

    # Проверяем, что кнопка "Оформить заказ" отображается
    make_order_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button')
    assert make_order_button.is_displayed()

    # Закрываем драйвер
    driver.quit()


def test_login_with_valid_cred_from_profile_page():
    # Создаем драйвер
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Открываем страницу входа
    driver.get('https://stellarburgers.nomoreparties.site/')

    # Нажимаем кнопку "Личный кабинет"
    driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a/p').click()

    # Вводим валидный зарегистрированный email
    email_field = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input')
    email_field.send_keys('12sfsf3@ya.ru')

     # Вводим пароль
    password_field = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input')
    password_field.send_keys('123456789')

    # Нажимаем кнопку "Войти"
    submit_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button')
    submit_button.click()

    # Ожидаем появления кнопки "Оформить заказ", чтобы убедиться что мы авторизованы
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button')))

    # Проверяем, что кнопка "Оформить заказ" отображается
    make_order_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button')
    assert make_order_button.is_displayed()

    # Закрываем драйвер
    driver.quit()

def test_login_with_valid_cred_from_restore_password_page():
    # Создаем драйвер
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Открываем страницу входа
    driver.get('https://stellarburgers.nomoreparties.site/forgot-password')

    # Нажимаем кнопку "Войти"
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p/a').click()

    # Вводим валидный зарегистрированный email
    email_field = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input')
    email_field.send_keys('12sfsf3@ya.ru')

     # Вводим пароль
    password_field = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input')
    password_field.send_keys('123456789')

    # Нажимаем кнопку "Войти"
    submit_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button')
    submit_button.click()

    # Ожидаем появления кнопки "Оформить заказ", чтобы убедиться что мы авторизованы
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button')))

    # Проверяем, что кнопка "Оформить заказ" отображается
    make_order_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button')
    assert make_order_button.is_displayed()

    # Закрываем драйвер
    driver.quit()

def test_login_with_invalid_pass():
    # Создаем драйвер
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Открываем страницу входа
    driver.get('https://stellarburgers.nomoreparties.site/')

    # Нажимаем кнопку "Вход"
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button').click()

    # Вводим валидный зарегистрированный email
    email_field = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input')
    email_field.send_keys('12sfsf3@ya.ru')

    # Вводим некорректный пароль
    password_field = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input')
    password_field.send_keys('123')

    # Нажимаем кнопку "Войти"
    submit_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button')
    submit_button.click()

    # Проверяем, что валидационное сообщение отображается
    validation_message = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/p')
    assert validation_message.get_attribute('innerText') == 'Некорректный пароль'

    # Закрываем драйвер
    driver.quit()