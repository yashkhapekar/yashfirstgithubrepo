import time

from selenium import webdriver

from selenium.webdriver.common.by  import By

driver=webdriver.Chrome(executable_path="C:\\Yash\yash e\chromedriver_win32\chromedriver.exe")
driver.get("http://mitintech.com/admin")
time.sleep(2)
driver.find_element(By.NAME,'username').send_keys('YASHKHAPEKAR')
driver.find_element(By.NAME,'password').send_keys('YASH@160620')
driver.find_element(By.XPATH,'//*[@id="login-form"]/div[3]/input').click()
time.sleep(5)
driver.find_element(By.LINK_TEXT,'Subjects').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="nav-sidebar"]/div[2]/table/tbody/tr[4]/td/a').click()
driver.find_element(By.XPATH,'//*[@id="content"]/h1').click()
driver.find_element(By.NAME,'name').send_keys('Electronics')
time
driver.find_element(By.NAME,'description').send_keys('THIS FVT SUBJECT IS ELECTRONICS')
time.sleep(4)
driver.find_element(By.NAME,'_save').click()
time.sleep(4)
driver.find_element(By.NAME,'name').send_keys('ELECTRONICS 1')
driver.find_element(By.NAME,'_addanother').click()
time.sleep(3)
driver.find_element(By.NAME,'name').send_keys('ELECTRONICS 2')
driver.find_element(By.NAME,'_continue').click()
time.sleep(2)
driver.find_element(By.LINK_TEXT,'Book Series').click()
time.sleep(4)
driver.find_element(By.XPATH,'//*[@id="nav-sidebar"]/div[2]/table/tbody/tr[1]/td/a').click()
time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="content"]/h1').click()
time.sleep(1)

time.sleep(3)
driver.find_element(By.NAME,'name').send_keys('ELECTRONIC IS BASED ON COMMUNICATION ENGINEERING ')
time.sleep(2)
driver.find_element(By.NAME,'_save').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="nav-sidebar"]/div[2]/table/tbody/tr[3]/th/a').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="nav-sidebar"]/div[2]/table/tbody/tr[3]/td/a').click()
time.sleep(3)
driver.find_element(By.NAME,'name').send_keys('12th')
time.sleep(2)
driver.find_element(By.NAME,'_save').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="nav-sidebar"]/div[2]/table/tbody/tr[2]/th/a').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="nav-sidebar"]/div[2]/table/tbody/tr[2]/td/a').click()
time.sleep(2)
driver.find_element(By.NAME,'name').send_keys('YASH')
time.sleep(2)
driver.find_element(By.NAME,'subject').send_keys('ELECTRONICS')
time.sleep(2)
driver.find_element(By.NAME,'bookseries'). send_keys('ELECTRONICS IS BASED ON COMMUNICATIOM')
time.sleep(2)
driver.find_element(By.NAME,'classid').send_keys('12th')
time.sleep(2)
driver.find_element(By.NAME,'_save').click()
time.sleep(10)