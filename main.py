from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

import pandas
import time

count = 0

driver =  webdriver.Chrome(ChromeDriverManager().install())

list = pandas.read_csv("contact.csv", dtype = str).to_dict('list')

driver.get("https://www.instagram.com")

time.sleep (1)

driver.find_element_by_css_selector("input[name='username']").send_keys('username')
driver.find_element_by_css_selector("input[name='password']").send_keys('password')
driver.find_element_by_xpath("//button[@type='submit']").click()

time.sleep(1)

WebDriverWait(driver, 15).until(lambda d: d.find_element_by_xpath('//button[text()="Not Now"]')).click()
WebDriverWait(driver, 15).until(lambda d: d.find_element_by_xpath('//button[text()="Not Now"]')).click()

for username in zip(list['username']):

    driver.get("https://www.instagram.com/"+str(list['username'][count]))

    try:

        WebDriverWait(driver, 15).until(lambda d: d.find_element_by_xpath('//button[text()="Follow"]')).click()

    except:

        pass

    count = count + 1
    time.sleep(2)