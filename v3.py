# -*- coding: utf-8 -*-
"""
Created on Thu Dec 03 01:09:39 2015

@author: Laksh
"""

import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def drivers(dot_email):
    driver=webdriver.Chrome()
    driver.implicitly_wait(30)
    driver.get('https://www.pi-supply.com/giveaways/black-piday-giveaway/?lucky=11750')
    driver.find_element_by_xpath("//select[@id='giveaways_answer']/option[text()='Pi Supply, duh!']").click()
    driver.find_element_by_id("giveaways_email").send_keys(dot_email)
    driver.find_element_by_xpath("//button").click()
    time.sleep(7)
    driver.quit()

def one_dot():
    for number in range(1,at_d_rate):
        for dot_number in range(1,100):
            str_dot = dot_number*'.'
            dot_email = email_id[0:number] + str_dot + email_id[number:]
            drivers(dot_email)
            print dot_email
            
def two_dot():
    for number in range(1,at_d_rate):
        str_dot = number*'.'
        dot_email = email_id[0:number] + str_dot + email_id[number:]
        print dot_email

def dot_dot():
    for number in range(1,10):
        print number*'.'

email_id = raw_input('Enter your fake email id: \n')
at_d_rate = email_id.find('@')
one_dot()
