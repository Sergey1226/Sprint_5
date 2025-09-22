import pytest
import time
import random
import string
from data import USER_EMAIL
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  # Добавлен импорт EC

# Фикстура для создания драйвера
@pytest.fixture
def driver():
    """Фикстура для создания драйвера Chrome"""
    driver = webdriver.Chrome()  # Без дополнительных настроек
    yield driver
    driver.quit()


# Фикстура для ожидания
@pytest.fixture
def wait(driver):
    """Фикстура для WebDriverWait с таймаутом 10 секунд"""
    return WebDriverWait(driver, timeout=10)


# Фикстура для генерации уникального email
@pytest.fixture
def generate_unique_email():
    """Генерация уникального email"""
    return USER_EMAIL.format(time.time())  # или использовать uuid для уникальности


# Фикстура для открытия страницы и нажатия кнопок
@pytest.fixture
def open_registration_page(driver, wait):
    """Открытие страницы и нажатие кнопок для регистрации"""
    from data import BASE_URL
    from locators import Locators

    driver.get(BASE_URL)
    
    login_button = wait.until(EC.element_to_be_clickable(Locators.LOGIN_REGISTER_BUTTON))
    login_button.click()

    no_account_button = wait.until(EC.element_to_be_clickable(Locators.NO_ACCOUNT_BUTTON))
    no_account_button.click()

    return driver, wait


@pytest.fixture
def open_login_page(driver, wait):
    """Открытие страницы логина"""
    from data import BASE_URL
    from locators import Locators
    
    driver.get(BASE_URL)
    
    # Ожидаем, пока кнопка "Вход и регистрация" станет доступной и нажимаем
    login_button = wait.until(EC.element_to_be_clickable(Locators.LOGIN_REGISTER_BUTTON))
    login_button.click()

    return driver

@pytest.fixture
def open_home_page(driver, wait):
    """Открытие главной страницы"""
    from data import BASE_URL
    
    driver.get(BASE_URL)
    return driver, wait
