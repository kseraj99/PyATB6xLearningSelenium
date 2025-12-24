from selenium import webdriver

import allure

@allure.title("Print the page source of the page")
def test_selenium():
    driver = webdriver.Edge()
    driver.get("https://thetestingacademy.com")
    print(driver.page_source)

    driver.quit()


