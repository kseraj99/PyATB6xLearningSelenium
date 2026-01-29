import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

@allure.title("Function test")
@allure.description("Verify functionality of web page")
def test_full_function_ui():
    # Launch Chrome browser
    driver = webdriver.Chrome()

    # List of expected product names after searching "ber"
    expectedList = ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]

    # Empty list to store actual product names fetched from UI
    actualList = []  # We will use append() to add items dynamically

    # Set implicit wait of 2 seconds (max wait for all elements)
    driver.implicitly_wait(2)
    # If element loads in 1 sec, it won’t wait full 2 sec – it saves time

    # Open the shopping website
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    driver.maximize_window()

    # Enter "ber" in the search box
    driver.find_element(By.CSS_SELECTOR, "input[class='search-keyword']").send_keys("ber")

    # Wait for search results to load
    time.sleep(2)  # Needed because results are loaded dynamically

    # Capture all product cards displayed after search
    results = driver.find_elements(By.XPATH, "//div[@class='products']/div")

    # Get number of products found
    count = len(results)

    # Validate that at least one product is displayed
    assert count > 0

    # Loop through each product
    for result in results:
        # Get product name and store in actualList
        actualList.append(result.find_element(By.XPATH, "h4").text)

        # Click on "Add to Cart" button for each product
        result.find_element(By.XPATH, "div/button").click()

    # Validate expected product list matches actual list
    assert expectedList == actualList

    # Click on Cart icon
    driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()

    # Click on Proceed to Checkout
    driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

    # ------------------- SUM VALIDATION -------------------

    # Capture all product prices in checkout table
    prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")

    sum = 0

    # Add all product prices
    for price in prices:
        sum = sum + int(price.text)

    print(sum)

    # Get the total amount displayed on UI
    totalAmount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)

    # Validate calculated sum equals UI total
    assert sum == totalAmount

    # ------------------- APPLY PROMO CODE -------------------

    # Enter promo code
    driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")

    # Click Apply button
    driver.find_element(By.CSS_SELECTOR, "button[class='promoBtn']").click()

    # Wait until promo confirmation message appears
    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoInfo")))

    # Print promo message
    print(driver.find_element(By.CLASS_NAME, "promoInfo").text)

    # Get discounted amount
    discountAmount = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)

    # Validate discount is applied
    assert totalAmount > discountAmount

    # ------------------- PLACE ORDER -------------------

    # Click Place Order button
    driver.find_element(By.XPATH, "//button[text()='Place Order']").click()

    # Capture all country options
    countries = driver.find_elements(By.XPATH, "//select[@style='width: 200px;']")

    # Select India from dropdown
    for country in countries:
        if country.text == "India":
            country.click()
            break

    # Accept Terms & Conditions checkbox
    driver.find_element(By.CSS_SELECTOR, ".chkAgree").click()

    # Click Proceed button
    driver.find_element(By.XPATH, "//button[text()='Proceed']").click()

    # Wait before closing browser
    time.sleep(2)

    # Close the browser
    driver.close()

