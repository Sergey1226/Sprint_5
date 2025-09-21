import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators import Locators  
from data import BASE_URL

@pytest.fixture
def open_home_page(driver, wait):

    driver.get(BASE_URL)
    return driver, wait
def test_create_ad_as_unauthorized_user(driver, wait, open_home_page):

    # Получаем доступ к драйверу и ожиданию
    driver, wait = open_home_page

    # Нажимаем кнопку "Разместить объявление"
    place_ad_button = wait.until(EC.element_to_be_clickable(Locators.PLACE_AD_BUTTON))
    place_ad_button.click()

    # Ожидаем появления модального окна
    auth_pop = wait.until(EC.visibility_of_element_located(Locators.AUTH_POPUP))
        
    # Проверяем, что заголовок модального окна соответствует ожидаемому
    modal_title = auth_pop.find_element(*Locators.AUTH_POPUP_NAME)
    assert modal_title.text == "Чтобы разместить объявление, авторизуйтесь", \
     f"Ожидался заголовок 'Чтобы разместить объявление, авторизуйтесь', но был '{modal_title.text}'"
