from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver


def test_open_constructor_from_profile():
    # Создаем драйвер
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Открываем страницу входа
    driver.get('https://stellarburgers.nomoreparties.site/')

    # Нажимаем кнопку "Вход"
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button').click()

    # Вводим email
    email_field = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input')
    email_field.send_keys('12sfsf3@ya.ru')

    # Вводим пароль
    password_field = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input')
    password_field.send_keys('123456789')

    # Нажимаем кнопку "Войти"
    submit_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button')
    submit_button.click()

    # Переходим в ЛК
    driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a/p').click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, '//*[@id="root"]/div/main/div/nav/ul/li[3]/button')))

    # Переход в конструктор
    driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/ul/li[1]/a').click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]')))

    # Ожидаем увидеть разделы конструктора
    element = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]')
    assert element.is_displayed(), "Элемент не виден"

    # Закрываем драйвер
    driver.quit()