
import time
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By


def test_project_1_Katalon_Positive():
    edge_options = Options()
    edge_options.add_argument("--start-maximized")
    edge_options.add_argument("--headless=new")
    driver = webdriver.Edge(edge_options)
    driver.get("https://katalon-demo-cura.herokuapp.com/")


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


def test_project_1_Katalon_Negative():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--headless=new")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://katalon-demo-cura.herokuapp.com/")


    make_appointment = driver.find_element(By.ID, "btn-make-appointment")
    make_appointment.click()
    user_box = driver.find_element(By.ID, "txt-username")
    user_box.send_keys("John Doe")
    pass_box = driver.find_element(By.ID, "txt-password")
    pass_box.send_keys("Wrong@123")
    login_button = driver.find_element(By.ID,"btn-login")
    login_button.click()
    time.sleep(2)
    login_error = driver.find_element(By.XPATH, "//p[@class='lead text-danger']").text
    assert login_error == "Login failed! Please ensure the username and password are valid."

    time.sleep(3)

    driver.quit()