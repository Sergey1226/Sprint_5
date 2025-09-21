import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators import Locators
from data import BASE_URL, EXISTING_EMAIL, USER_PASSWORD, EXPECTED_URL_LOGIN

@pytest.fixture
def open_login_page(driver, wait):

    driver.get(BASE_URL)

    # Ожидаем, пока кнопка "Вход и регистрация" станет доступной и нажимаем
    login_button = wait.until(EC.element_to_be_clickable(Locators.LOGIN_REGISTER_BUTTON))
    login_button.click()

    return driver

def test_login_user(driver, wait, open_login_page):

    driver = open_login_page  

    # Заполнение формы авторизации данными пользователя
    email_input = wait.until(EC.visibility_of_element_located(Locators.EMAIL_INPUT))
    email_input.send_keys(EXISTING_EMAIL)  # Вводим email

    password_input = wait.until(EC.visibility_of_element_located(Locators.PASSWORD_INPUT))
    password_input.send_keys(USER_PASSWORD)  # Вводим пароль

    # Нажимаем кнопку "Войти"
    sign_in_button = wait.until(EC.element_to_be_clickable(Locators.SIGN_IN_BUTTON))
    sign_in_button.click()

    # Ожидаем, что произошел редирект на главную страницу
    wait.until(EC.url_to_be(EXPECTED_URL_LOGIN))

    # Проверка отображения аватара и имени пользователя на главной странице
    user_avatar = wait.until(EC.visibility_of_element_located(Locators.USER_AVATAR_LOCATOR))
    user_name = wait.until(EC.visibility_of_element_located(Locators.USER_NAME_EXACT_LOCATOR))

    # Проверка правильного расположения элементов: аватар и имя должны быть слева от кнопки "Разместить объявление"
    assert_elements_position(driver, user_avatar, user_name)

def assert_elements_position(driver, user_avatar, user_name):
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
