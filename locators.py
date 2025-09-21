from selenium.webdriver.common.by import By

class Locators:
    #Основные элементы
    LOGIN_REGISTER_BUTTON = (By.XPATH, "//button[contains(text(), 'Вход и регистрация')]")
    NO_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(), 'Нет аккаунта')]")
    PLACE_AD_BUTTON = (By.XPATH, "//button[contains(text(), 'Разместить объявление')]") 
    SIGN_OUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выйти')]")
    
    #Форма регистрации и логина    
    EMAIL_INPUT = (By.XPATH, "//input[@placeholder='Введите Email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@placeholder='Пароль']")
    CONFIRM_PASSWORD_INPUT = (By.XPATH, "//input[@placeholder='Повторите пароль']")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(), 'Создать аккаунт')]")
    SIGN_IN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")
    
    #Элементы после авторизации
    USER_AVATAR_LOCATOR = (By.XPATH, "//div[contains(@class, 'flexRow')]/button[contains(@class, 'circleSmall')]")
    USER_NAME_EXACT_LOCATOR = (
        By.XPATH,
        "//div[contains(@class, 'columnSmall')]//h3[contains(@class, 'profileText') and contains(@class, 'name') and normalize-space(text())='User.']"
    )
    
    #Ошибки
    EMAIL_ERROR_MESSAGE = (By.XPATH, "//form//div[2]/div[1]/span[text()='Ошибка']")
    ERROR_FIELD = (By.XPATH, "//div[contains(@class, 'input_inputError')]")
    GENERIC_ERROR = (By.XPATH, "//span[contains(text(), 'Ошибка')]")
    
    #Модальные окна
    AUTH_POPUP = (By.CSS_SELECTOR, "form.popUp_shell__LuyqR")
    AUTH_POPUP_NAME = (By.XPATH, "//h1[contains(text(), 'Чтобы разместить объявление, авторизуйтесь')]")
    #Форма создания объявления
    AD_TITLE_INPUT = (By.XPATH, "//input[@placeholder='Название']")
    DESCRIPTION_INPUT = (By.XPATH, "//textarea[@name='description']")    #Описание товара             
    PRICE_INPUT = (By.XPATH, "//input[@placeholder='Стоимость']") #стоимоcть
    
    # Dropdowns
    CITY_DROPDOWN = (By.XPATH, "//input[@name='city']/following-sibling::button") #дропдаун по городу
    CITY_DROPDOWN_MENU = (By.XPATH, "//div[contains(@class, 'dropDownMenu_options__CmHmm')]") #меню дропдауна по городу
    CATEGORY_DROPDOWN = (By.XPATH, "//input[@name='category']/following-sibling::button") #дропдаун по категории
    CATEGORY_DROPDOWN_MENU = (By.XPATH, "//div[contains(@class, 'dropDownMenu_options__CmHmm')]") #меню дропдауна по категории
    
    #Конкретные опции
    CITY_OPTION_SPB = (By.XPATH, "//button[.//span[text()='Санкт-Петербург']]") #выбор города из списка
    CATEGORY_OPTION_HOBBY = (By.XPATH, "//button[.//span[text()='Книги']]") #выбор категории из списка
    
    # Radio buttons
    RADIO_NEW = (By.XPATH, "//input[@type='radio' and @value='Новый']") #радибаттон состояние товара
    RADIO_USED = (By.XPATH, "//div[contains(@class, 'radioUnput_inputRegular__FbVbr')]") #радибаттон состояние товара
    
    #Кнопки
    PUBLISH_BUTTON = (By.XPATH, "//button[contains(text(), 'Опубликовать')]") # опубликовать
    
    #Карточки объявлений
    AD_CARDS = (By.XPATH, "//div[contains(@class, 'card')]") # поиск карточки
