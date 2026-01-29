"""
Actions class is an ability provided by Selenium for handling keyboard and mouse events.
- Keyboard Events
- Mouse Events
- Wheel Mouse

from selenium.webdriver.common.action_chains import **ActionChains**

actions = ActionChains(driver)
Methods of Action Class

Action class is useful mainly for mouse and keyboard actions. In order to perform such actions, Selenium provides various methods.

Mouse Actions in Selenium:

1. Perform Mouse Hover Action on the Web Element
2. moveToElement(live).build().perform();
3. doubleClick(): Performs double click on the element
4. clickAndHold(): Performs long click on the mouse without releasing it
5. dragAndDrop(): Drags the element from one point and drops to another
6. moveToElement(): Shifts the mouse pointer to the center of the element
7. contextClick(): Performs right-click on the mouse Keyboard Actions in Selenium
8. sendKeys(): Sends a series of keys to the element
9. keyUp(): Performs key release
10. keyDown(): Performs keypress without release.

"""
import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton


@allure.title("Action P2")
@allure.description("Verify Action Mouse")
def test_verify_action_mouse():

    # Launch Chrome browser
    driver = webdriver.Chrome()

    # Open the test page
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")

    # Locate the element which needs to be clicked
    target = driver.find_element(By.ID, "click")

    # Create ActionBuilder object
    actions = ActionBuilder(driver)

    # Move mouse to the element
    actions.pointer_action.move_to(target)

    # Press left mouse button
    actions.pointer_action.pointer_down(MouseButton.LEFT)

    # Release left mouse button (this completes the click)
    actions.pointer_action.pointer_up(MouseButton.LEFT)

    # Execute the actions
    actions.perform()

    # Wait so we can visually verify the action
    time.sleep(4)

    # Close the browser
    driver.quit()
