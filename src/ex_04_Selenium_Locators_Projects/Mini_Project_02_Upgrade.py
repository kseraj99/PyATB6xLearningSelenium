"""
Project-2
Navigate to this URL- augtest_040823@idrive.com
find the userid field and password field
Enter the username and password
click on login button
Verify the Upgrade now! button

"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def test_mini_project_2():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://www.idrive360.com/enterprise/login")
    time.sleep(4)
    email_box = driver.find_element(By.ID,"username")
    email_box.send_keys("augtest_040823@idrive.com")
    pass_box = driver.find_element(By.ID,"password")
    pass_box.send_keys("123456")
    login_button = driver.find_element(By.ID, "frm-btn")
    login_button.click()
    time.sleep(12)
    upgrade_msg = driver.find_element(By.XPATH, "//button[@class='id-btn id-warning-btn-drk id-tkn-btn']").text
    assert "Upgrade Now!" == upgrade_msg

    driver.quit()


  

