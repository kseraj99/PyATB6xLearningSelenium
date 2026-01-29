import allure
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_verify_window2():

    # Launch Edge browser
    driver = webdriver.Edge()

    # Maximize browser window
    driver.maximize_window()

    # Apply implicit wait of 4 seconds
    driver.implicitly_wait(4)

    # Open the test URL
    driver.get("https://the-internet.herokuapp.com/windows")

    # Click on "Click Here" link to open new window
    driver.find_element(By.LINK_TEXT, "Click Here").click()

    # Get list of all opened window handles
    windowsOpened = driver.window_handles

    # Switch control to the new (child) window (index 1)
    driver.switch_to.window(windowsOpened[1])

    # Wait to visually verify child window
    time.sleep(2)

    # Capture heading text from child window
    pageLogo = driver.find_element(By.XPATH, "//div[@class='example']/h3").text
    print(pageLogo)

    # Switch back to parent (main) window (index 0)
    driver.switch_to.window(windowsOpened[0])

    # Wait to visually verify parent window
    time.sleep(2)

    # Capture heading text from parent window
    mainLogo = driver.find_element(By.XPATH, "//div[@class='example']/h3").text
    print(mainLogo)

    # Assertion to validate main window content
    assert "Opening a new window" in mainLogo

    # Close the current window (parent window)
    driver.close()
