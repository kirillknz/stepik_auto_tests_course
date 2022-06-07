from selenium.webdriver.common.by import By
import time



def test_btn_add_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    #time.sleep(30)
    assert browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
