import pytest
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


class TestUnauthorizedAdCreation:
    
    def test_create_ad_as_unauthorized_user(self, driver, wait, open_home_page):
        
        # Нажимаем кнопку "Разместить объявление"
        place_ad_button = wait.until(EC.element_to_be_clickable(Locators.PLACE_AD_BUTTON))
        place_ad_button.click()

        # Ожидаем появления модального окна
        auth_pop = wait.until(EC.visibility_of_element_located(Locators.AUTH_POPUP))
            
        # Проверяем, что заголовок модального окна соответствует ожидаемому
        modal_title = auth_pop.find_element(*Locators.AUTH_POPUP_NAME)
        assert modal_title.text == "Чтобы разместить объявление, авторизуйтесь", \
         f"Ожидался заголовок 'Чтобы разместить объявление, авторизуйтесь', но был '{modal_title.text}'"
