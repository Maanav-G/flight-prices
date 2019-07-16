# access websites and automate testing
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# pandas for data structuring 
import pandas as pd

import time
import datetime

# connecting email
import smtplib
from email.mime.multipart import MIMEMultipart

# connect to the web broswer for automated testing
browser = webdriver.Chrome(executable_path='/Users/maanav/chromedriver')

# set the fligth path 
return_ticket = "//label[@id='flight-type-roundtrip-label-hp-flight']"
one_way_ticket = "//label[@id='flight-type-one-way-label-hp-flight']"
multi_ticket = "//label[@id='flight-type-multi-dest-label-hp-flight']"

# function that chooses a ticket type 
def ticket_chooser(ticket):
    try:
        ticket_type = browser.find_element_by_xpath(ticket)
        ticket_type.click()
    except Exception as e:
        pass

# function that chooses departure country
def dep_country_chooser(dep_country):
    fly_from = browser.find_element_by_xpath("//input[@id='flight-origin-hp-flight']")
    time.sleep(1)
    fly_from.clear()
    time.sleep(1.5)
    fly_from.send_keys('  ' + dep_country)
    time.sleep(1.5)
    first_item = browser.find_element_by_xpath("//a[@id='aria-option-0']")
    time.sleep(1.5)
    first_item.click()