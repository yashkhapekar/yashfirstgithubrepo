import time
from selenium.webdriver.support.ui import Select

from selenium import webdriver

from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:\\Users\khape\Downloads\chromedriver_win32 (2)\chromedriver.exe")

driver.get("http://mitintech.com/admin/")
driver.find_element(By.NAME,'username').send_keys('YASHKHAPEKAR')
time.sleep(2)
driver.find_element(By.NAME,'password').send_keys('YASH@160620')
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="login-form"]/div[3]/input').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="content-main"]/div[3]/table/tbody/tr[9]/th/a').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="nav-sidebar"]/div[3]/table/tbody/tr[9]/td/a').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="content"]/h1').click()
time.sleep(2)
driver.find_element(By.NAME,'worksheet1').send_keys("C:\\Users\khape\\Downloads\\JAI BHOLE ENTERPRIZES (1).pdf")
time.sleep(2)
driver.find_element(By.NAME,'worksheet2').send_keys("C:\\Users\khape\\Downloads\\JAI BHOLE ENTERPRIZES (1).pdf")
time.sleep(2)
yash=Select(driver.find_element(By.NAME,'subject'))
yash.select_by_index(44)
time.sleep(2)
yash=Select(driver.find_element(By.NAME,'bookseries'))
yash.select_by_index(26)
time.sleep(2)
yash=Select(driver.find_element(By.NAME,'classid'))
yash.select_by_index(5)
time.sleep(2)
yash=Select(driver.find_element(By.NAME,'chapter'))
yash.select_by_index(18)
time.sleep(2)
driver.find_element(By.NAME,'_save').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="nav-sidebar"]/div[3]/table/tbody/tr[8]/th/a').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="nav-sidebar"]/div[3]/table/tbody/tr[8]/td/a').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="content"]/h1').click()
time.sleep(2)
yash=Select(driver.find_element(By.NAME,'user'))
yash.select_by_index(4)
time.sleep(2)
driver.find_element(By.NAME,'schools').send_keys('SINDHI HINDI HIGH SCHOOL')
time.sleep(2)
yash=Select(driver.find_element(By.NAME,'subject'))
yash.select_by_index(44)
time.sleep(2)
yash=Select(driver.find_element(By.NAME,'bookseries'))
yash.select_by_index(26)
time.sleep(2)
yash=Select(driver.find_element(By.NAME,'state'))
yash.select_by_index(1)
time.sleep(2)
yash=Select(driver.find_element(By.NAME,'city'))
yash.select_by_index(1)
time.sleep(2)
driver.find_element(By.NAME,'mobile').send_keys("7420921250 ")
time.sleep(2)
driver.find_element(By.NAME,'status').click()
time.sleep(2)
driver.find_element(By.NAME,'_save').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="nav-sidebar"]/div[3]/table/tbody/tr[7]/th/a').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="nav-sidebar"]/div[3]/table/tbody/tr[7]/td/a').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="content"]/h1').click()
time.sleep(2)
yash=Select(driver.find_element(By.NAME,'subject'))
yash.select_by_index(44)
time.sleep(2)
yash=Select(driver.find_element(By.NAME,'bookseries'))
yash.select_by_index(26)
time.sleep(2)
yash=Select(driver.find_element(By.NAME,'classid'))
yash.select_by_index(5)
time.sleep(2)
driver.find_element(By.NAME,'viewbook').send_keys("C:\\Users\khape\\Downloads\\JAI BHOLE ENTERPRIZES (1).pdf")
time.sleep(2)
driver.find_element(By.NAME,'_save').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="nav-sidebar"]/div[3]/table/tbody/tr[5]/th/a').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="nav-sidebar"]/div[3]/table/tbody/tr[5]/td/a').click()
time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="content"]/h1').click()
time.sleep(3)
driver.find_element(By.NAME,'state').send_keys('MAHARASTRA ')
time.sleep(3)
driver.find_element(By.NAME,'_save').click()
time.sleep(3)
