import sys
from helpers import base
from helpers import locators
sys.path.append("..")


username = base.config_reader('login', 'username')
password = base.config_reader('login', 'password')


def login(page):
    page.locator(locators.USER_NAME_XPATH).fill(username)
    page.click(locators.CONTINUE_BUTTON_XPATH)
    page.locator(locators.PASSWORD_XPATH).fill(password)
    page.click(locators.SUBMIT_BUTTON_XPATH)