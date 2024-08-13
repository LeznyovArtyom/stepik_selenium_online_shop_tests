from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

def test_page_has_basket_button(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    # time.sleep(30)
    browser.implicitly_wait(5)

    # Проверка наличия кнопки добавления в корзину
    try:
        basket_button = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
    except NoSuchElementException:
        assert False, "basket button not found"