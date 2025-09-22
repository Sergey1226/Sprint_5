import pytest
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from data import EXISTING_EMAIL, USER_PASSWORD, EXPECTED_URL_LOGIN


class TestUserLoginLogout:
    
    def test_login_logout_user(self, driver, wait, open_login_page):
        
        # Заполнение формы авторизации данными пользователя
        email_input = wait.until(EC.visibility_of_element_located(Locators.EMAIL_INPUT))
        email_input.send_keys(EXISTING_EMAIL)  

        password_input = wait.until(EC.visibility_of_element_located(Locators.PASSWORD_INPUT))
        password_input.send_keys(USER_PASSWORD) 

        # Нажимаем кнопку "Войти"
        sign_in_button = wait.until(EC.element_to_be_clickable(Locators.SIGN_IN_BUTTON))
        sign_in_button.click()

        # Ожидаем, что произошел редирект на главную страницу
        wait.until(EC.url_to_be(EXPECTED_URL_LOGIN))

        # Ожидаем, пока кнопка "Выйти" станет доступной и нажимаем
        sign_out_button = wait.until(EC.element_to_be_clickable(Locators.SIGN_OUT_BUTTON))
        sign_out_button.click()

        # Проверка, что аватар и имя пользователя исчезли
        assert wait.until(EC.invisibility_of_element_located(Locators.USER_AVATAR_LOCATOR)), "Аватар не исчез!"
        assert wait.until(EC.invisibility_of_element_located(Locators.USER_NAME_EXACT_LOCATOR)), "Имя пользователя не исчезло!"
        
        # Проверка, что кнопка "Вход и регистрация" появилась после выхода
        login_register_button = wait.until(EC.visibility_of_element_located(Locators.LOGIN_REGISTER_BUTTON))
        assert login_register_button.is_displayed(), "Кнопка 'Вход и регистрация' не появилась после выхода"


    
    