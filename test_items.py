from selenium.webdriver.common.by import By
import time


def test_visible_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    time.sleep(5)
    assert button, "Кнопка отсутствует"