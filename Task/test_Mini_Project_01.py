"""
Locators-Find the Web elements

Open the URL https://app.vwo.com/#/login

Find the Email id and enter the email as admin@admin.com

Find the Pass input box  and enter password as admin.

Find and Click on the submit button

Verify that the error message is shown
 "Your email, password, IP address or location did not match"_
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def test_mini_project_1():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--headless=new")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://app.vwo.com/#/login")
    user_input = driver.find_element(By.ID, "login-username")
    user_input.send_keys("admin@admin.com")
    user_pass = driver.find_element(By.ID,"login-password")
    user_pass.send_keys("admin")
    login_button = driver.find_element(By.ID, "js-login-btn")
    login_button.click()
    time.sleep(2)
    error_msg = driver.find_element(By.ID, "js-notification-box-msg").text
    assert "Your email, password, IP address or location did not match" == error_msg

    time.sleep(2)

    driver.quit()
