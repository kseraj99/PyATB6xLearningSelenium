import allure
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.title("SVG part2")
@allure.description("SVG part2 Verification")
def test_svg_part2():
    driver = webdriver.Chrome()
    driver.get("https://www.amcharts.com/svg-maps/?map=india")
    list_of_states = driver.find_elements(By.XPATH,
                                          "//*[name()='svg']/*[name()='g'][7]/*[name()='g']/*[name()='g']/*[name()='path']")
    for states in list_of_states:
        print(states.get_attribute("aria-label"))
        if "Bihar" in states.get_attribute("aria-label"):
            states.click()
            break


    time.sleep(2)
    driver.quit()