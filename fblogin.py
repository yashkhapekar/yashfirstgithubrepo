import time

from selenium import webdriver

from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:\\Yash\yash e\chromedriver_win32\chromedriver.exe")
driver.get("https://www.facebook.com/login/")
time.sleep(2)
driver.find_element(By.NAME,'email').send_keys(' ')
time.sleep(3)
driver.find_element(By.NAME,'pass').send_keys('')
time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="loginbutton"]').click()
time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="login_link"]').click()
time.sleep(3)
driver.find_element(By.NAME,'email').send_keys('')
time.sleep(3)