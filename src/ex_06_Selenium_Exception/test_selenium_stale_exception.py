"""
 StaleElementException basically comes whenever page is refreshed,
 DOM structure changes. This generally happens in modern applications or
 modern JavaScript frameworks like React 
"""

import allure
import time
from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.title("stale exception")
@allure.description("stale exception")
def test_stale_element_exception():
    driver = webdriver.Chrome()
    driver.get("https://google.com")
    try:
        text_box = driver.find_element(By.ID, "APjFqb")
        driver.refresh()
        text_box.send_keys("Seraj Khan")
    except StaleElementReferenceException as see:
        print(see.msg)
    time.sleep(2)
    driver.quit()