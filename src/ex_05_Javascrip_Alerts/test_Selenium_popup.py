import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


def test_javascript_prompt():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.makemytrip.com/")
    driver.maximize_window()

    wait = WebDriverWait(driver, 10)

    time.sleep(5)

    close_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//span[@data-cy='closeModal']"))
    )
    close_btn.click()

    time.sleep(2)
    driver.quit()
