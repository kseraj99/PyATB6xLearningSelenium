import allure
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

@allure.title("Select")
@allure.description("Verify Select")
def test_select_dropdown():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/dropdown")

    select_tag = driver.find_element(By.ID, "dropdown")
    select = Select(select_tag)
    select.select_by_visible_text("Option 2")

    time.sleep(2)
    driver.quit()