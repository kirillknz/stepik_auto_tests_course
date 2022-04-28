from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.execute_script("window.scrollBy(0, 100);")
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button = browser.find_element_by_id("book")
    button.click()

    value = browser.find_element_by_xpath("//span[@id='input_value']")
    x1 = value.text
    x = str(x1)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    y = calc(x)


    input1 = browser.find_element_by_xpath("//input[@id='answer']")
    input1.send_keys(y)

    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

