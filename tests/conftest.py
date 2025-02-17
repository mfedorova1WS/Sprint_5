import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver():
    service = Service(executable_path=ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  # Максимизация окна браузера

    # Создаем объект драйвера
    _driver = webdriver.Chrome(service=service, options=options)

    return _driver  # Возвращаем драйвер в тест