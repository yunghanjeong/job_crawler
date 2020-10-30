from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selectorlib import Extractor
import random
from bs4 import BeautifulSoup
import requests
import json
import time
import os

class job_crawler():
    #initialize self
    def __init__(self):
        driver_loc = r"C:\Users\Yung\.wdm\drivers\chromedriver\win32\85.0.4183.87\chromedriver.exe"
        self.driver =  webdriver.Chrome(driver_loc)
    
    #wait random amoutn of times
    def wait_random(self):
        picktime = random.choice(range(0,5))
        self.driver.implicitly_wait(picktime)
    
    #this fucntion opens chrome and goes to linked in and serach
    def get_jobs(self, job,location):
        driver = self.driver
        #Use the line below for install
        #go to this website
        driver.get("http://www.indeed.com")
        
        #enters job string into what box
        driver.find_element_by_id("text-input-what").send_keys(job)
        
        #enters location into where box
        #below is necessary for clearing preexisting location input
        driver.find_element_by_id("text-input-where").send_keys(Keys.CONTROL + "a") #select everything in location
        driver.find_element_by_id("text-input-where").send_keys(Keys.BACKSPACE) #delete to clear
        
        #enter location
        driver.find_element_by_id("text-input-where").send_keys(location)
        #press enter to search
        driver.find_element_by_id("text-input-where").send_keys(Keys.ENTER)
        return driver.current_url
        
    def get_html(self, url):
        req = requests.get(url)
        soup = BeautifulSoup(req.content, "html.parser")
        return soup


crawler = job_crawler()
url = crawler.get_jobs("data science", "New Jersey")
html_soup = crawler.get_html(url)
a_html = html_soup.find_all("a")
ans = []
for link in a_html:
    test = str(link.get("href")).split("&")
    try:
        ans.append(test[1])
    except:
        continue