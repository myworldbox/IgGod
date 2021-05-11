from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait 
from selenium import webdriver
import time

driver =  webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.instagram.com")

time.sleep (2)

driver.find_element_by_css_selector("input[name='username']").send_keys('username')
driver.find_element_by_css_selector("input[name='password']").send_keys('password')
driver.find_element_by_xpath("//button[@type='submit']").click()

time.sleep(2)

WebDriverWait(driver, 15).until(lambda d: d.find_element_by_xpath('//button[text()="Not Now"]')).click()
WebDriverWait(driver, 15).until(lambda d: d.find_element_by_xpath('//button[text()="Not Now"]')).click()

driver.find_element_by_xpath('//div[text()="See All"]').click() 

for i in range (100):

    time.sleep(2)
    
    driver.execute_script("arguments[0].click();", driver.find_element_by_xpath('//button[text()="Follow"]'))