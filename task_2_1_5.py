from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/math.html"
    
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.implicitly_wait(5)
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    field = browser.find_element(By.ID, "answer")
    field.send_keys(y)

    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    checkbox.click()
    r_button = browser.find_element(By.ID, "robotsRule")
    r_button.click()
    submit_button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    submit_button.click()
    print(browser.switch_to.alert.text)
    
finally:
    time.sleep(5)
    browser.quit()