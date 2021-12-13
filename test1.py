import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.google.com/")
driver.maximize_window()
time.sleep(5)
gmail=driver.find_element(By.XPATH,"//a[normalize-space()='Gmail']")
action = ActionChains(driver)
time.sleep(5)
action.context_click(gmail).perform()
