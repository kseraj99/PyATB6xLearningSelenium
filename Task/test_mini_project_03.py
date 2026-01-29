"""
Navigate
https://katalon-demo-cura.herokuapp.com/
Make appointment
Verify also.
"""

import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.title("Appointment Booking")
@allure.description("Verify, I am able to book an appointment")
def test_verify_appointment_booking():
    driver = webdriver.Edge()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()
    driver.implicitly_wait(4)

    appointment_button = driver.find_element(By.ID, "btn-make-appointment")
    appointment_button.click()
    user_id = driver.find_element(By.ID, "txt-username")
    user_id.send_keys("John Doe")
    pass_word = driver.find_element(By.ID,"txt-password")
    pass_word.send_keys("ThisIsNotAPassword")
    loging_button = driver.find_element(By.ID, "btn-login")
    loging_button.click()
    apply = driver.find_element(By.ID, "chk_hospotal_readmission")
    apply.click()
    program = driver.find_element(By.ID, "radio_program_none")
    program.click()
    visit_date = driver.find_element(By.ID, "txt_visit_date")
    visit_date.send_keys("29/01/2026")
    text_comment = driver.find_element(By.ID,"txt_comment")
    text_comment.send_keys("I want to book an appointment")
    cnf_booking = driver.find_element(By.ID, "btn-book-appointment")
    cnf_booking.click()
    booking_cnf = driver.find_element(By.XPATH,"//div[@class='col-xs-12 text-center']/h2").text
    assert "Appointment Confirmation" == booking_cnf


    time.sleep(2)
    driver.quit()


