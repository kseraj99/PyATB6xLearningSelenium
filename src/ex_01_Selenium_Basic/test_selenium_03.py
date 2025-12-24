from selenium import webdriver

import pytest
import allure

@allure.title("verify that we are able to open a page by using selenium")
@allure.description("We will open a page and verify that it is getting opened by using selenium")
def test_first_tc():
    driver = webdriver.Chrome()
    driver.get("https://thetestingacademy.com/")
    print(driver.title)
    print(driver.current_url)
    assert driver.title == "TheTestingAcademy | Learn Software Testing and Automation Testing"

    driver.quit()


