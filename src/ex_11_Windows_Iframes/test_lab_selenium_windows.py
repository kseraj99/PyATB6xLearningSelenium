"""
Project-Windows Automation
Verify that on this URL, when a person click on the click here button,
it opens a new window. Where a new window is written, you have to verify that also.

https://the-internet.herokuapp.com/windows

"""
import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

@allure.title("Windows")
@allure.description("Verify windows")
def test_verify_windows():

    # Create Chrome options object
    chrome_options = Options()

    # Launch browser in incognito mode
    chrome_options.add_argument("--incognito")

    # Launch Chrome browser with options
    driver = webdriver.Chrome(options=chrome_options)

    # Open the test URL
    driver.get("https://the-internet.herokuapp.com/windows")

    # Maximize the browser window
    driver.maximize_window()

    # Apply implicit wait of 2 seconds
    driver.implicitly_wait(2)

    # Store parent (main) window handle ID
    parent_window = driver.current_window_handle
    print(parent_window)
    # Example output: D2D5066134CDFCD44D8EE4286690EBCB

    # Locate the "Click Here" link which opens a new window
    click_button = driver.find_element(By.XPATH, "//a[normalize-space()='Click Here']")

    # Click on the link to open new window
    click_button.click()

    # Get all window handles (parent + child windows)
    window_handles = driver.window_handles
    print(window_handles)
    # Example output: ['87C0FCD6FA49ED17803110B306F15213', '5566ABD8A67A820491C310400A6E1F62']

    # Loop through all window handles
    for handles in window_handles:

        # Switch control to each window
        driver.switch_to.window(handles)

        # Check if the current window contains "New Window" text
        if "New Window" in driver.page_source:
            print("Test Pass!!")   # Validation success
            break

    # Wait to visually verify the result
    time.sleep(2)


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



