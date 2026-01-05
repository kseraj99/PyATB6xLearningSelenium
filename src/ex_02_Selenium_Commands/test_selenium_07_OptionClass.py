import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_chrome_options():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--headless")


    driver = webdriver.Chrome(chrome_options)

    driver.get("https://katalon-demo-cura.herokuapp.com/")

    time.sleep(2)
    driver.quit()