import pytest
from data import EXPECTED_URL, USER_PASSWORD
from locators import Locators
from selenium.webdriver.support import expected_conditions as EC


class TestUserRegistration:
        
    def test_user_registration(self, driver, wait, generate_unique_email, open_registration_page):

        # Генерация уникального email
        unique_email = generate_unique_email
            
        # Заполнение формы регистрации
        email_input = wait.until(EC.visibility_of_element_located(Locators.EMAIL_INPUT))
        email_input.send_keys(unique_email)

        password_input = wait.until(EC.visibility_of_element_located(Locators.PASSWORD_INPUT))
        password_input.send_keys(USER_PASSWORD)

        confirm_password_input = wait.until(EC.visibility_of_element_located(Locators.CONFIRM_PASSWORD_INPUT))
        confirm_password_input.send_keys(USER_PASSWORD)

        # Ожидаем, пока кнопка "Создать аккаунт" станет кликабельной
        create_account_button = wait.until(EC.element_to_be_clickable(Locators.CREATE_ACCOUNT_BUTTON))
        create_account_button.click()

        # Ожидаем переход на главную страницу
        wait.until(EC.url_to_be(EXPECTED_URL))

        # Проверка отображения аватара и имени
        user_avatar = wait.until(EC.visibility_of_element_located(Locators.USER_AVATAR_LOCATOR))
        user_name = wait.until(EC.visibility_of_element_located(Locators.USER_NAME_EXACT_LOCATOR))

        # Проверка расположения аватара и имени
        self._assert_elements_position(driver, user_avatar, user_name)

    def _assert_elements_position(self, driver, user_avatar, user_name):
    
        avatar_location = user_avatar.location
        name_location = user_name.location
        post_ad_button = driver.find_element(*Locators.PLACE_AD_BUTTON)
        post_ad_button_location = post_ad_button.location

        # Проверяем, что аватар и имя расположены слева от кнопки "Разместить объявление"
        assert avatar_location['x'] < post_ad_button_location['x'], \
            "Аватар должен быть слева от кнопки 'Разместить объявление'"
        assert name_location['x'] < post_ad_button_location['x'], \
            "Имя пользователя должно быть слева от кнопки 'Разместить объявление'"

        # Проверяем, что элементы отображаются
        assert user_avatar.is_displayed(), "Аватар пользователя не отображается"
        assert user_name.is_displayed(), "Имя пользователя не отображается"
