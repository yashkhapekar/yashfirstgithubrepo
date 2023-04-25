import time

from selenium import webdriver

from selenium.webdriver.common.by  import By

driver=webdriver.Chrome(executable_path="C:\\Yash\yash e\chromedriver_win32\chromedriver.exe")
driver.get("http://mitintech.com/admin")
driver.implicitly_wait(3)
driver.find_element(By.NAME,'username').send_keys('YASHKHAPEKAR')
driver.find_element(By.NAME,'password').send_keys('YASH@160620')
driver.find_element(By.XPATH,'//*[@id="login-form"]/div[3]/input').click()
driver.find_element(By.LINK_TEXT,'Subjects').click()
driver.find_element(By.XPATH,'//*[@id="nav-sidebar"]/div[2]/table/tbody/tr[4]/td/a').click()
driver.find_element(By.XPATH,'//*[@id="content"]/h1').click()
driver.find_element(By.NAME,'name').send_keys('Electronics')

driver.find_element(By.NAME,'description').send_keys('this is my fvt subject')
driver.find_element(By.NAME,'_save').click()
driver.find_element(By.NAME,'name').send_keys('ELECTRONICS 1')
driver.find_element(By.NAME,'_addanother').click()
driver.find_element(By.NAME,'name').send_keys('ELECTRONICS 2')
driver.find_element(By.NAME,'_continue').click()