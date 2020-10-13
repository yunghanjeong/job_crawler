from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selectorlib import Extractor
import requests
import json
import time
import os

#this fucntion opens chrome and goes to linked in and serach
def get_jobs(job,location):
    #Use the line below for install
    #driver = webdriver.Chrome(ChromeDriverManager().install())
    driver = webdriver.Chrome(r"C:\Users\Yung\.wdm\drivers\chromedriver\win32\85.0.4183.87\chromedriver.exe")
    driver.get("http://www.indeed.com")
    #enters job string into what box
    driver.find_element_by_id("text-input-what").send_keys(job)
    
    
    #enters location into where box
    #below is necessary for clearing preexisting location input
    driver.find_element_by_id("text-input-where").send_keys(Keys.CONTROL + "a") #select everything in location
    driver.find_element_by_id("text-input-where").send_keys(Keys.BACKSPACE)
    
    #enter location
    driver.find_element_by_id("text-input-where").send_keys(location)
    #press enter to search
    driver.find_element_by_id("text-input-where").send_keys(Keys.ENTER)
    
    driver.implicitly_wait(1)



get_jobs("data science", "New Jersey")