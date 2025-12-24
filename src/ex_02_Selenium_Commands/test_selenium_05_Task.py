import time

from selenium import webdriver
import allure
from selenium.webdriver.common.by import By


@allure.title("Print the title of the page")
def test_selenium():
    driver = webdriver.Edge()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    title = driver.find_element(By.XPATH,"//div[@class='text-vertical-center']/h1").text
    print(title)
    assert "CURA Healthcare Service" in title
    time.sleep(2)
    driver.quit()


