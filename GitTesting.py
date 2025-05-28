# Import webdriver module from selenium package
from selenium import webdriver
import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

# Instantiate webdriver and launch Chrome browser

driver: WebDriver = webdriver.Chrome()

# Open the specified web page
driver.get("https://jugno.racketail.com/")

time.sleep(10) #wait for 7 seconds to let the page load

#locate tha username web element
#username = driver.find_element(By.NAME, "email")

#relative xpath to locate  username
username = driver.find_element(By.XPATH,"//input[@name='email']")

#enter username
username.send_keys("admin@nexustechinnov.com")#enter username

#locate the password web element
#password = driver.find_element(By.NAME,"password")

#relative xpath to locate passsword
password = driver.find_element(By.XPATH,"//input[@name='password']")

#enter password
password.send_keys("Admin95@#")

#locate the login button
#loginBtn = driver.find_element(By.TYPE,"submit")

#relative xpath to locate login button
loginBtn = driver.find_element(By.XPATH,"//button[@type='submit']")


#click on login button
loginBtn.click()

time.sleep(5)# wait for 5 sec

#reltive xpath to locate web element jugno Dashbord icon and porferm click on icon
dashbordicon = driver.find_element(By.XPATH,"//input[@class='w-[20px] h-[18px] lg:w-[21px] lg:h-[21px] 2xl:w-[31px] 2xl:h-[31px]']")

# #click on all icon
#navbar.click()


time.sleep(15) #wait for 5 seconds


#close the browser window
driver.quit()
