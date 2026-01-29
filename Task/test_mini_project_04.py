import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.title("Payment Module")
@allure.description("Verify, we are able to do the payment or not")
def test_payment_module():
    driver = webdriver.Edge()
    driver.implicitly_wait(4)
    driver.maximize_window()
    driver.get("https://selectorshub.com/xpath-practice-page/?")
    payment_option = driver.find_element(By.XPATH,"//form[@id='paymentForm']")
    driver.execute_script("arguments[0].scrollIntoView(true);", payment_option)
    card_holder = driver.find_element(By.ID,"cardName")
    card_holder.send_keys("Seraj Khan")
    card_number = driver.find_element(By.ID,"cardNumber")
    card_number.send_keys("1234234534561234")
    expiry_date = driver.find_element(By.ID,"expiry")
    expiry_date.send_keys("0212")
    cvv = driver.find_element(By.ID,"cvv")
    cvv.send_keys("123")
    pay_now = driver.find_element(By.XPATH,"//button[@type='submit']")
    pay_now.click()


    time.sleep(4)
    driver.quit()