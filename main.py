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
# used time.sleep to give browser enough time to adapte to updates 
def dep_country_chooser(dep_country):
    fly_from = browser.find_element_by_xpath("//input[@id='flight-origin-hp-flight']")
    time.sleep(1)
    # clear any preexisting value
    fly_from.clear()
    time.sleep(1.5)
    fly_from.send_keys('  ' + dep_country)
    time.sleep(1.5)
    # click first option
    first_item = browser.find_element_by_xpath("//a[@id='aria-option-0']")
    time.sleep(1.5)
    first_item.click()

# same logic for arrival country 
def arrival_country_chooser(arrival_country):
    fly_to = browser.find_element_by_xpath("//input[@id='flight-destination-hp-flight']")
    time.sleep(1)
    fly_to.clear()
    time.sleep(1.5)
    fly_to.send_keys('  ' + arrival_country)
    time.sleep(1.5)
    first_item = browser.find_element_by_xpath("//a[@id='aria-option-0']")
    time.sleep(1.5)
    first_item.click()

# choose departure dates
def dep_date_chooser(month, day, year):
    # find element on page
    dep_date_button = browser.find_element_by_xpath("//input[@id='flight-departing-hp-flight']")
    # clear any preexisting value
    dep_date_button.clear()
    # fill element with date
    dep_date_button.send_keys(month + '/' + day + '/' + year)

# choose return date 
# clearning was not working, used .BACKSPACE instead
def return_date_chooser(month, day, year):
    return_date_button = browser.find_element_by_xpath("//input[@id='flight-returning-hp-flight']")
    
    for i in range(11):
        return_date_button.send_keys(Keys.BACKSPACE)
    return_date_button.send_keys(month + '/' + day + '/' + year)


# function clicks the search button
def search():
    # finds search element on page
    search = browser.find_element_by_xpath("//button[@class='btn-primary btn-action gcw-submit']")
    # clicks search
    search.click()
    # time delay to let browser process
    time.sleep(15)
    print('Results ready!')