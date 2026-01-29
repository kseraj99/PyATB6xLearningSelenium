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
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


@allure.title("Action Keyword")
@allure.description("Verify Action Keywords")
def test_verify_action_keyword():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")

    first_name = driver.find_element(By.XPATH, "//input[@name='firstname']")

    action = ActionChains(driver)
    (action
     .key_down(Keys.SHIFT)
     .send_keys_to_element(first_name, "Seraj Khan")
     .key_up(Keys.SHIFT).perform())

    time.sleep(4)
    driver.quit()
