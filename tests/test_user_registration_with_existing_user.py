import pytest
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from data import EXISTING_EMAIL, USER_PASSWORD


class TestExistingEmailRegistration:
    
    def test_registration_with_existing_email(self, driver, wait, open_registration_page):
        
        # Используем существующий email 
        existing_email = EXISTING_EMAIL

        # Заполнение формы регистрации
        email_input = wait.until(EC.visibility_of_element_located(Locators.EMAIL_INPUT))
        email_input.send_keys(existing_email)  
        
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
