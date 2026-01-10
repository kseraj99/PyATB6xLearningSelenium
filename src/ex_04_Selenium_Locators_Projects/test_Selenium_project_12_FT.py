import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


@allure.title("Positive Testcase")
@allure.description("Verify that the free trail button is clickable")

def test_vwo_free_trail_button():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    driver.find_element(By.XPATH, "//a[@class='text-link Td(n) Whs(nw)']").click()
    assert driver.current_url == "https://vwo.com/free-trial/?utm_medium=website&utm_source=login-page&utm_campaign=mof_eg_loginpage"
    time.sleep(2)
    driver.quit()