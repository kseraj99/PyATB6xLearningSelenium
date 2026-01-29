"""
Javascript Executor
JavaScriptExecutor is an interface in Selenium WebDriver that
allows direct execution of JavaScript code within the browser context.
#### Key Features
- Enables execution of **JavaScript code** in the current window or frame.
- Provides two main methods: `driver.execute_script("alert(1)")`
- Useful for **handling dynamic web content** and **complex interaction.**


3 Major usages -

1. Click on element which are hidden. dynamically
2. Scrolling
3. Enter the text input(which are not visible properly).

- arguments[0].click():
This function clicks on the element specified as the first argument.
- arguments[0].scrollIntoView():
This function scrolls the element specified as the first argument into view.
- arguments[0].setAttribute(arguments[1], arguments[2]):
This function sets the attribute specified by the second argument to the value specified
by the third argument for the element specified as the first argument.
- arguments[0].innerHTML = arguments[1]:
This function sets the inner HTML of the element specified as the first argument to the value specified by the second argument.
- return arguments[0].value:
This function returns the value of the element specified as the first argument.
- return arguments[0].style.display:
This function returns the display style of the element specified as the first argument.

"""


import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.title("JS")
@allure.description("Verify JS")
def test_js():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://app.vwo.com/#/login")
    driver.execute_script("alert(1)")





    time.sleep(2)
    driver.quit()