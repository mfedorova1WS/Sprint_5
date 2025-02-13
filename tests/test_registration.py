from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver


def test_registration_with_valid_conditions():
    # Создаем драйвер
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Открываем страницу входа
    driver.get('https://stellarburgers.nomoreparties.site/')

    # Нажимаем кнопку "Вход"
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button').click()

    # Нажимает кнопку регистрации
    registration_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p[1]/a')
    registration_button.click()

    # Вводим имя
    email_field = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input')
    email_field.send_keys('Вася')

    # Вводим email
    email_field = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input')
    email_field.send_keys('12sf7f75483@ya.ru')

     # Вводим пароль
    password_field = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input')
    password_field.send_keys('123456789')

    # Нажимаем кнопку "Зарегистрироваться"
    sign_up_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button')
    sign_up_button.click()

    # Ожидаем увидеть форму входа
    element = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/h2')
    assert element.is_displayed(), "Элемент не виден"

    # Закрываем драйвер
    driver.quit()

def test_registration_with_invalid_pass():
    # Создаем драйвер
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Открываем страницу входа
    driver.get('https://stellarburgers.nomoreparties.site/')

    # Нажимаем кнопку "Вход"
    driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button').click()

    # Нажимает кнопку регистрации
    registration_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p[1]/a')
    registration_button.click()

    # Вводим имя
    email_field = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input')
    email_field.send_keys('Вася')

    # Вводим email
    email_field = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input')
    email_field.send_keys('12sf4545457f75483@ya.ru')

     # Вводим пароль
    password_field = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input')
    password_field.send_keys('12345')

    # Нажимаем кнопку "Зарегистрироваться"
    sign_up_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button')
    sign_up_button.click()

    # Ожидаем увидеть валидационное сообщение
    element = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/p')
    assert element.get_attribute('innerText') == 'Некорректный пароль'

    # Закрываем драйвер
    driver.quit()