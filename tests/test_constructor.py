from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
import pytest

@pytest.mark.parametrize("tab_xpath, expected_element_xpath, message",
                         [('//*[@id="root"]/div/main/section[1]/div[1]/div[3]', '//*[@id="root"]/div/main/section[1]/div[2]/h2[3]', "Элемент 'Начинки' не виден"),
                          ('//*[@id="root"]/div/main/section[1]/div[1]/div[2]', '//*[@id="root"]/div/main/section[1]/div[2]/h2[2]', "Элемент 'Соусы' не виден"),
                          ('//*[@id="root"]/div/main/section[1]/div[1]/div[1]', '//*[@id="root"]/div/main/section[1]/div[2]/h2[1]', "Элемент 'Булки' не виден")])
def test_open_constructor_from_profile(tab_xpath,expected_element_xpath, message):
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
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, tab_xpath)))

    # Получаем элемент вкладки
    tab_element = driver.find_element(By.XPATH, tab_xpath)

    # Проверяем, является ли элемент доступным для клика
    if "tab_tab_type_current__2BEPc" not in tab_element.get_attribute("class"):
        # Кликнем на вкладку, если она доступна
        tab_element.click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, expected_element_xpath)))
    else:
        # Если вкладка неактивная, значит она уже выбрана, переходим к проверке
        pass

    # Проверяем наличие заголовка
    element = driver.find_element(By.XPATH, expected_element_xpath)
    assert element.is_displayed(), message

    # Закрываем драйвер
    driver.quit()