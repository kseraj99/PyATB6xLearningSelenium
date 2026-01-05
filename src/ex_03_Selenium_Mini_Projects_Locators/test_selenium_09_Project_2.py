"""
Project 2 - Automating by using the Selenium Python.
1. Navigate to the URL - https://katalon-demo-cura.herokuapp.com/
2. Find the Make appointment Button
3. Click on the Make appointment Button
4. Next Page will be loaded
5. Find and Enter wrong Username and Password and Click on the Login Button.
6. Verify the Login failed message.

"""

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def test_project_1_Katalon_negative():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    """
    <a ...Opening tag
    id="btn-make-appointment" 
    href="./profile.php#login" 
    class="btn btn-dark btn-lg">
    Make Appointment
    </a>...closing tag
    """
    make_appointment = driver.find_element(By.ID, "btn-make-appointment")
    make_appointment.click()
    user_box = driver.find_element(By.ID, "txt-username")
    user_box.send_keys("John Doe")
    pass_box = driver.find_element(By.ID, "txt-password")
    pass_box.send_keys("ThisIsNotAPassword1222")
    login_button = driver.find_element(By.ID,"btn-login")
    login_button.click()
    time.sleep(2)
    login_error = driver.find_element(By.XPATH, "//p[@class='lead text-danger']").text
    assert login_error == "Login failed! Please ensure the username and password are valid."

    time.sleep(3)

    driver.quit()