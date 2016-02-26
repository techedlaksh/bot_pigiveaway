# -*- coding: utf-8 -*-
"""
Created on Thu Dec 03 00:27:53 2015

@author: Laksh
"""




#choice = raw_input("Enter the address!!")
driver=webdriver.Chrome("V:\Back\Compressed\chromedriver_win32\chromedriver.exe")
driver.implicitly_wait(30)
driver.get('https://www.pi-supply.com/giveaways/black-piday-giveaway/?lucky=11998')
driver.find_element_by_xpath("//select[@id='giveaways_answer']/option[text()='Pi Supply, duh!']").click()
driver.find_element_by_id("giveaways_email").send_keys("la.ksharora123@gmail.com")
driver.find_element_by_xpath("//button").click()
driver.quit()