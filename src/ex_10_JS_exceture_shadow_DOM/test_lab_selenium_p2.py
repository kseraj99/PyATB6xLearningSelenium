import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.title("JS")
@allure.description("Verify JS")
def test_js():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://selectorshub.com/xpath-practice-page/")
    driver.execute_script("window.scrollBy(0,500);")

    time.sleep(2)
    driver.quit()