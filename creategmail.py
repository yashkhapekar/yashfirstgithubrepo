import time

from selenium import webdriver

from selenium.webdriver.common.by  import By

driver=webdriver.Chrome(executable_path="C:\\Yash\yash e\chromedriver_win32\chromedriver.exe")
driver.get("https://www.gmail.com/")
time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div[2]/div/div[2]/div/div/div[1]/div/button/span').click()
driver.find_element(By.XPATH,'//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div/ul/li[1]/span[2]').click()
driver.find_element(By.NAME,'firstName').send_keys('yash')
driver.find_element(By.NAME,'lastName').send_keys('khapekar')
driver.find_element(By.NAME,'Username').send_keys('khapekaryash76')
driver.find_element(By.NAME,'Passwd').send_keys('Yash@980')
time.sleep(4)
driver.find_element(By.NAME,'ConfirmPasswd').send_keys('Yash@980')
driver.find_element(By.XPATH,'//input[@type="checkbox"]').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="accountDetailsNext"]/div/button/span').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="phoneNumberId"]').send_keys(9373141119)
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button').click()




