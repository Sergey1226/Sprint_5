import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators import Locators
from data import BASE_URL, EXISTING_EMAIL, USER_PASSWORD

@pytest.fixture
def open_registration_page(driver, wait):
    #Открытие страницы и нажатие кнопок для регистрации
    driver.get(BASE_URL)
    
    # Ожидаем, пока кнопка "Вход и регистрация" станет доступной
    login_button = wait.until(EC.element_to_be_clickable(Locators.LOGIN_REGISTER_BUTTON))
    login_button.click()

    # Ожидаем появления кнопки "Нет аккаунта"
    no_account_button = wait.until(EC.element_to_be_clickable(Locators.NO_ACCOUNT_BUTTON))
    no_account_button.click()
    
    return driver  

def test_registration_error_highlighting(driver, wait, open_registration_page):
    #Тест на отображение ошибок при вводе существующего email
    driver = open_registration_page  

    # Используем существующий email 
    existing_email = EXISTING_EMAIL

    # Заполнение формы регистрации
    email_input = wait.until(EC.visibility_of_element_located(Locators.EMAIL_INPUT))
    email_input.send_keys(existing_email)  # Вводим невалидный email
    
    password_input = wait.until(EC.visibility_of_element_located(Locators.PASSWORD_INPUT))
    password_input.send_keys(USER_PASSWORD)

    confirm_password_input = wait.until(EC.visibility_of_element_located(Locators.CONFIRM_PASSWORD_INPUT))
    confirm_password_input.send_keys(USER_PASSWORD)
    

    # Нажимаем кнопку "Создать аккаунт"
    create_account_button = wait.until(EC.element_to_be_clickable(Locators.CREATE_ACCOUNT_BUTTON))
    create_account_button.click()


    # Ожидаем появления сообщения об ошибке под полем Email
    email_error_message = wait.until(EC.visibility_of_element_located(Locators.EMAIL_ERROR_MESSAGE))
    assert "Ошибка" in email_error_message.text, "Сообщение об ошибке не содержит слово 'Ошибка'"
    # Проверяем, что на всех полях (Email, Пароль, Повторите пароль) появился класс ошибки (border red)
    error_field = wait.until(EC.visibility_of_element_located(Locators.ERROR_FIELD))
    assert "input_inputError" in error_field.get_attribute("class"), "Поле не содержит класс ошибки"
