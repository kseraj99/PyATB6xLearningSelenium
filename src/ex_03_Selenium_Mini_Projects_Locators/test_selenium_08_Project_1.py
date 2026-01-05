"""
Project 1 - Automating by using the Selenium Python.
1. Navigate to the URL - https://katalon-demo-cura.herokuapp.com/
2. Find the Make appointment Button
3. Click on the Make appointment Button
4. Next Page will be loaded
5. Find and Enter the details Username and Password and Click on the Login Button.
6. Verify current URL-https://katalon-demo-cura.herokuapp.com/#appointment

"""

import time
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By


def test_project_1_Katalon():
    Edge_options = Options()
    Edge_options.add_argument("--start-maximized")
    driver = webdriver.Edge(Edge_options)
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
    pass_box.send_keys("ThisIsNotAPassword")
    login_button = driver.find_element(By.ID,"btn-login")
    login_button.click()

    time.sleep(4)

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"

    driver.quit()