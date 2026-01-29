import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_verify_iframe_selection():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.implicitly_wait(4)
    driver.get("https://the-internet.herokuapp.com/frames")
    link_text = driver.find_element(By.LINK_TEXT, "iFrame")
    link_text.click()
    cross_button = driver.find_element(By.XPATH, "//div[@class='tox-icon']")
    cross_button.click()
    driver.switch_to.frame("mce_0_ifr")

    inbox_text = driver.find_element(By.XPATH, "//body[@id='tinymce']/p").text
    print(inbox_text)
    assert "Your content goes here." == inbox_text

    time.sleep(2)
    driver.quit()