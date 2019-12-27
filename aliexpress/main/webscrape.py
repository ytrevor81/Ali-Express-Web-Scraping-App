from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time
import random

'''All functionality related to webscraping goes into this file'''

delay = random.randint(10,100)
scrollheight = 1000

class BrowserControl(object):
    '''Controls the browser's behavior and requests. This class consists of only 2 methods for convinience:
    a 20+ line method to prepare the page source for BeautifulSoup, and a short method that will be called
    in views.py after the page source is processed by BeautifulSoup'''

    @classmethod
    def login_page(cls, webdriver):
        '''Logins into the fake account'''
        WebDriverWait(webdriver, delay).until(EC.frame_to_be_available_and_switch_to_it((By.ID,"alibaba-login-box")))     #makes <iframe> login-form useable
        WebDriverWait(webdriver, delay)    #waits for a random amount of time, so that aliexpress cannot detect this app as a  robot

        webdriver.find_element_by_xpath('//*[@id="fm-login-id"]').send_keys("deanyoung800@gmail.com")      #Finds username box and enters username of fake account
        WebDriverWait(webdriver, delay)

        webdriver.find_element_by_id("fm-login-password").send_keys("Cosmos000")   #Finds password box and enters password of fake account
        WebDriverWait(webdriver, delay)

        webdriver.find_element_by_xpath('//*[@id="login-form"]/div[5]/button').click()     #Clicks the log-in button
        WebDriverWait(webdriver, delay)

    @classmethod
    def scroll_timer(cls, webdriver):
        '''Sets a timer for scrolling down the page'''
        for timer in range(0,50):
            webdriver.execute_script("window.scrollTo(0, "+ str(scrollheight) +")")
            y += 1000
            time.sleep(1)

    @classmethod
    def prepare_page_source(cls, search):
        '''The product search is the parameter. This function will open the browser and will return
        the webdriver object for processing the page source in data_parser.py with BeautifulSoup'''

        link = "https://www.aliexpress.com/wholesale?catId=0&initiative_id=SB_20181225216320&SearchText=" + search  #main link used for this webapp
        chromepath = "C://Users/User/Desktop/chromedriver/chromedriver.exe"     #path of robot-controlled browser
        driver = webdriver.Chrome(chromepath)   #opens browser
        #driver.set_window_position(-10000,0)    #keeps the browser out of the user's sight
        driver.get(ali)     #sends request
        
        self.login_page(driver)     #logins into the account

        WebDriverWait(driver, delay).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="search-key"]')))   #locates the search-bar of the page, just to add extra time
        self.scroll_timer(driver)   #scrolls down the page at a specific time

        return driver   #returns webdriver object to data_parser.py for BeautifulSoup processing

    @classmethod
    def close_browser(cls, webdriver):
        '''Closes the browser after a delay. This method will be called in data_parser.py'''
        WebDriverWait(webdriver, delay)
        webdriver.close()
