import pytest
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from data import BASE_URL, INVALID_EMAIL


class TestRegistrationErrors:
    
    def test_registration_error_highlighting(self, driver, wait, open_registration_page):
        
        # Используем невалидный email 
        invalid_email = INVALID_EMAIL
        
        # Заполнение формы регистрации
        email_input = wait.until(EC.visibility_of_element_located(Locators.EMAIL_INPUT))
        email_input.send_keys(invalid_email)
        
        create_account_button = wait.until(EC.element_to_be_clickable(Locators.CREATE_ACCOUNT_BUTTON))
        create_account_button.click()
        
        # Ожидаем появления сообщения об ошибке под полем Email
        email_error_message = wait.until(EC.visibility_of_element_located(Locators.EMAIL_ERROR_MESSAGE))
        assert "Ошибка" in email_error_message.text, "Сообщение об ошибке не содержит слово 'Ошибка'"
       
        # Проверяем, что на всех полях (Email, Пароль, Повторите пароль) появился класс ошибки (border red)
        error_field = wait.until(EC.visibility_of_element_located(Locators.ERROR_FIELD))
        assert "input_inputError" in error_field.get_attribute("class"), "Поля не содержат класс ошибки"
