from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FORM = (By.CLASS_NAME, 'Auth_login__3hAey')
    EMAIL_FIELD = (By.NAME, 'name')
    PASSWORD_FIELD = (By.NAME, 'Пароль')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button.button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_medium__3zxIa")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, '.Auth_link__1fOlj[href="/register"]')
    VALIDATION_MESSAGE = (By.CSS_SELECTOR, '.input__error.text_type_main-default')

class MainPageLocators:
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_large__G21Vg")
    MAKE_ORDER_BUTTON = (By.CSS_SELECTOR, '.button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_large__G21Vg')
    CONSTRUCTOR_BUNS_TAB = (By.XPATH, "//h2[text()='Булки']")
    CONSTRUCTOR_SAUCE_TAB = (By.XPATH, "//h2[text()='Соусы']")
    CONSTRUCTOR_FILLING_TAB = (By.XPATH, "//h2[text()='Начинки']")
    CONSTRUCTOR_BUNS_TAB_TITLE = (By.XPATH, "//span[text()='Булки']")
    CONSTRUCTOR_SAUCE_TAB_TITLE = (By.XPATH, "//span[text()='Соусы']")
    CONSTRUCTOR_FILLING_TAB_TITLE = (By.XPATH, "//span[text()='Начинки']")

class ProfilePageLocators:
    LOGOUT_BUTTON = (By.CSS_SELECTOR, '.Account_button__14Yp3')
    PROFILE_TABS = (By.CLASS_NAME, 'Account_list__3KQQf')

class RegisterPageLocators:
    NAME_FIELD = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    EMAIL_FIELD = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_FIELD = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button.button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_medium__3zxIa")
    VALIDATION_MESSAGE = (By.CSS_SELECTOR, '.input__error.text_type_main-default')

class ForgotPasswordPage:
    LOGIN_BUTTON = (By.XPATH, "//a[@href='/login']")

class NavigationBar:
    PROFILE_BUTTON = (By.XPATH, "//a[@href='/account']")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//a[@href='/']")