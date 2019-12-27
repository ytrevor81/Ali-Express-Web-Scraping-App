
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import requests
from bs4 import BeautifulSoup
import time
import random





product = "tiger"
amazon = 'https://www.amazon.com/s?k=tapestries&ref=nb_sb_noss_1'
ali = "https://www.aliexpress.com/wholesale?catId=0&initiative_id=SB_20181225216320&SearchText=" + product

#request = requests.get(amazon)

chromepath = "C://Users/User/Desktop/chromedriver/chromedriver.exe"
driver = webdriver.Chrome(chromepath)
#driver.set_window_position(-10000,0)
driver.get(ali)

delay = random.randint(10,100)

WebDriverWait(driver, delay).until(EC.frame_to_be_available_and_switch_to_it((By.ID,"alibaba-login-box")))
WebDriverWait(driver, delay)
driver.find_element_by_xpath('//*[@id="fm-login-id"]').send_keys("deanyoung800@gmail.com")
WebDriverWait(driver, delay)
driver.find_element_by_id("fm-login-password").send_keys("Cosmos000")
WebDriverWait(driver, delay)
driver.find_element_by_xpath('//*[@id="login-form"]/div[5]/button').click()

WebDriverWait(driver, delay)
WebDriverWait(driver, delay).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="search-key"]')))
y = 1000
for timer in range(0,50):
    driver.execute_script("window.scrollTo(0, "+str(y)+")")
    y += 1000
    time.sleep(1)

html = driver.page_source
soup = BeautifulSoup(html, 'lxml')
WebDriverWait(driver, delay)



driver.close()

supplier = soup.find_all('a', {'class': "store-name"})
shipping = soup.find_all('span', {'class': "shipping-value"})

product_titles = soup.find_all('a', {'class':"item-title"})
product_prices = soup.find_all('span', {'class':"price-current"})
product_ratings = soup.find_all('span', {'class':"rating-value"})
products_sold = soup.find_all('a', {'class':"sale-value-link"})

titles = [x.get_text() for x in product_titles]
prices = [x.get_text() for x in product_prices]
ratings = [x.get_text() for x in product_ratings]
sold = [x.get_text() for x in products_sold]
suppliers = [x.get_text() for x in supplier]
free_shipping = [x.get_text() for x in shipping]


print(titles, len(titles))
print(prices, len(prices))
print(ratings, len(ratings))
print(sold, len(sold))
print(suppliers, len(suppliers))
print(free_shipping, len(free_shipping))
