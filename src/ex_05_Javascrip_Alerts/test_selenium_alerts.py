
import allure
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


@allure.title("JavaScript alerts")
@allure.description("To verify, that we are able to click on javascript")
def test_javaScript_alerts():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    js_popup = driver.find_element(By.XPATH, "//button[@onclick='jsAlert()']")
    js_popup.click()
    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver._switch_to.alert
    alert.accept()
    result = driver.find_element(By.ID,"result").text

    assert result == "You successfully clicked an alert"

    time.sleep(2)
    driver.quit()

def test_alerts_confirm_accept():
    driver = webdriver.Edge()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    confirm = driver.find_element(By.XPATH, "//button[@onclick='jsConfirm()']")
    confirm.click()
    time.sleep(2)

    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver._switch_to.alert
    alert.accept()

    results= driver.find_element(By.ID, "result").text

    assert results == "You clicked: Ok"

    driver.quit()

def test_alerts_confirm_dismiss():
    driver = webdriver.Edge()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    confirm = driver.find_element(By.XPATH, "//button[@onclick='jsConfirm()']")
    confirm.click()
    time.sleep(2)

    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver._switch_to.alert
    alert.dismiss()

    results= driver.find_element(By.ID, "result").text

    assert results == "You clicked: Cancel"

    driver.quit()

def test_alerts_js_prompt_accept():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    confirm = driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']")
    confirm.click()
    time.sleep(2)

    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver._switch_to.alert
    alert.send_keys("Seraj Khan")
    alert.accept()

    results = driver.find_element(By.ID, "result").text

    assert results == "You entered: Seraj Khan"

    driver.quit()

