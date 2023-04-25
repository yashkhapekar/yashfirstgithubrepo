import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from selenium.webdriver.common.by  import By

driver=webdriver.Chrome(executable_path="C:\\Yash\yash e\chromedriver_win32\chromedriver.exe")
driver.get("http://mitintech.com/admin")
xyz=WebDriverWait(driver,3)
xyz.until (expected_conditions.presence_of_element_located((By.NAME,'username'))).send_keys('yash')
driver.find_element(By.NAME,'username').send_keys('YASHKHAPEKAR')
driver.find_element(By.NAME,'password').send_keys('YASH@160620')
driver.find_element(By.XPATH,'//*[@id="login-form"]/div[3]/input').click()
