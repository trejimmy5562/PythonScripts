#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 13:38:21 2019

@author: trejimmy5562
"""

from selenium import webdriver 
#launch/open browser
#from selenium.webdriver.common.keys import Keys
#for inputting text
from selenium.webdriver.common.by import By 
#search for things using specific parameters
from selenium.webdriver.support.ui import WebDriverWait 
#wait for page to load
from selenium.webdriver.support import expected_conditions as EC
#specify what you are looking for on page to see if it has loaded
from selenium.common.exceptions import TimeoutException
#handling a timeout situation 


option = webdriver.ChromeOptions()
option.add_argument(" - incognito")
#make it incognito!
browser = webdriver.Chrome(executable_path='/Path/To/chromedriver', chrome_options=option)

browser.get("https://github.com/TheDancerCodes")
#specify which website

# Wait 20 seconds for page to load
timeout = 20
try:
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//img[@class='avatar width-full rounded-2']")))
except TimeoutException:
    print("Timed out waiting for page to load")
    browser.quit()
    

# find_elements_by_xpath returns an array of selenium objects.
#titles_element = browser.find_elements_by_xpath("//a[@class='text-bold']")
# use list comprehension to get the actual repo titles and not the selenium objects.
#titles = [x.text for x in titles_element]
# print out all the titles.
#print('titles:')
#print(titles, '\n')
#Find search bar and input text




