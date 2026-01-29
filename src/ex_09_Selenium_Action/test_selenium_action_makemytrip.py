import time
import allure
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.title("Makemytrip")
@allure.description("Verify makemytrip booking")
def test_makemytrip_booking():

    chrome_options = Options()
    chrome_options.add_argument("--incognito")

    # Launch Chrome
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()

    driver.get("https://www.makemytrip.com/")

    wait = WebDriverWait(driver, 15)

    # Close login popup
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@data-cy='closeModal']"))).click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//span[@class='coachmark']").click()
    # Click From city
    time.sleep(2)


    #  Type "del"
    actions = ActionChains(driver)
    actions.move_to_element(fromCi)


    #
    # # Wait for city list
    # cities = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//span[@class='revampedCityName']")))
    #
    # for city in cities:
    #     if city.text == "New Delhi, India":
    #         driver.execute_script("arguments[0].scrollIntoView(true);", city)
    #         time.sleep(1)
    #         driver.execute_script("arguments[0].click();", city)
    #         break
    #
    # # Read selected value
    # wait.until(EC.text_to_be_present_in_element_value(
    #     (By.XPATH, "//input[@placeholder='From']"),
    #     "New Delhi"
    # ))
    # selected_city = driver.find_element(By.XPATH, "//input[@placeholder='From']").get_attribute("value")
    #
    # print("Selected City:", selected_city)
    #
    # assert selected_city == "New Delhi, India"

    time.sleep(3)
    driver.quit()
