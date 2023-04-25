import time
from selenium.webdriver.support.ui import Select

from selenium import webdriver

from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:\\Users\khape\Downloads\chromedriver_win32 (2)\chrome"
                                        "driver.exe")

driver.get("https://www.instagram.com/accounts/login/")
time.sleep(2)
driver.find_element(By.NAME,'username').send_keys('thats_yash16')
driver.find_element(By.NAME,'password').send_keys('Yash@160616')
driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]').click()
time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="mount_0_0_Na"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div[2]/div/div/div/div[4]/div').click()
time.sleep(12)