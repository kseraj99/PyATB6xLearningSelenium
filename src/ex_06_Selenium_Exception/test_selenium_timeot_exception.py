import time
import allure
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.title("timeout exception")
@allure.description("timeout exception")
def test_timeout_exception():
    driver = webdriver.Chrome()
    driver.get("https://google.com")
    try:
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@button='name']")))
    except TimeoutException as see:
        print(see)
        print("timeout exception occured! 10 second passed")
    finally:
            driver.quit()