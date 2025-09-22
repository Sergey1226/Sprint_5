import pytest
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from data import EXISTING_EMAIL, USER_PASSWORD, EXPECTED_URL_LOGIN


class TestUserLogin:
    
    def test_login_user(self, driver, wait, open_login_page):
        
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

        # Проверка отображения аватара и имени пользователя на главной странице
        user_avatar = wait.until(EC.visibility_of_element_located(Locators.USER_AVATAR_LOCATOR))
        user_name = wait.until(EC.visibility_of_element_located(Locators.USER_NAME_EXACT_LOCATOR))

        # Проверка правильного расположения элементов
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

        # Проверяем, что элементы отображаются на странице
        assert user_avatar.is_displayed(), "Аватар пользователя не отображается"
        assert user_name.is_displayed(), "Имя пользователя не отображается"
