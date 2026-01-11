import allure
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.title("SVG")
@allure.description("SVG Verification")
def test_svg_part1():
    driver = webdriver.Chrome()
    driver.get("https://www.flipkart.com")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("macmini")
    time.sleep(2)
    list_of_svg_elmt = driver.find_elements(By.XPATH,"//*[name()='svg']")
    list_of_svg_elmt[0].click()


    time.sleep(2)
    driver.quit()