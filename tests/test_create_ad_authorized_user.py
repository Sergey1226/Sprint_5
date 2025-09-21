import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from locators import Locators
from data import BASE_URL, EXISTING_EMAIL, USER_PASSWORD, EXPECTED_URL_LOGIN
import time

@pytest.fixture
def open_login_page(driver, wait):

    driver.get(BASE_URL)

    #Ожидаем кнопку 'Вход и регистрация'
    login_button = wait.until(EC.element_to_be_clickable(Locators.LOGIN_REGISTER_BUTTON))

    login_button.click()

    return driver


def test_create_ad_authorized_user(driver, wait, open_login_page):

    driver = open_login_page

    # Вводим email для авторизации
    email_input = wait.until(EC.element_to_be_clickable(Locators.EMAIL_INPUT))
    email_input.send_keys(EXISTING_EMAIL)

    # Вводим пароль для авторизации
    password_input = wait.until(EC.element_to_be_clickable(Locators.PASSWORD_INPUT))
    password_input.send_keys(USER_PASSWORD)

    sign_in_button = wait.until(EC.element_to_be_clickable(Locators.SIGN_IN_BUTTON))
    sign_in_button.click()

    wait.until(EC.url_to_be(EXPECTED_URL_LOGIN))
 
    # Ждем полной загрузки страницы после редиректа
    wait.until(EC.presence_of_element_located(Locators.PLACE_AD_BUTTON))
    time.sleep(1)

    # Переходим к кнопке "Разместить объявление"
    place_ad_button = wait.until(EC.element_to_be_clickable(Locators.PLACE_AD_BUTTON))
    place_ad_button.click()

    # Ждем загрузки формы создания объявления
    wait.until(EC.presence_of_element_located(Locators.AD_TITLE_INPUT))
    
    ad_title = "Продаю велосипед"
    
def find_element_retry(locator, wait, timeout=10):
    try:
        
        return wait.until(EC.element_to_be_clickable(locator))
    except StaleElementReferenceException:
        
        raise StaleElementReferenceException(f"Элемент {locator} стал устаревшим")
    except TimeoutException:
       
        raise TimeoutException(f"Не удалось найти элемент {locator} в течение {timeout} секунд")
    
    # Вводим заголовок объявления
    ad_title_input = find_element_retry(Locators.AD_TITLE_INPUT, wait)
    ad_title_input.send_keys(ad_title)

    # Вводим описание объявления
    description_input = find_element_retry(Locators.DESCRIPTION_INPUT, wait)
    description_input.send_keys("Велосипед в хорошем состоянии, почти не использовался.")

    # Вводим цену
    price_input = find_element_retry(Locators.PRICE_INPUT, wait)
    price_input.send_keys("100")
    
    category_dropdown = wait.until(EC.element_to_be_clickable(Locators.CATEGORY_DROPDOWN))
    category_dropdown.click()

    # Ждем появления меню и кликаем на нужную категорию
    category_option = wait.until(EC.element_to_be_clickable(Locators.CATEGORY_OPTION_HOBBY))
    category_option.click()
    
    #  Используем CITY_DROPDOWN 
    city_dropdown = wait.until(EC.element_to_be_clickable(Locators.CITY_DROPDOWN))
    city_dropdown.click()

    # Ждем появления меню и кликаем на нужный город
    city_option = wait.until(EC.element_to_be_clickable(Locators.CITY_OPTION_SPB))
    city_option.click()
  
    radio_used = find_element_retry(Locators.RADIO_USED)
    radio_used.click()

    publish_button = find_element_retry(Locators.PUBLISH_BUTTON)
    publish_button.click()
    

    # Ждем завершения публикации
    user_avatar = find_element_retry(Locators.USER_AVATAR_LOCATOR)
    user_avatar.click()

    # Ждем загрузки профиля
    wait.until(EC.presence_of_element_located(Locators.AD_CARDS))

    ad_cards = wait.until(EC.presence_of_all_elements_located(Locators.AD_CARDS))

    # Проверяем, что объявление совпадает
    assert (ad_title in card.text for card in ad_cards), f"Объявление '{ad_title}' не найдено!"
      