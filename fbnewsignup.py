import time

from selenium import webdriver

from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:\\Yash\yash e\chromedriver_win32\chromedriver.exe")
driver.get("https://www.facebook.com/")
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="login_link"]/div[3]').send_keys('ROMAN')
time.sleep(2)
