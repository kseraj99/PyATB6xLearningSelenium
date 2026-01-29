import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.title("JS")
@allure.description("Verify JS")
def test_js():

    # Launch Edge browser
    driver = webdriver.Edge()

    # Maximize the browser window
    driver.maximize_window()

    # Open the test web page
    driver.get("https://selectorshub.com/xpath-practice-page/")

    # Locate the Shadow DOM host element by ID
    user_view = driver.find_element(By.ID, "userName")

    # Scroll the page until the Shadow DOM element is visible
    driver.execute_script("arguments[0].scrollIntoView(true);", user_view)

    # Use JavaScript to access Shadow DOM and fetch the username input field
    user_name = driver.execute_script(
        "return document.querySelector('div#userName')"
        ".shadowRoot.querySelector('#kils')"
    )

    # Enter text into the username field inside Shadow DOM
    user_name.send_keys("seraj Khan")

    # Access nested Shadow DOM to locate the pizza input field
    my_pizza = driver.execute_script(
        "return document.querySelector('div#userName')"
        ".shadowRoot.querySelector('div#app2')"
        ".shadowRoot.querySelector('#pizza')"
    )

    # Enter text into the pizza field
    my_pizza.send_keys("cheez Pizza")

    # Pause execution for 2 seconds to observe the result
    time.sleep(2)

    # Close the browser and end the session
    driver.quit()
