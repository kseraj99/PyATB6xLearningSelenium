import allure
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException


@allure.title("Exception Handle")
@allure.description("Verify exception handle")
def test_exception_handle():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    try:
        element = driver.find_element(By.ID, "This id is not available")
    except NoSuchElementException as nse:
        print(nse.msg)

    driver.quit()

