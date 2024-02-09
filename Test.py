import time
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.google.com/")
driver.maximize_window()
time.sleep(5)
driver.close()
