from selenium import webdriver
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link = "https://russiasmartcity.ru/"

try:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.maximize_window()
    browser.implicitly_wait(5)
    browser.get(link)
    
    def test_public():
        
        news_button = browser.find_element(By.LINK_TEXT, 
        'Новости')
        news_button.click()
        
        publications = browser.find_element(By.LINK_TEXT,
        'Публикации')
        publications.click()
        
        time.sleep(5)
        
        topic_1 = browser.find_element(By.XPATH,
        '(//span[contains(@class, "s-form-checkbox__mark")])[1]')
        
        time.sleep(5)
        topic_1.click()
        
        
        
        time.sleep(5)
        
    test_public()
   
finally:
    time.sleep(5)
    # close browser
    browser.quit()

# empty string


