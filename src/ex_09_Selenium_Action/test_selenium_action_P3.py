import time
import allure
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton

@allure.title("Action P3")
@allure.description("Verify Click and Hold")
def test_verify_click_and_hold():

    # Launch the Chrome browser
    driver = webdriver.Chrome()

    # Open the test web page
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")

    # Find the draggable element on the page using its ID
    target = driver.find_element(By.ID, "draggable")

    # Pause for 2 seconds so the user can see the element before action starts
    time.sleep(2)

    # Create an ActionChains object to perform advanced mouse actions
    action = ActionChains(driver)

    # Perform click and hold operation on the target element
    # This simulates pressing the mouse button down and holding it
    action.click_and_hold(on_element=target)

    # Execute the action sequence
    action.perform()

    # Wait for 4 seconds to visually confirm the click-and-hold action
    time.sleep(10)

    # Close the browser and end the test
    driver.quit()
