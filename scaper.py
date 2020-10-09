from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selectorlib import Extractor
import requests
import json
import time

def get_jobs(job,location):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("http://www.indeed.com")
    #job search what id = "text-input-what"
    #location where id = "text-input-where"
    job_box = driver.find_element_by_id("text-input-what").send_keys(job)
    #location_box = driver.find_element_by_id("text-input-where").clear()
    
    driver.implicitly_wait(1)
    #location_box = driver.find_element_by_id("text-input-where").send_keys(location)
    #icl-WhatWhere-buttonWrapper
    #icl-Button icl-Button--primary icl-Button--md icl-WhatWhere-button
    search_button = driver.find_element_by_class_name("icl-WhatWhere-buttonWrapper").click()


get_jobs("data science", "New Jersey")